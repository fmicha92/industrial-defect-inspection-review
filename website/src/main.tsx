import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import { cleanSiteUrl } from "./lib/routes";
import "./styles.css";
import "./theme.css";

const cleanUrl = cleanSiteUrl(window.location.href, import.meta.env.BASE_URL);
if (cleanUrl) window.history.replaceState(window.history.state, "", cleanUrl);

const root = document.getElementById("root");
if (!root) throw new Error("Missing #root application mount");

createRoot(root).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
