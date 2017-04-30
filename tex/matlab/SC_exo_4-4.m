function retour=Cauchy(x,y)
retour = x.^2+(y.^2)/4;
end

[X,Y] = ode45(@Cauchy,[0 1.5],0.2);

z = Cauchy(X,Y)

plot(X,Y,X,z,'o')
print -dps exo44.ps
