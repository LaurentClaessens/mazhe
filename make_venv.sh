#!/bin/bash

#
# This script installs the required venv for the linter.
#

# apt install  make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git


# git clone https://github.com/pyenv/pyenv.git ~/.pyenv
# cd ~/.pyenv/libexec
# ./pyenv install 3.7.4

# You may have to hack
# cd /usr/lib/x86_64-linux-gnu
# sudo ln -s libffi.so.7 libffi.so.6

VERSION=3.8.3
PYTHON3=~/.pyenv/versions/$VERSION/bin/python3
MAIN_DIR=$PWD
VENV_DIR=$MAIN_DIR/venv
BIN_DIR=$VENV_DIR/bin


pip3_install()
{
    PACKAGE=$1
    cd $BIN_DIR
    ./pip3 install $PACKAGE
}

upgrade_pip()
{
    cd $BIN_DIR
    ./pip3 install --upgrade pip
}

install_venv()
{
    echo $PYTHON3
    echo $VENV_DIR
    $PYTHON3 -m venv $VENV_DIR
}

install_pip_packages()
{
    # pass
    echo "rien à installer ?"
}

install_venv
upgrade_pip
install_pip_packages
