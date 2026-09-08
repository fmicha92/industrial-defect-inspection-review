import { type ReactNode, useEffect, useRef } from "react";
import { createPortal } from "react-dom";

export default function DetailDialog({
  children,
  labelId,
  descriptionId,
  onClose,
  className = "",
  returnFocus,
}: {
  children: ReactNode;
  labelId: string;
  descriptionId?: string;
  onClose: () => void;
  className?: string;
  returnFocus?: Element | null;
}) {
  const dialogRef = useRef<HTMLElement>(null);
  const initialFocus = useRef(returnFocus ?? document.activeElement);
  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;
    const shell = document.querySelector<HTMLElement>(".app-shell");
    const previousInert = shell?.inert ?? false;
    const previousOverflow = document.body.style.overflow;
    if (shell) shell.inert = true;
    document.body.style.overflow = "hidden";
    const focusable = () =>
      [
        ...dialog.querySelectorAll<HTMLElement>(
          'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex="0"]',
        ),
      ].filter((element) => element.getClientRects().length > 0);
    const frame = requestAnimationFrame(() => (focusable()[0] ?? dialog).focus());
    const onKey = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        onClose();
      }
      if (event.key !== "Tab") return;
      const elements = focusable();
      const first = elements[0] ?? dialog;
      const last = elements[elements.length - 1] ?? dialog;
      if (
        event.shiftKey &&
        (document.activeElement === first || !dialog.contains(document.activeElement))
      ) {
        event.preventDefault();
        last.focus();
      } else if (
        !event.shiftKey &&
        (document.activeElement === last || !dialog.contains(document.activeElement))
      ) {
        event.preventDefault();
        first.focus();
      }
    };
    document.addEventListener("keydown", onKey);
    return () => {
      cancelAnimationFrame(frame);
      document.removeEventListener("keydown", onKey);
      document.body.style.overflow = previousOverflow;
      if (shell) shell.inert = previousInert;
      const target = initialFocus.current;
      if (
        (target instanceof HTMLElement || target instanceof SVGElement) &&
        target.isConnected &&
        "focus" in target &&
        typeof target.focus === "function"
      )
        target.focus({ preventScroll: true });
    };
  }, [onClose]);
  return createPortal(
    <div
      className="drawer-layer"
      onClick={(event) => {
        if (event.target === event.currentTarget) onClose();
      }}
    >
      <aside
        ref={dialogRef}
        className={`detail-drawer ${className}`}
        role="dialog"
        aria-modal="true"
        aria-labelledby={labelId}
        aria-describedby={descriptionId}
        tabIndex={-1}
      >
        {children}
      </aside>
    </div>,
    document.body,
  );
}
