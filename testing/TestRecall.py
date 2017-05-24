#! /usr/bin/python3
# -*- coding: utf8 -*-


# This script compares the files "*.pstricks" with the corresponding one 
# "*.pstricks.recall" and prints a warning if they are not equal.

# It is supposed to be launched from 'testing.sh' and 
# assumes many stuff on the directory structure.

import os
import sys

directory=sys.argv[1]

def pstricks_files_iterator(directory):
    os.chdir(directory)
    for f in os.listdir():
        if f.endswith(".pstricks"):
            yield f

def wrong_file_list(directory):
    wfl=[]
    for filename in pstricks_files_iterator(directory):
        with open(filename,'r') as f:
            get_text=f.read()
        try :
            with open(filename+".recall",'r') as f:
                recall_text=f.read()
        except FileNotFoundError as err :
            print("No recall file for ",filename)
            print("See 'phystricks/testing/README.md' to know how to use 'test_recall.py'")
            recall_text=""

        if get_text != recall_text :
            wfl.append(filename)
