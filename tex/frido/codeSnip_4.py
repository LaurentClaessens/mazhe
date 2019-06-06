#!/usr/bin/python3

def rec(A,x):
    return ((x**2+A)/x)/2

A = 3       # Compute square root of 3
x = 1000    # Initial guess: 1000

for i in range(1,100):
    print(i, x, x**2, x**2-A)
    x = rec(A, x)
