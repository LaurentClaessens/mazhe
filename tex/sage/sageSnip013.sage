def u(k):
    """
    return the kth term in the expansion of 'e'
    """
    return 1/factorial(k)

def sum_u(n):
    """
    return the sum of the 'n' first terms, that is with
    k froim 0 to n-1.
    """
    L=[  u(k) for k in range(0,n)  ]
    return sum(L)

s = sum_u(5)        # This is a fraction
print(s)
print( numerical_approx(s)  )
