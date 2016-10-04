function y=f(x)
a=3
y=x.*exp(-x/a)
endfunction

function y=fp(x)
y=-(1/3)*x.*exp(-x/3)+exp(-x/3)
endfunction

X=-2:0.1:10
Y=f(X)

xmax=fzero('fp',2)
ymax=f(xmax)
plot(X,Y,xmax,ymax,'o')

print -dps G21-1.ps
