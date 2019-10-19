#!/bin/bash

# These tests are supposed to be launched in a cloned directory.


PWD=`pwd`

MAIN_TEX=$PWD/..
AUTO_PICTURES_TEX=$MAIN_TEX/auto/pictures_tex
AUTO_PICTURES_TIKZ=$MAIN_TEX/auto/pictures_tikz
SRC_PHYSTRICKS=$PWD

compile_pass ()
{
    cd $SRC_PHYSTRICKS
    ./figures_giulietta.py --all --pass-number=$1 &&
    cd $MAIN_TEX
    pytex lst_giulietta.py --no-external
}

# Remove the garbage files

cd $SRC_PHYSTRICKS
rm *.pyc >> /dev/null

cd $AUTO_PICTURES_TEX
rm *.pstricks
rm *.md5 >> /dev/null
rm *.pdf >> /dev/null
rm *.aux >> /dev/null

# Compile three times the demo pictures
# (yes, some pictures need three passes)

cd $SRC_PHYSTRICKS
compile_pass 1 &&
compile_pass 2 &&
compile_pass 3
