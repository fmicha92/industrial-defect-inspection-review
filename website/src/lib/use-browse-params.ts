import { useCallback } from "react";
import { useSearchParams } from "react-router-dom";

export function useBrowseParams() {
  const [params, setParams] = useSearchParams();
  const update = useCallback(
    (fields: Record<string, string | null>, replace = true) => {
      setParams(
        (current) => {
          const next = new URLSearchParams(current);
          Object.entries(fields).forEach(([key, value]) => {
            if (value === null || value === "" || value === "all") next.delete(key);
            else next.set(key, value);
          });
          return next;
        },
        { replace },
      );
    },
    [setParams],
  );
  return { params, update };
}
