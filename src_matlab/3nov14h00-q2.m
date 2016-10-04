function y=f(t)
y=exp(cos(t)).*sin(t-1).^2+2*sqrt(t.^3+7*t)
end

X = 0:0.1:10
Y = f(X)
plot(X,Y)
print -dps exo3novQ2.ps
