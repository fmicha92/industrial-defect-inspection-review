import type { Plugin } from "vite";
import { sitePages } from "../src/lib/routes";

export function staticPages(): Plugin {
  return {
    name: "static-route-pages",
    apply: "build",
    generateBundle: {
      order: "post",
      handler(_options, bundle) {
        const entry = bundle["index.html"];
        if (!entry || entry.type !== "asset" || typeof entry.source !== "string") {
          throw new Error("The built index.html is required to generate static route pages.");
        }
        const template = entry.source;
        for (const page of sitePages) {
          const title = page.title.replaceAll("&", "&amp;");
          const source = template.replace(/<title>.*?<\/title>/s, `<title>${title}</title>`);
          if (page.path === "/") entry.source = source;
          else
            this.emitFile({ type: "asset", fileName: `${page.path.slice(1)}index.html`, source });
        }
      },
    },
  };
}
