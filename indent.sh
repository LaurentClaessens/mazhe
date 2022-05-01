#!/bin/bash

base_dir=$(pwd)
frido_dir=$base_dir/tex/frido

echo "You should not run this when the future references are not ok."
echo "Are you ok ? [y/n]"
read is_ok


if [ "$is_ok" == "y" ]; then
    echo "Ok.Making the indentation."
else
    echo "stop"
    exit 1
fi

cd $frido_dir
for f in $(ls *.tex); do echo $f ; latexindent -w  $f ;done

cd $base_dir
