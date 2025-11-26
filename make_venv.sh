#!/bin/bash

set -ue

# sudo apt install  build-essential zlib1g-dev libffi-dev libssl-dev libreadline-dev libsqlite3-dev liblzma-dev libbz2-dev

MAIN_DIR=$(pwd)
VENV_DIR="$MAIN_DIR/venv"
BIN_DIR="$VENV_DIR/bin"
PYTHON_VERSION=3.10.12

# Adapter à votre situation.
pyenv_dir=$MAIN_DIR/pyenv
PYTHON3="$pyenv_dir/versions/$PYTHON_VERSION/bin/python3"
PYENV_ROOT=$pyenv_dir

function clone_pyenv()
{
  if [ ! -d "$pyenv_dir" ]; then
    git clone https://github.com/pyenv/pyenv.git $pyenv_dir
  fi
}

function compile_python()
{
  echo $PYENV_ROOT
  cd pyenv/bin
  PYENV_ROOT=$pyenv_dir ./pyenv install -s -v 3.10.12
}

function install_pytex()
{
    pytex_dir=$MAIN_DIR/pytex
    if [ ! -d "$pytex_dir" ]; then
      git clone git@github.com:LaurentClaessens/pytex.git $pytex_dir
    fi
    cd $pytex_dir
    git pull 
}

function create_venv()
{
  echo "Creating the virtual environment"
  "$PYTHON3" -m venv "$VENV_DIR"
  cd "$BIN_DIR" || exit 1
  ./pip3 install --upgrade pip
}


function pip_requirements()
{
  cd "$BIN_DIR" || exit 1
  ./pip3 install -r "$MAIN_DIR/requirements.txt"
}


clone_pyenv
compile_python
install_pytex
create_venv
pip_requirements
