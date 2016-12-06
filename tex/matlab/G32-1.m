function retour=Cauchy(x,y)
retour = y/2 + 2*exp(x/2).*cos(2*x)
end

function retour=solution(x)
retour = sin(2*x).*exp(x/2)
end

[x,y]=ode45(@Cauchy,[0,4],0)

X = 0:0.1:4
Y=solution(X)
plot(x,y,X,Y)
print -dps G32-1.ps
