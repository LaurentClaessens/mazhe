#!/bin/bash


# You may have to hack

#
# git clone https://github.com/pyenv/pyenv.git
# cd .pyenv/bin
# ./pyenv install 3.10.4

MAIN_DIR=$(pwd)
VENV_DIR="$MAIN_DIR/venv"
BIN_DIR="$VENV_DIR/bin"
PYTHON_VERSION=3.10.4

PYTHON3="$HOME/.pyenv/versions/$PYTHON_VERSION/bin/python3"

echo "le python3 sera $PYTHON3"


function install_pytex()
{
    echo "bonjour"
    pak_dir=$VENV_DIR/lib/python3.10/site-packages
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

echo "Creating the virtual environment"
"$PYTHON3" -m venv "$VENV_DIR"


cd "$BIN_DIR" || exit 1
./pip3 install --upgrade pip

cd "$BIN_DIR" || exit 1
./pip3 install -r "$MAIN_DIR/requirements.txt"


install_pytex
