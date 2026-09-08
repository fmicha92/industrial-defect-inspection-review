// @vitest-environment jsdom
import { cleanup, render, screen, within } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { afterEach, expect, it } from "vitest";
import meta from "../../public/data/meta.json";
import { SiteLayout } from "./Layout";

afterEach(cleanup);

it("shows the navigation without a snapshot date in the top bar", () => {
  render(
    <MemoryRouter>
      <SiteLayout meta={meta}>
        <h1>Evidence explorer</h1>
      </SiteLayout>
    </MemoryRouter>,
  );
  const header = within(screen.getByRole("banner"));
  expect(header.queryByText(/Graph snapshot/i)).toBeNull();
  expect(header.queryByText(/Aug 27, 2026/)).toBeNull();
  expect(
    header.getByRole("link", { name: "Industrial Inspection Evidence Explorer home" }),
  ).toBeDefined();
  expect(
    within(header.getByRole("navigation", { name: "Primary navigation" })).getAllByRole("link"),
  ).toHaveLength(4);
  const footer = within(screen.getByRole("contentinfo"));
  expect(footer.getByText(meta.title)).toBeDefined();
  expect(footer.getByText(meta.authors.join(" · "))).toBeDefined();
});
