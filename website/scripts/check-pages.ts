import assert from "node:assert/strict";
import { once } from "node:events";
import { readdir, readFile, stat } from "node:fs/promises";
import { createServer } from "node:http";
import { extname, resolve, sep } from "node:path";
import { GITHUB_PAGES_BASE, sitePages } from "../src/lib/routes";

const root = resolve(import.meta.dirname, "../dist");
const publicRoot = resolve(import.meta.dirname, "../public");
const mime: Record<string, string> = {
  ".html": "text/html",
  ".js": "text/javascript",
  ".css": "text/css",
  ".json": "application/json",
  ".csv": "text/csv",
  ".svg": "image/svg+xml",
};

// Serve only existing files, with directory redirects and no SPA fallback.
const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url ?? "/", "http://localhost");
    if (!url.pathname.startsWith(GITHUB_PAGES_BASE)) throw new Error("Outside site");
    let path = resolve(root, decodeURIComponent(url.pathname.slice(GITHUB_PAGES_BASE.length)));
    if (path !== root && !path.startsWith(`${root}${sep}`)) throw new Error("Outside build");
    const info = await stat(path);
    if (info.isDirectory()) {
      if (!url.pathname.endsWith("/")) {
        response.writeHead(301, { Location: `${url.pathname}/${url.search}` });
        response.end();
        return;
      }
      path = resolve(path, "index.html");
    }
    const content = await readFile(path);
    response.writeHead(200, { "Content-Type": mime[extname(path)] ?? "application/octet-stream" });
    response.end(content);
  } catch {
    response.writeHead(404);
    response.end("Not found");
  }
});

async function filesIn(directory: string): Promise<string[]> {
  const entries = await readdir(directory, { withFileTypes: true });
  return (
    await Promise.all(
      entries.map(async (entry) => {
        const path = resolve(directory, entry.name);
        return entry.isDirectory() ? filesIn(path) : [path];
      }),
    )
  ).flat();
}

server.listen(0, "127.0.0.1");
try {
  await once(server, "listening");
  const address = server.address();
  assert(address && typeof address !== "string");
  const origin = `http://127.0.0.1:${address.port}`;
  let checked = 0;
  async function get(path: string, expectedType?: string) {
    const response = await fetch(`${origin}${path}`);
    assert.equal(response.status, 200, `${path} must be a real published file`);
    if (expectedType) assert.equal(response.headers.get("content-type"), expectedType, path);
    checked += 1;
    return response;
  }

  for (const page of sitePages) {
    const path = GITHUB_PAGES_BASE + page.path.slice(1);
    for (const query of ["", "?record=E39", "?node=Papers%2FAlpha+Beta&pin=a&pin=b"]) {
      const html = await (await get(path + query, "text/html")).text();
      assert(html.includes(`<title>${page.title.replaceAll("&", "&amp;")}</title>`), path);
      const assets = [...html.matchAll(/(?:src|href)="([^"]+)"/g)].map((match) => match[1]);
      assert(
        assets.some((asset) => asset.endsWith(".js")),
        `${path}: missing entry script`,
      );
      assert(
        assets.some((asset) => asset.endsWith(".css")),
        `${path}: missing styles`,
      );
      for (const asset of assets) {
        assert(asset.startsWith(GITHUB_PAGES_BASE), `${path}: asset outside repository base`);
        await get(asset, mime[extname(asset)]);
      }
    }
    if (page.path !== "/") {
      const redirect = await fetch(`${origin}${path.slice(0, -1)}?record=E39`, {
        redirect: "manual",
      });
      assert.equal(redirect.status, 301);
      assert.equal(redirect.headers.get("location"), `${path}?record=E39`);
    }
  }
  assert.equal((await fetch(`${origin}${GITHUB_PAGES_BASE}missing/`)).status, 404);

  const publicFiles = await filesIn(publicRoot);
  for (const path of publicFiles) {
    const relative = path
      .slice(publicRoot.length + 1)
      .split(sep)
      .join("/");
    const result = await get(GITHUB_PAGES_BASE + relative, mime[extname(path)]);
    assert.deepEqual(Buffer.from(await result.arrayBuffer()), await readFile(path), relative);
  }
  const builtFiles = await filesIn(root);
  assert(
    !builtFiles.some((path) => /\.(tex|bib|sty|cls)$/i.test(path)),
    "No LaTeX sources in dist",
  );
  const chunks = builtFiles.filter((path) => /GraphExplorer-[^/\\]+\.(js|css)$/.test(path));
  assert.equal(chunks.length, 2, "The graph's lazy script and stylesheet must be published");
  for (const path of chunks) {
    const relative = path
      .slice(root.length + 1)
      .split(sep)
      .join("/");
    await get(GITHUB_PAGES_BASE + relative, mime[extname(path)]);
  }
  console.log(
    `Pages checks passed: ${sitePages.length} routes, ${publicFiles.length} unchanged public files, ${checked} successful static requests.`,
  );
} finally {
  await new Promise<void>((done, reject) =>
    server.close((error) => (error ? reject(error) : done())),
  );
}
