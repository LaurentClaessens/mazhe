#!/bin/bash
# -*- coding: utf8 -*-

# These tests are supposed to be launched in a cloned directory.


PWD=`pwd`

echo $PWD

MAIN_TEX=$PWD/..
AUTO_PICTURES_TEX=$MAIN_TEX/auto/pictures_tex
AUTO_PICTURES_TIKZ=$MAIN_TEX/auto/pictures_tikz
PICTURES_SRC=$PWD

compile_pass ()
{
    cd $PICTURES_SRC
    ./figures_mazhe.py --all --pass-number=$1 &&
    cd $MAIN_TEX
    pytex lst_everything.py --no-external 
}

# Remove the garbage files

cd $PICTURES_SRC
rm *.pyc >> /dev/null

cd $AUTO_PICTURES_TEX
rm *.pstricks 


rm *.md5 >> /dev/null
rm *.pdf >> /dev/null

rm *.pstricks >> /dev/null
rm *.aux >> /dev/null

# Compile three times the demo pictures 
# (yes, some pictures need three passes)

cd $PICTURES_SRC
compile_pass 1 &&
compile_pass 2 &&
compile_pass 3 
