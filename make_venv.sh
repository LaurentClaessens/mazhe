#!/bin/bash

set -u

# git clone https://github.com/pyenv/pyenv.git
# cd .pyenv/bin
# ./pyenv install 3.10.4

MAIN_DIR=$(pwd)
VENV_DIR="$MAIN_DIR/venv"
BIN_DIR="$VENV_DIR/bin"
PYTHON_VERSION=3.10.4   # version 3.10 hard-coded in yann_dirmanage.py
pak_dir=$VENV_DIR/lib/python3.10/site-packages

PYTHON3="$HOME/.pyenv/versions/$PYTHON_VERSION/bin/python3"

echo "le python3 sera $PYTHON3"


function install_pytex()
{
    echo "bonjour"
    pytex_dir=$pak_dir/pytex
    if [ ! -d "$pytex_dir" ]; then
      echo "$pytex_dir does not exist."
      cd $pak_dir
      git clone git@github.com:LaurentClaessens/pytex.git
    fi
    if [[ -d "$pytex_dir" ]]
    then
      echo "$pytex_dir exists on your filesystem."
      cd $pytex_dir
      git pull 
    fi
}

function install_custom()
{
    pak_name=$1
    github_url=$2
    echo "bonjour"
    site_dir=$VENV_DIR/lib/python3.10/site-packages
    pak_dir=$site_dir/$pak_name
    if [ ! -d "$pak_dir" ]; then
      echo "$pak_dir does not exist."
      cd $site_dir
      git clone $github_url
    fi
    if [[ -d "$pak_dir" ]]
    then
      echo "$pak_dir exists on your filesystem."
      cd $pak_dir
      git pull 
    fi
}

function install_sage()
{
  # Assume that sage is installed on your system.
  ln -s /usr/lib/python3/dist-packages/sage $pak_dir
}


echo "Creating the virtual environment"
"$PYTHON3" -m venv "$VENV_DIR"


cd "$BIN_DIR" || exit 1
./pip3 install --upgrade pip

cd "$BIN_DIR" || exit 1
./pip3 install -r "$MAIN_DIR/requirements.txt"


install_custom pytex clone git@github.com:LaurentClaessens/pytex.git
install_custom yanntricks https://github.com/LaurentClaessens/yanntricks
install_sage
