#! /usr/bin/env python3
# -*- coding: utf8 -*-


x,y=var("x,y")

C=[]
C.append(x)
C.append(y)

def coef4(h):
    S=0
    for i in [0,1]:
        for j in [0,1]:
            for k in [0,1]:
                for l in [0,1]:
                    S=S+h[i]*h[j]*h[k]*h[l]*C[i]*C[j]*C[k]*C[l]
    return S

def coef2(h):
    S=0
    for i in [0,1]:
        for j in [0,1]:
            S=S+h[i]*h[j]*C[i]*C[j]
    return S

cross=[]
square=[]

cross.append(  [1,0] )
cross.append(  [-1,0] )
cross.append(  [0,1] )
cross.append(  [0,-1] )

square=[]
square.append(  [-1,-1] )
square.append(  [1,-1] )
square.append(  [-1,1] )
square.append(  [1,1] )


print("Cross scheme :")

K=sum(  coef2(v) for v in cross   )
L=sum(  coef4(v) for v in cross   )
print(K)
print(L)

print("square scheme :")

K=sum(  coef2(v) for v in square   )
L=sum(  coef4(v) for v in square   )
print(K)
print(L)
