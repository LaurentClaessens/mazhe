#! /usr/bin/python3
# -*- coding: utf8 -*-

"""
Vous frappez à la porte d'une famille qui a deux enfants. Une fille ouvre la porte et vous dit "Je suis l'aînée".
Quelle est la probabilité que l'autre soit une fille ?
"""


import random

def famille():
    """
    return a pair of 'f' and 'g'.
    """
    a=[random.choice( ['g','f'] )]
    a.append(random.choice( ['g','f'] ))
    return a

def toctoc():
    """
    - Create a family with two children. 
    - Pick the second one, the elder.
    - if it is a 'g', return None.
    - if it is a 'f', return the other one.
    """
    F=famille()
    if F[1] != 'f':
        return None
    else :
        if F[0]=='f':
            return 1
        else :
            return 0

N_girl_opens=0
N_girl_other=0
for k in range(1,10000):
    res=toctoc()
    if res is not None:
        N_girl_opens = N_girl_opens+1
        N_girl_other = N_girl_other + res

proba=N_girl_other/N_girl_opens
print(proba)        # ~0.5, intuitively correct.
