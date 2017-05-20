#! /usr/bin/python3
# -*- coding: utf8 -*-


# This script compares the files "*.pstricks" with the corresponding one 
# "*.pstricks.recall" and prints a warning if they are not equal.

import os

def pstricks_files_iterator():
    for f in os.listdir():
        if f.endswith(".pstricks"):
            yield f

for filename in pstricks_files_iterator():
    with open(filename,'r') as f:
        get_text=f.read()

    try :
        with open(filename+".recall",'r') as f:
            recall_text=f.read()
    except FileNotFoundError as err :
        print(err)
        print("See 'phystricks/testing/README.md' to know how to use 'test_recall.py'")
        raise

    if get_text != recall_text :
        print("Wrong : "+filename)


