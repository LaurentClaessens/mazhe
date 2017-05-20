#!/bin/bash
# -*- coding: utf8 -*-


PWD=`pwd`

echo $PWD

exit

MAIN_TEX=$PWD/..
PICTURES_TEX=$MAIN_TEX/auto/pictures_tex
PICTURES_SRC=$PWD
PICTURES_TIKZ=$MAIN_TEX/auto/pictures_tikz

compile_pass ()
{
cd $PICTURES_SRC
./figures_mazhe.py --all --pass-number=$1 &&
cd $MAIN_TEX
pytex lst_everything.py --no-external --all 
}

# Remove the garbage files

cd $PICTURES_SRC
rm *.pyc >> /dev/null

cd $PICTURES_TEX
rm *.comment >> /dev/null

cd $PICTURES_TIKZ
rm *.dpth >> /dev/null
rm *.log >> /dev/null
rm *.maf >> /dev/null
rm *.mtc >> /dev/null
rm *.mtc0 >> /dev/null
rm *.nlo >> /dev/null

rm *.md5 >> /dev/null
rm *.pdf >> /dev/null

rm *.pstricks >> /dev/null
rm *.aux >> /dev/null

# Compile three times the demo pictures 
# (yes, some pictures need three passes)

cd $PICTURES_SRC
compile_demo 1 &&
compile_demo 2 &&
compile_demo 3 

# Then compare with the "recall" ones

cd $PICTURES_SRC

./test_recall.py

