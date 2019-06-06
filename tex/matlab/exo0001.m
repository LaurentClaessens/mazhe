function y=f(x)
y=(1+x).*exp(-x.^2+2*x.*cos(x))-(1+x.^4).^2.*sin(x)
end

X = -3:0.1:3
Y = f(X)
plot(X,Y)


print -dps exo0001.ps
