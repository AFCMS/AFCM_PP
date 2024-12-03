# SPDX-FileCopyrightText: 2024 AFCMS <afcm.contact@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import pathlib
import subprocess

"""
Export Inkscape SVG files to raw SVG and PNG in multiple resolutions
"""

# INKSCAPE_COMMAND: list[str] = ["inkscape"]
INKSCAPE_COMMAND = ["flatpak", "run", "org.inkscape.Inkscape"]

RESOLUTIONS: set[int] = {64, 128, 256, 512, 1024, 2048}


def export_simple_svg(src_path: pathlib.Path, out_path: pathlib.Path):
    print("Exporting:", out_path.name)

    if not src_path.exists():
        print(f"File {src_path.name} do not exist!")
        exit(1)

    subprocess.run(
        INKSCAPE_COMMAND + ["-o", str(out_path), "--export-plain-svg", str(src_path)]
    )


def export_simple_png(src_path: pathlib.Path, out_path: pathlib.Path, size: int):
    print("Exporting:", out_path.name)

    if not src_path.exists():
        print(f"File {src_path.name} do not exist!")
        exit(1)

    subprocess.run(
        INKSCAPE_COMMAND
        + [
            "-o",
            str(out_path),
            f"--export-width={size}",
            f"--export-height={size}",
            str(src_path),
        ]
    )


for t in {"round", "square"}:
    for c in {"alpha", "white"}:
        source_path = pathlib.Path(f"./src/AFCM_source_{t}_{c}.svg")
        out_path_svg = pathlib.Path(f"./svg/AFCM_{t}_{c}.svg")

        export_simple_svg(source_path, out_path_svg)

        for s in RESOLUTIONS:
            out_path = pathlib.Path(f"./png/AFCM_{t}_{c}_x{s}.png")

            export_simple_png(source_path, out_path, s)

for c in {"alpha", "white"}:
    source_path = pathlib.Path(f"./src/AFCM_source_square_{c}_no_border.svg")
    out_path_svg = pathlib.Path(f"./svg/AFCM_square_{c}_no_border.svg")

    export_simple_svg(source_path, out_path_svg)

    for s in RESOLUTIONS:
        out_path = pathlib.Path(f"./png/AFCM_square_{c}_no_border_x{s}.png")

        export_simple_png(source_path, out_path, s)


for f in pathlib.Path("./png").glob("*.png"):
    subprocess.run(["oxipng", "--opt", "max", "--strip", "all", "--zopfli", str(f)])
