function z=f(x,y)
z=-(x.^2+y.^2)
end

[x,y] = ode45(@f,[0,2],1)
plot(x,y)

print -dps exo3novQ3.ps
