function y=f(x)
	if log(x)-x+2 < 0
		y = x.^2-4*x;
	else
		y = (log(x)+2).^2-4*x;
	endif
endfunction

X = 1:0.1:10;

Y = 1:length(X);
for i=1:length(X)
	Y(i)=f(X(i));
endfor

plot(X,Y)
print -dps exo55.ps

