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

def tex_file_iterator(directory):
    for p in os.listdir(directory):
        path=os.path.join(directory,p)
        if os.path.isfile(path):
            if path.endswith(".tex"):
                yield path
        if os.path.isdir(path) and not exclude_dir(path):
            for f in tex_file_iterator(path):
                yield f


print(starting_path)

for f in tex_file_iterator(starting_path):
    print(f)
