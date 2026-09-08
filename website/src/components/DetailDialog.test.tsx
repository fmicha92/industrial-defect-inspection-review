// @vitest-environment jsdom
import { cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import DetailDialog from "./DetailDialog";

beforeEach(() => {
  vi.stubGlobal("requestAnimationFrame", (callback: FrameRequestCallback) =>
    window.setTimeout(() => callback(0), 0),
  );
  vi.stubGlobal("cancelAnimationFrame", (id: number) => window.clearTimeout(id));
});
afterEach(() => {
  cleanup();
  document.body.replaceChildren();
  document.body.style.overflow = "";
  vi.unstubAllGlobals();
});

describe("record dialog accessibility", () => {
  it.each(["button", "circle"])("restores focus to a connected %s trigger", async (kind) => {
    const shell = document.createElement("div");
    shell.className = "app-shell";
    const trigger =
      kind === "circle"
        ? document.createElementNS("http://www.w3.org/2000/svg", "circle")
        : document.createElement("button");
    trigger.setAttribute("tabindex", "0");
    shell.append(trigger);
    document.body.append(shell);
    (trigger as HTMLElement | SVGElement).focus();
    const view = render(
      <DetailDialog labelId="title" onClose={() => {}} returnFocus={trigger}>
        <h2 id="title">Record</h2>
      </DetailDialog>,
    );
    await waitFor(() => expect(document.activeElement).toBe(screen.getByRole("dialog")));
    expect(shell.inert).toBe(true);
    expect(document.body.style.overflow).toBe("hidden");
    view.unmount();
    expect(shell.inert).toBe(false);
    expect(document.body.style.overflow).toBe("");
    expect(document.activeElement).toBe(trigger);
  });

  it("closes with Escape or the backdrop but not an interior click", () => {
    const close = vi.fn();
    render(
      <DetailDialog labelId="title" onClose={close}>
        <h2 id="title">Record</h2>
      </DetailDialog>,
    );
    fireEvent.click(screen.getByText("Record"));
    expect(close).not.toHaveBeenCalled();
    fireEvent.keyDown(document, { key: "Escape" });
    expect(close).toHaveBeenCalledTimes(1);
    fireEvent.click(screen.getByRole("dialog").parentElement!);
    expect(close).toHaveBeenCalledTimes(2);
  });

  it("retains an existing body scroll lock after dismissal", () => {
    document.body.style.overflow = "hidden";
    const view = render(
      <DetailDialog labelId="title" onClose={() => {}}>
        <h2 id="title">Record</h2>
      </DetailDialog>,
    );
    view.unmount();
    expect(document.body.style.overflow).toBe("hidden");
  });
});
