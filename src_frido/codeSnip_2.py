def Newton(f,x0,toll,maxit):
    fp=f.derivative()
    n=0
    x=x0
    diff=toll+1
    while abs(diff)>toll and n<maxit:
        n=n+1
        diff=-f(x)/fp(x)
        x=x+diff
    return x,n
