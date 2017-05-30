#! /usr/bin/python3
# -*- coding: utf8 -*-

# The directory passed as argument is the main directory of the
# mazhe project.


import os
import sys
import string

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

def _file_to_url_iterator(filename):
    """
    iterate over the url cited in 'filename'
    """
    pos=0
    with open(filename,'r') as f:
        text=f.read()

    for line in text.split("\\url{")[1:]:
        url=line[0:line.find("}")]
        yield url
    for line in text.split("\\href{")[1:]:
        url=line[0:line.find("}")]
        yield url

    # La frime serait d'utiliser des vues de listes
    # pour éviter la copie.
    if filename.endswith("mazhe.bib"):
        for line in text.split("url =")[1:]:
            start=line.find('"')
            end=line.find('"',2)
            url=line[start+1:end]
            if url is not "...":
                yield url

def file_to_url_iterator(filename):
    for url in _file_to_url_iterator(filename):
        if url != r"\lstname":
            yield url

            

def check_url_corectness(url,f):
    if url=="":
        print("There is an empty URL in ",f)
    if url[0] not in string.ascii_letters :
        print("In ",f," : the url does not starts with an ascii character :")
        print(url)


for f in tex_file_iterator(starting_path):
    for url in file_to_url_iterator(f):
        check_url_corectness(url,f)
