#!/usr/bin/env python3
"""Buat ulang README galeri tiap paket, manifest.json, dan daftar paket di README utama.

Jalankan dari root repo setiap kali menambah paket baru:
    python scripts/build_index.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICONS = ROOT / "icons"
FOOTAGE = ROOT / "footage"
VIDEO_EXT = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}
COLS = 6
START = "<!-- PACKS:START -->"
END = "<!-- PACKS:END -->"


def title_of(name: str) -> str:
    return re.sub(r"^pack-\d+-", "", name).replace("-", " ").title()


def icon_gallery(pack: Path) -> int:
    icons = sorted(p for p in pack.iterdir() if p.suffix.lower() in {".svg", ".png"})
    rows = []
    for i in range(0, len(icons), COLS):
        cells = "".join(
            f'<td align="center" width="120"><img src="{p.name}" width="56" height="56" alt="{p.stem}"><br><sub>{p.stem}</sub></td>'
            for p in icons[i : i + COLS]
        )
        rows.append(f"<tr>{cells}</tr>")
    meta_file = pack / "pack.json"
    meta = json.loads(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
    desc = meta.get("description", "")
    (pack / "README.md").write_text(
        f"# {meta.get('title', title_of(pack.name))}\n\n{desc}\n\n"
        f"**{len(icons)} icon** · format {', '.join(sorted({p.suffix[1:].upper() for p in icons}))}"
        f"{' · ' + meta['size'] if meta.get('size') else ''}\n\n"
        f"[← Kembali ke semua paket](../../README.md)\n\n<table>\n" + "\n".join(rows) + "\n</table>\n",
        encoding="utf-8",
    )
    return len(icons)


def main() -> None:
    manifest: dict[str, list[dict[str, object]]] = {"icons": [], "footage": []}
    lines = ["### Icon", "", "| Paket | Jumlah | Galeri |", "|---|---|---|"]
    for pack in sorted(p for p in ICONS.iterdir() if p.is_dir()):
        n = icon_gallery(pack)
        files = sorted(p.name for p in pack.iterdir() if p.suffix.lower() in {".svg", ".png"})
        manifest["icons"].append({"pack": pack.name, "count": n, "files": files})
        lines.append(f"| {title_of(pack.name)} | {n} | [lihat](icons/{pack.name}/README.md) |")

    lines += ["", "### Footage", ""]
    packs = sorted(p for p in FOOTAGE.iterdir() if p.is_dir()) if FOOTAGE.exists() else []
    if not packs:
        lines.append("Belum ada. Lihat [footage/README.md](footage/README.md) untuk cara menambah.")
    else:
        lines += ["| Paket | Jumlah | Folder |", "|---|---|---|"]
        for pack in packs:
            vids = sorted(p.name for p in pack.rglob("*") if p.suffix.lower() in VIDEO_EXT)
            manifest["footage"].append({"pack": pack.name, "count": len(vids), "files": vids})
            lines.append(f"| {title_of(pack.name)} | {len(vids)} | [buka](footage/{pack.name}) |")

    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    block = START + "\n" + "\n".join(lines) + "\n" + END
    readme.write_text(re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S), encoding="utf-8")
    print(f"OK: {len(manifest['icons'])} paket icon, {len(manifest['footage'])} paket footage")


if __name__ == "__main__":
    main()
