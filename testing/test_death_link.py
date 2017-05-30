#! /usr/bin/python3
# -*- coding: utf8 -*-

# The directory passed as argument is the main directory of the
# mazhe project.


import os
import sys

starting_path=os.path.abspath(sys.argv[1])

def exclude_dir(directory):
    if "build" in directory:
        return True
    if ".git" in directory :
        return True
    return False

def _tex_file_iterator(directory):
    for p in os.listdir(directory):
        path=os.path.join(directory,p)
        if os.path.isfile(path):
            if path.endswith(".tex"):
                yield path
        if os.path.isdir(path) and not exclude_dir(path):
            for f in _tex_file_iterator(path):
                yield f

def tex_file_iterator(directory):
    """
    Provides 'mazhe.bib' and then the '.tex' files in the
    directory (recursive).
    """
    yield os.path.join(directory,"mazhe.bib")
    for p in _tex_file_iterator(directory):
        yield p

def file_to_url_iterator(filename):
    """
    iterate over the url cited in 'filename'
    """
    pos=0
    with open(filename,'r') as f:
        text=f.read()

    for line in text.split("\\url{")[1:]:
        url=line[0:line.find("}")]
        print(url)

# Tel quel, il ne liste pas mazhe.bib
for f in tex_file_iterator(starting_path):
    file_to_url_iterator(f)
