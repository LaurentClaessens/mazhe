function y=l(lz,v)
c=3*10^8
y=lz*sqrt(1-(v.^2/c^2))
end
c=3*10^8
lz = 1.3
X = 0:10000:c
Y = l(lz,X)
plot(X,Y)
print -dps exo3novQ4.ps
