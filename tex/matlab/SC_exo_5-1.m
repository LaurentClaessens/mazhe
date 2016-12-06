% Cette fonction donne x_{n+1} en fonction de x_n.
function y = recurrence(x)
	y=sqrt(2+x);
end

n = 12
x = 0;

% On va appliquer n fois la récurrence
for i = 1:n
	x = recurrence(x);
endfor

x

% Pour faire une fonction qui calcule le terme n, il suffit de faire 
% une fonction qui contient n fois la récurrence.
function y = xn(n)
	x = 0;
	for i = 1:n
		x = recurrence(x);
	endfor
	y = x;
end

% Pour calculer le terme numéro 100 de la suite :
TermeCent = xn(100)
