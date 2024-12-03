# AFCM Profile Picture Source

![Linter](https://github.com/AFCMS/AFCM_PP/workflows/Linting/badge.svg)

Images: All rights reserved

Code: GPLv3

## Workflow

You need the [Hack Nerd Font](https://github.com/ryanoasis/nerd-fonts) font installed for the profile picture to render properly.

To modify the profile picture, you need to edit the files in `./src` using Inkscape.

Then you can regenerate all the simple SVG and PNG files just by using `python3 ./export.py` (you need to have the inkscape executable or a Flatpak installation, it's not auto detected).

You also need to have the `oxipng` executable in your PATH to optimize the PNG files.

`oxipng` is configured to use the Zopfli compressor which is very slow on large files like the max resolutions.
