var('N')
h=1/(N+1)
f1=(N+1)*x
f2=-(N+1)*x+2
f3=(N+1)*x-1
f4=-(N+1)*x+3

inner11=(f1*f1).integrate(x,0,h)+(f2*f2).integrate(x,h,2*h)
inner12=(f2*f3).integrate(x,h,2*h)

print(inner11.simplify_full())
print(inner12.simplify_full())

# For the inner products of the derivatives :

d_inner11=(f1.derivative(x)*f1.derivative(x)).integrate(x,0,h)+(f2.derivative(x)*f2.derivative(x)).integrate(x,h,2*h)
d_inner12=(f2.derivative(x)*f3.derivative(x)).integrate(x,h,2*h)

print(d_inner11.simplify_full())
print(d_inner12.simplify_full())
