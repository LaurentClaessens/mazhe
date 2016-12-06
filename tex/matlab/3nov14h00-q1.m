function y=intergrande(t)
y=cos(sin(t));
end

function y=f(x)
y=quad('intergrande',0,x)-1/4;
end

reponse = fzero('f',0.3)		% 0.25265

X = 0:0.1:5;
Y = f(X);
plot(X,Y,'o')
print -dps exo0013.ps
