#!/usr/bin/python3

"""
This is a single-usage script.

History:
    Up to October 11, 2019 each theme was in its own file (`xx_theme.tex`). The issue is that Vim did not detect correctly the fact that spell checker has to be activated. More or less because there are no '\section' at the top.
    Thus I put the whole in the same file.
"""

from pathlib import Path

theme_list = [ "21_theme", "23_theme", "76_theme", "60_theme", "3_theme", "24_theme", "14_theme", "61_theme", "52_theme", "15_theme", "42_theme", "66_theme", "1_theme", "2_theme", "73_theme", "65_theme", "4_theme", "27_theme", "46_theme", "50_theme", "53_theme", "16_theme", "59_theme", "11_theme", "56_theme", "40_theme", "43_theme", "63_theme", "64_theme", "69_theme", "74_theme", "44_theme", "45_theme", "47_theme", "48_theme", "49_theme", "5_theme", "39_theme", "77_theme", "51_theme", "17_theme", "67_theme", "13_theme", "12_theme", "38_theme", "35_theme", "30_theme", "9_theme", "68_theme", "75_theme", "28_theme", "19_theme", "29_theme", "32_theme", "33_theme", "62_theme", "71_theme", "20_theme", "70_theme", "34_theme", "36_theme", "7_theme", "37_theme", "31_theme", "57_theme", "54_theme", "55_theme", "58_theme", "41_theme", "6_theme", "10_theme", "72_theme"]

base_dir = Path('.').resolve() / ".." / ".."
print("base_dir", base_dir)
theme_dir = base_dir.resolve() / "tex" / "front_back_matter"
print("theme_dir", theme_dir)

def name_to_path(name):
    """Return the path of a 'theme' file from its name."""
    return theme_dir / f"{name}.tex"


for name in theme_list:
    filename = name_to_path(name)
    theme_text = open(filename, 'r').read()
    print(theme_text)


