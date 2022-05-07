#!/bin/bash

base_dir=$(readlink -f $PWD/..)
frido_dir=$base_dir/tex/frido
front_back_dir=$base_dir/tex/front_back_matter

echo "You should not run this when the future references are not ok."
echo "Are you ok ? [y/n]"
read is_ok


if [ "$is_ok" == "y" ]; then
    echo "Ok.Making the indentation."
else
    echo "stop"
    exit 1
fi


function make_dir()
{
    target=$1
    cd $target
    # for f in $(ls $target/*.tex); do echo $f ; latexindent -w  $f ;done
    for f in $(ls $target/*.tex); do echo $f ;done
}


make_dir $frido_dir
make_dir $front_back_dir
