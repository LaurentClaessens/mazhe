#!/usr/bin/python3

import math


def fun(x:float)->float:
    return 2*x**2-4*x+2-math.exp(-x)


def one_step(a:float, b:float)->tuple[float, float]:
    """
    One step of bissection.

    a: minial value of the root
    b: max value of the root

    return a new min and max for the interval in which the root lies.
    """
    f_a = fun(a)
    f_b = fun(b)
    check = f_a * f_b
    if check > 0:
        raise ValueError("la fonction doit avoir des signes opposés")
    middle = (a+b)/2
    value = fun(middle)

    # Pour bien faire, il faudrait traiter ici le cas 'value == 0'

    if f_a * value > 0:
        # f a le même signe en a et au milieu.
        return middle, b
    # Ici on sait que f_a et value ont un signe opposé
    return a, middle
    


a = 1
b = 1.5

for step_num in range(1, 11):
    a,b = one_step(a,b)
    middle = (a+b)/2
    value = fun(middle)
    print(f"étape {step_num} -- a={a}, b={b}, m={middle}, f(m)={value}")
