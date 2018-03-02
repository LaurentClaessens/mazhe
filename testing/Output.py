# -*- coding: utf8 -*-

"""
A small mechanism which creates the function 'output'.

- output("foo") prints 'foo' on the screen and in a given file

The point is to use `output` instead of `print` for the lines which have to
be displayed as summary.
"""

import os,sys

class SummaryOutput(object):
    """
    This class serves to replace `print` for the summary messages
    """
    def __init__(self,out):
        self.out=out
    def __call__(self,*args):
        text=""
        for a in args:
            text=text+str(a)+" "
        self.out.write(text+"\n")

class FileOutput(object):
    """
    A `FileOutput` object is intended to be given as `out` in
    `SummaryOutput`. Thus here the write` function always gets
    a single `str` argument, since the work of conversion from `*args` is
    done in `SummaryOutput.__call__`

    Creating an object does not empties the log file. The reasons is that
    one round of testing a document asks for several launch of `pytex`. Only
    the output of the last one would be available in the log file.

    However, here we check that the file exists; if not we create it.
    """
    def __init__(self,filename):
        self.filename=filename
        if not os.path.isfile(self.filename):
            with open(self.filename,'w') as f:
                f.write("Here is the log file")
    def write(self,text):
        sys.stdout.write(text)
        with open(self.filename,'a') as f:
            f.write(text)

def args_to_output(args):
    """
    If one of the args is of the form
    'output=<filename>'
    creates an output that prints on the screen and in the file.

    If no "--output" is found, returns the usual 'print' function.
    """
    for arg in args :
        if arg.startswith("--output="):
            filename=arg.split("=")[1]
            return SummaryOutput(FileOutput(filename))
    return print
