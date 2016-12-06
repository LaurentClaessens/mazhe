function y = f(fric)
	Re = 10^4
	y = sqrt(fric).*(0.4 +1.74.*log(Re.*sqrt(fric) ) )
end


debut = 0
fin = 0.05
pas = (fin-debut)/1000
echantillon = debut+pas:pas:fin
	% On ne commence pas à zéro parce que le log n'y a pas de sens.

valeurs = f(echantillon)

plot(echantillon,valeurs)		
print -dps exo2-5.ps	
