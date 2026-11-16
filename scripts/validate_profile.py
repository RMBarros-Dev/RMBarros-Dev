from __future__ import annotations

from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
REQUIRED_REFERENCES = (
    "assets/brand/banner.svg",
    "assets/brand/logo.svg",
)


def main() -> int:
    errors: list[str] = []
    readme = README.read_text(encoding="utf-8")

    for reference in REQUIRED_REFERENCES:
        if reference not in readme:
            errors.append(f"README.md does not reference {reference}")
        elif not (ROOT / reference).is_file():
            errors.append(f"Referenced file does not exist: {reference}")

    svg_files = sorted((ROOT / "assets" / "brand").glob("*.svg"))
    if not svg_files:
        errors.append("No SVG files found in assets/brand/")

    for svg_path in svg_files:
        try:
            tree = ET.parse(svg_path)
            root = tree.getroot()
            if not root.tag.endswith("svg"):
                errors.append(f"{svg_path.relative_to(ROOT)}: root element is not SVG")
                continue
            if not root.attrib.get("viewBox"):
                errors.append(f"{svg_path.relative_to(ROOT)}: missing viewBox")
            local_names = {element.tag.rsplit("}", 1)[-1] for element in root.iter()}
            if "title" not in local_names:
                errors.append(f"{svg_path.relative_to(ROOT)}: missing accessible title")
        except ET.ParseError as exc:
            errors.append(f"{svg_path.relative_to(ROOT)}: invalid XML: {exc}")

    if errors:
        print("Profile validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Profile validation passed: {len(svg_files)} SVG files and all local README references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
