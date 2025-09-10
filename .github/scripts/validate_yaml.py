import sys
from pathlib import Path

import yaml

FILES = [
    ".github/workflows/ci.yml",
    ".github/workflows/security-scan.yml",
    ".github/dependabot.yml",
]


def main() -> None:
    for f in FILES:
        print("\n--", f)
        try:
            text = Path(f).read_text(encoding="utf-8")
            s = text.strip()
            if s.startswith("```"):
                lines = text.splitlines()
                if lines and lines[0].startswith("```"):
                    lines = lines[1:]
                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]
                text = "\n".join(lines)
            yaml.safe_load(text)
            print("OK")
        except Exception as exc:  # pragma: no cover - simple runner
            print("ERROR:", exc)
            sys.exit(1)

    print("\nAll files parsed (or first error reported).")


if __name__ == "__main__":
    main()
