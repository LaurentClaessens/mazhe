function retour=Cauchy(x,y)
retour = 1+y.^2;
end

[x,y] = ode45(@Cauchy,[0 1.5],0)

X = 0:0.001:1.5;
Y = tan(X);

plot(x,y,'o',X,Y)
print -dps exo43.ps
