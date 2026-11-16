from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
READMES = (ROOT / "README.md", ROOT / "README.en.md")
REQUIRED_ASSETS = ("assets/brand/banner.svg", "assets/brand/logo.svg")
LOCAL_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
IMAGE_LINK = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
SVG_DIR = ROOT / "assets" / "brand"


def local_target(raw: str) -> Path | None:
    raw = raw.strip()
    if not raw or raw.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw):
        return None
    target = unquote(raw.split("#", 1)[0].split("?", 1)[0])
    return (ROOT / target).resolve() if target else None


def validate_readme(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"Missing required document: {path.relative_to(ROOT)}")
        return
    content = path.read_text(encoding="utf-8")
    for asset in REQUIRED_ASSETS:
        if asset not in content:
            errors.append(f"{path.name} does not reference {asset}")
    links = LOCAL_LINK.findall(content) + IMAGE_LINK.findall(content)
    for raw in links:
        target = local_target(raw)
        if target is None:
            continue
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.name}: reference escapes repository: {raw}")
            continue
        if not target.exists():
            errors.append(f"{path.name}: missing local reference: {raw}")


def validate_svg(path: Path, errors: list[str]) -> None:
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid SVG/XML: {exc}")
        return
    if root.tag.rsplit("}", 1)[-1] != "svg":
        errors.append(f"{path.relative_to(ROOT)}: root element is not SVG")
    if not root.attrib.get("viewBox"):
        errors.append(f"{path.relative_to(ROOT)}: missing viewBox")
    names = {node.tag.rsplit("}", 1)[-1] for node in root.iter()}
    if "title" not in names:
        errors.append(f"{path.relative_to(ROOT)}: missing accessible title")


def main() -> int:
    errors: list[str] = []
    for readme in READMES:
        validate_readme(readme, errors)
    if not SVG_DIR.is_dir():
        errors.append("Missing assets/brand/ directory")
        svg_files: list[Path] = []
    else:
        svg_files = sorted(SVG_DIR.glob("*.svg"))
    if not svg_files:
        errors.append("No SVG files found in assets/brand/")
    for svg in svg_files:
        validate_svg(svg, errors)
    if errors:
        print("Profile validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Profile validation passed: {len(READMES)} READMEs, {len(svg_files)} SVG assets, all local references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
