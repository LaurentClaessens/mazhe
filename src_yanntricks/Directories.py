
# MAIN_TEX
#   is the directory of the main latex file.

# PICTURES_TEX
#   is the directory in which the latex code of the picture will be written (that is the files `*.pstricks`).

# PICTURES_SRC
#   is the directory containing the source of the figures (typically yanntricks*.py). This sould be "." because why should you put these somewhere else ?

# PICTURES_TIKZ
#   is the directory in which one store the intermediate tikz files *.md5 and *.pdf

# Directories are given relative to the one where the source pictures are.

# Attention : these directories are hard-coded in src_yanntricks/testing.sh

from pathlib import Path

HERE = Path('.')

PICTURES_SRC = HERE
SAGE_DIR = HERE
MAIN_TEX = HERE / ".."
AUTO = MAIN_TEX / "auto"
MAIN_TEX = MAIN_TEX.resolve()
PICTURES_TIKZ = AUTO / "pictures_tikz"
PICTURES_TEX = AUTO / "pictures_tex"
