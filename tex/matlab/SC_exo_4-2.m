function y=Integrande(t)
y = exp(t.^2);
end

% La fonction qui à x fait correspondre l'intégrale de f entre 0 et x
function y=Integrale(x)
y=quad('Integrande',0,x);
end

% La fonction Dawson de l'énoncé
function y=Dawson(x)
y=exp(-x.^2)*Integrale(x);
end

reponseA = Dawson(1)	% 0.53808

function y=Dawsonbis(x)
y=Dawson(x)-0.5;
end

reponseB = fzero('Dawsonbis',0.7) % 0.66607
