function y=f(x)
y=4.144*(10^(14))./x.^2
endfunction

function y=W(x)
R=6500000
y=quad(@f,R,R+x)
endfunction

h=10000

X=0:100:10000
Y=1:length(X)
for i=1:length(X)
	Y(i)=W(X(i))
endfor
plot(X,Y)
print -dps G22-2.ps

