#! /usr/bin/python3
# -*- coding: utf8 -*-

import random

def famille():
    """
    return a pair of 'f' and 'g'
    """
    a=[random.choice( ['g','f'] )]
    a.append(random.choice( ['g','f'] ))
    return a

def toctoc():
    F=famille()
    s=random.choice([0,1])
    if F[s] != 'f':
        #print("ce n'est pas une fille qui ouvre")
        return None
    else : 
        t=(s+1)%2
        #print("L'autre sera ",t,"c'est à dire",F[t])
        if F[t]=='f':
            return 1
        else :
            return 0

N_girl_opens=0
N_girl_other=0
for k in range(1,10000):
    print('----------')
    res=toctoc()
    if res is not None:
        N_girl_opens = N_girl_opens+1
        N_girl_other = N_girl_other + res
        print(res,N_girl_opens,N_girl_other)

proba=N_girl_other/N_girl_opens
print(proba)
