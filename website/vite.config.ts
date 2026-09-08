import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";
import { staticPages } from "./scripts/static-pages";
import { GITHUB_PAGES_BASE } from "./src/lib/routes";

export default defineConfig(({ command, isPreview }) => ({
  base: command === "build" || isPreview ? GITHUB_PAGES_BASE : "/",
  plugins: [react(), staticPages()],
  build: {
    target: "es2022",
    sourcemap: true,
  },
}));
