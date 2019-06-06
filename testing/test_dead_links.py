#! /usr/bin/python3
# -*- coding: utf8 -*-
r""" Read all the .tex files in the current directory, and check *every* link.

- Every broken link (in \url or \href) is displayed.
- The directory passed as argument is the main directory of the mazhe project.
"""

import os,sys,string

from Output import args_to_output

output=args_to_output(sys.argv)

try:
    import requests

    # use default solution with
    def is_not_dead(url):
        try:
            ret = requests.head(url)
            return ret.status_code < 400
        except Exception as e:
            # print("Exception:", e)
            # For debug, could be used to distinguish 404 errors
            # and non-existing domains
            return False
# requests was not found, not an issue!
except ImportError:
    try:                 # assuming Python 3!
        from http.client import HTTPConnection
    except ImportError:  # using Python 2!
        from httplib import HTTPConnection
    try:                 # assuming Python 3!
        from urllib.parse import urlparse
    except ImportError:  # using Python 2!
        from urlparse import urlparse

    # use other function, with HTTPConnection and urlparse
    def is_not_dead(url):
        try:
            p = urlparse(url)
            conn = HTTPConnection(p.netloc)
            conn.request('HEAD', p.path)
            resp = conn.getresponse()
            return resp.status < 400
        except Exception as e:
            # print("Exception:", e)
            # For debug, could be used to distinguish 404 errors
            # and non-existing domains
            return False


starting_path = os.path.abspath(sys.argv[1])

mainbib = "mazhe.bib"


def exclude_dir(directory):
    # subdirectory 'build' is created by '<mazhe>/testing/testing.sh'
    if "build" in directory:
        return True
    if ".git" in directory :
        return True
    return False


def _tex_file_iterator(directory):
    for p in os.listdir(directory):
        path = os.path.join(directory, p)
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
    bib = os.path.join(directory, mainbib)
    if os.path.exists(bib) and os.path.isfile(bib):
        yield bib
    for p in _tex_file_iterator(directory):
        yield p

def _file_to_url_iterator(filename):
    """
    iterate over the url cited in 'filename'
    """
    pos = 0
    # FIXME possible encoding issue!
    with open(filename, 'r') as f:
        text = f.read()

    for line in text.split(r"\url{")[1:]:
        url = line[0 : line.find("}")]
        yield url
    for line in text.split(r"\href{")[1:]:
        url = line[0 : line.find("}")]
        yield url

    # La frime serait d'utiliser des vues de listes
    # pour éviter la copie.
    if filename.endswith(mainbib):
        for line in text.split("url =")[1:]:
            start = line.find('"')
            end = line.find('"', 2)
            url = line[start + 1 : end]
            if url is not "...":
                yield url

# List of broken links for which the author is already contacted,
# so we do not check these urls.
contacted_author = []
contacted_author.append("http://www.sebastien-pellerin.fr/zfiles/agreg/devanalyse.pdf")
contacted_author.append("http://www.sebastien-pellerin.fr/zfiles/agreg/devalgebre.pdf")
contacted_author.append("http://dynamaths.free.fr/docs/lecons/developpement_algebre_6.pdf")
contacted_author.append("http://www.ceremade.dauphine.fr/~mgubi/e1112/pd3.pdf")
contacted_author.append("http://www.rblld.fr/cours/chap8.pdf")
contacted_author.append("http://www.rblld.fr/cours/chap6.pdf")
contacted_author.append("http://www.iecn.u-nancy.fr/~kurtzman/cours/agreg/esperance-conditionnelle.pdf")
contacted_author.append("http://www.dms.umontreal.ca/~math1600/6Supplement/Normematricielle-1.pdf")
contacted_author.append("http://perso.eleves.bretagne.ens-cachan.fr/~pmonm570/fichiers/1-total.pdf")
contacted_author.append("http://li.perso.math.cnrs.fr/textes/Integration/change-v.pdf")


def is_serious_url(url):
    if url == r"\lstname":
        return False
    if url in contacted_author :
        return False
    return True


def file_to_url_iterator(filename):
    for url in _file_to_url_iterator(filename):
        if is_serious_url(url):
            yield url


def check_url_corectness(url,f):
    if url=="":
        output("There is an empty URL in ",f)
    if url[0] not in string.ascii_letters :
        output("In ",f," : the url does not starts with an ascii character :")
        output(url)


# Run script
if __name__ == '__main__':
    for f in tex_file_iterator(starting_path):
        for url in file_to_url_iterator(f):
            check_url_corectness(url,f)
            if not is_not_dead(url):
                # FIXME we should print the line also
                output("dead link in ", f, " :")
                output(url)
