#! /usr/bin/python3
# -*- coding: utf8 -*-

"""
Vous savez qu'une famille a deux enfants.
Vous demandez à un parent si il y a une fille.
Réponse : Oui.
Question : quelle est la probabilité que ce soient deux filles ?
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
    - If 'gg', there are no girls -> return None
    - If 'gf', there is a girl but the other is a boy -> 0
    - If 'fg', there is a girl but the other is a boy -> 0
    - If 'ff', there is a girl and the other is a girl -> 1
    """
    F=famille()
    if F==['g','g'] :
        return None
    if F==['g','f']:
        return 0
    if F==['f','g']:
        return 0
    if F==['f','f']:
        return 1

N_at_least_one_girl=0
N_two_girls=0
for k in range(1,10000):
    res=toctoc()
    if res is not None:
        N_at_least_one_girl=N_at_least_one_girl+1
        N_two_girls=N_two_girls+res

proba=N_two_girls/N_at_least_one_girl
print(proba)        # ~0.333. Beware !
