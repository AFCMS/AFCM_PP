import pathlib
import subprocess

"""
Author: AFCM
License: GPLv3

Export Inkscape SVG files to raw SVG and PNG in multiple resolutions
"""

for t in {"round", "square"}:
	for c in {"alpha", "white"}:
		source_path = pathlib.Path(f"./src/AFCM_source_{t}_{c}.svg")

		if not source_path.exists():
			print(f"File ./src/AFCM_source_{t}_{c}.svg do not exist!")
			exit(1)

		out_path = pathlib.Path(f"./svg/AFCM_{t}_{c}.svg")

		print("Exporting:", out_path.name)
		subprocess.run(["inkscape", "-o", out_path, "--export-plain-svg", source_path])
		print("\n")


for t in {"round", "square"}:
	for c in {"alpha", "white"}:
		source_path = pathlib.Path(f"./svg/AFCM_{t}_{c}.svg")

		for s in {256, 512, 1024, 2048}:
			out_path = pathlib.Path(f"./png/AFCM_{t}_{c}_x{s}.png")

			print("Exporting:", out_path.name)
			subprocess.run(["inkscape", "-o", out_path, f"--export-width={s}", f"--export-height={s}", source_path])
			print("\n")
