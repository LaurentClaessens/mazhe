function y=f(x)
	y = (exp(x)*x.^4)/(exp(x)-1).^2;
endfunction

% La fonction suivante donne la valeur de l'intégrale
% de la fonction demandée entre 0 et xm.
function y=Integrale(xm)
y = quad('f',0,xm);
endfunction

R = 8.314;
xm = 313/300;

reponse = (9*R/xm^3)*Integrale(xm)	% 23.636
