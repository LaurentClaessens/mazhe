#!/bin/bash

base_dir=$(pwd)
frido_dir=$base_dir/tex/frido

cd $frido_dir
for f in $(ls *.tex); do echo $f ; latexindent -w  $f ;done


cd $base_dir
