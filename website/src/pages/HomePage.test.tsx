// @vitest-environment jsdom
import { cleanup, fireEvent, render, screen, within } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { afterEach, describe, expect, it, vi } from "vitest";
import meta from "../../public/data/meta.json";
import type { SiteData } from "../types";
import HomePage from "./HomePage";

vi.mock("../components/GraphExplorer", () => ({
  default: () => <div data-testid="graph-preview" />,
}));

afterEach(() => {
  cleanup();
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
});

const data = {
  meta,
  datasets: { datasets: [] },
  evidence: { items: [] },
  graph: { nodes: [], edges: [] },
} as unknown as SiteData;

async function openHome() {
  render(
    <MemoryRouter>
      <HomePage data={data} />
    </MemoryRouter>,
  );
  await screen.findByTestId("graph-preview");
}

describe("front-page article credit", () => {
  it("shows the exact article title and ordered authors in the banner", async () => {
    await openHome();
    const article = screen.getByRole("region", { name: meta.title });
    expect(within(article).getByRole("heading", { name: meta.title })).toBeDefined();
    expect(article.textContent).toContain(meta.authors.join(" · "));
    expect(article.closest(".hero-section")).not.toBeNull();
    expect(article.closest("details")).toBeNull();
    expect(
      article.compareDocumentPosition(screen.getByTestId("graph-preview")) &
        Node.DOCUMENT_POSITION_FOLLOWING,
    ).toBeTruthy();
  });

  it("keeps the established headline and lower navigation", async () => {
    await openHome();
    expect(
      screen.getByRole("heading", { level: 1, name: /See exactly where.*the evidence holds/ }),
    ).toBeDefined();
    expect(screen.getByRole("heading", { name: "Follow the question you have" })).toBeDefined();
    expect(screen.getByRole("button", { name: "Explore the graph" })).toBeDefined();
  });

  it("includes the principle and continue button in the opening screen before graph navigation", async () => {
    await openHome();
    const hero = screen.getByRole("region", { name: meta.title }).closest(".hero-section");
    const principle = screen.getByRole("region", { name: "Interpretive principle" });
    const graph = screen.getByRole("region", { name: "Evidence graph" });
    const opening = hero?.closest(".opening-screen");
    const continueButton = screen.getByRole("button", { name: "Continue scrolling" });
    expect(opening).not.toBeNull();
    expect(hero?.nextElementSibling).toBe(principle);
    expect(principle.parentElement).toBe(opening);
    expect(continueButton.closest(".principle-band")).toBeNull();
    expect(principle.nextElementSibling).toBe(continueButton.parentElement);
    expect(continueButton.closest(".opening-screen")).toBe(opening);
    expect(opening?.lastElementChild).toBe(continueButton.parentElement);
    expect(opening?.nextElementSibling).toBe(graph);
    expect(continueButton.getAttribute("aria-controls")).toBe(graph.id);
    expect(
      within(graph).getByRole("heading", { name: "Navigate the evidence graph" }),
    ).toBeDefined();
  });

  it.each(
    [true, false].flatMap((reducedMotion) =>
      [
        { scrollY: 0, openingBottom: 900 },
        { scrollY: 320, openingBottom: 900 },
        { scrollY: 180, openingBottom: 1200.25 },
      ].map((geometry) => ({ ...geometry, reducedMotion })),
    ),
  )(
    "scrolls past the entire opening screen from $scrollY to $openingBottom (reduced motion: $reducedMotion)",
    async ({ reducedMotion, scrollY, openingBottom }) => {
      window.matchMedia = vi.fn().mockReturnValue({ matches: reducedMotion });
      vi.stubGlobal("scrollY", scrollY);
      const scrollTo = vi.spyOn(window, "scrollTo").mockImplementation(() => {});
      await openHome();
      const graph = screen.getByRole("region", { name: "Evidence graph" });
      const opening = screen
        .getByRole("button", { name: "Continue scrolling" })
        .closest(".opening-screen") as HTMLElement;
      vi.spyOn(opening, "getBoundingClientRect").mockReturnValue(
        new DOMRect(0, 76 - scrollY, 1440, openingBottom - 76),
      );
      graph.scrollIntoView = vi.fn();
      for (const name of ["Explore the graph", "Continue scrolling"]) {
        fireEvent.click(screen.getByRole("button", { name }));
        expect(document.activeElement).toBe(graph);
        expect(scrollTo).toHaveBeenLastCalledWith({
          top: Math.ceil(openingBottom),
          behavior: reducedMotion ? "instant" : "smooth",
        });
        expect(graph.scrollIntoView).not.toHaveBeenCalled();
      }
    },
  );
});
