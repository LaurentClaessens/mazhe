debut = 0
fin = pi/2
nombre = 20

v = debut:(fin-debut)/(nombre-1):fin

# Juste pour rire : vérification que c'est bien équidistant :
for i = 2:length(v)			# length(v) donne la longueur du vecteur v
	v(i)-v(i-1)
endfor

function y = f(x)
	y = exp(sin(x).^2)
endfunction

f(v)
%1.0000
%1.0068 
%...
%2.6998
%2.7183

