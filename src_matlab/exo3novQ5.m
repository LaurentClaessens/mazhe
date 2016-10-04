function z=cauchy(x,y)
z= -sin(x)*y
end

function y=exact(x)
y=exp(cos(x))
end

e = exp(1)
[x,y]=ode45(@cauchy,[0,2],e)

X = 0:0.1:2
Y = exact(X)
plot(x,y,'o',X,Y)
print -dps exo3novQ5.ps

