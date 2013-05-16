function y=f1(x)
y=sin(x.^2)
endfunction

function y=f2(x)
y=exp(x)/4
endfunction

function y=f(x)
y=f1(x)-f2(x)
endfunction

X = 0:0.05:2
Y1 = f1(X)
Y2 = f2(X)

t1 = 0.7
t2 = 1.3

r1 = fzero('f',t1)
r2 = fzero('f',t2)

r1		%0.74452
r2		%1.3525

plot(X,Y1,X,Y2,r1,f1(r1),'o',r2,f1(r2),'o')
print -dps exo2-1.ps
