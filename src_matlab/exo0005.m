p = [1 0 0 0 0 -5 0 2]

X = -2:0.1:2
Y = polyval(p,X)

plot(X,Y)
print -dps exo0005.ps
