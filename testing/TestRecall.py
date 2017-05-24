#! /usr/bin/python3
# -*- coding: utf8 -*-


# This script compares the files "*.pstricks" with the corresponding one 
# "*.pstricks.recall" and prints a warning if they are not equal.

# The directory passed as argument is the main directory of the
# mazhe project.
#
# So, relative to the passed argument 
# - '.pstricks' files to be checked are in `auto/pictures_tex`
# - '.recall' files to be checked against are in `src_phystricks`

import os

def pstricks_files_iterator(directory):
    for f in os.listdir(directory):
        if f.endswith(".pstricks"):
            yield os.path.join(directory,f)

def wrong_file_list(directory):
    """
    return a tuple of lists
    - the list of missing 'recall'
    - the list of 'recall/pstricks' which do not match
    """
    src_phystricks_dir=os.path.join(directory,"src_phystricks")
    auto_pictures_tex_dir=os.path.join(directory,"auto/pictures_tex")
    wfl=[]  # wrong file list
    mfl=[]  # missing file list
    print("src_phystricks_dir : ",src_phystricks_dir)
    for filename in pstricks_files_iterator(auto_pictures_tex_dir):
        with open(filename,'r') as f:
            get_text=f.read()
        try :
            recall_filename=os.path.join(src_phystricks_dir,
                                os.path.split(filename)[1]+".recall")
            with open(recall_filename,'r') as f:
                recall_text=f.read()
        except FileNotFoundError as err :
            mfl.append(filename)
            recall_text=get_text    # we do not append it to the wfl list.

        if get_text != recall_text :
            wfl.append(filename)
    return mfl,wfl
