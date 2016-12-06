function retour=phi(t)
retour = sqrt(t)*cos(t);
end

function retour = f(x)
retour = x.^2*quad('phi',0,x);
end

f(1)	#0.53120
X=0:0.1:3
Y=[]
for	i = 1:length(X) 
	Y(i)=f(X(i))	;
end

plot(X,Y)
print -dps G31-3.ps
