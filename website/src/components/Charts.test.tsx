// @vitest-environment jsdom
import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";
import { ChangeDistribution, EvidenceScatter } from "./Charts";

afterEach(cleanup);
const item = {
  id: "E01",
  dataset: "Dataset",
  representative: { metric: "Accuracy", baseline: 80, after: 90, normalizedChange: 0.5 },
  categories: { domain: "Metals", concept: "Classification", model: "CNN", family: "GAN" },
};
describe("evidence chart controls", () => {
  it.each(["click", "Enter", " "])("opens a comparison with %s", (action) => {
    const select = vi.fn();
    render(<EvidenceScatter items={[item]} onSelect={select} />);
    const point = screen.getByRole("button", { name: /E01: Dataset/ });
    if (action === "click") fireEvent.click(point);
    else fireEvent.keyDown(point, { key: action });
    expect(select.mock.calls[0][0]).toBe("E01");
    expect(select.mock.calls[0][1]).toBe(point);
  });
  it("explains an empty chart", () => {
    render(<EvidenceScatter items={[]} />);
    expect(screen.getByRole("status").textContent).toContain("No points match");
  });
});

describe("normalized-change distribution controls", () => {
  it.each(["click", "Enter", " "])("opens the original comparison with %s", (action) => {
    const select = vi.fn();
    render(<ChangeDistribution items={[item]} onSelect={select} />);
    const point = screen.getByRole("button", { name: /E01: Dataset/ });
    if (action === "click") fireEvent.click(point);
    else fireEvent.keyDown(point, { key: action });
    expect(select.mock.calls[0][0]).toBe("E01");
    expect(select.mock.calls[0][1]).toBe(point);
    expect(point.getAttribute("fill")).toBe("#2d7182");
    expect(screen.getByText("median 0.43")).toBeDefined();
  });
});
