% La fonction suivante retourne le plus grand en valeur absolue de a et b.
function y=maxvalabs(a,b)
	if abs(a)>abs(b)
		y = a;
	else 
		y = b;
	end
end

% deux vecteurs de tests.
x = [1,4,8,-4,-4];
y = [-2,3,7,-5,5];

% On crée le vecteur z qui a la m\ême longueur que x. 
% Peu importe ce qu'il y a dedans parce qu'on va le redéfinir juste après.
z = 1:length(x)

for i = 1:length(x)
	z(i) = maxvalabs(x(i),y(i));
endfor

z
