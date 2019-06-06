# -*- coding: utf8 -*-

"""
This file contains some utilities for debugging.
"""

def dprint(*args):
    """
    Same as "print", but easier to search/remove when I do not
    need anymore.
    """
    print(" ".join(args))

