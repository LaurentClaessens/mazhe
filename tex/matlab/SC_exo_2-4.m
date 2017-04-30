function y = f1(x)
	y = sin(x)+sin(3*x)/3+sin(5*x)/5+sin(7*x)/7
end

function y = f2(x)
	y = (x.^2.*abs(x-2)).^(1/3)
end

function y = f3(x)
	y = sqrt(x).*sin(1./x)
end

# Créer un vecteur avec les valeurs où on va calculer la fonction
echantillon = 0:0.1:2*pi		
# Créer le vecteur avec les valeurs de la fonction
v = f1(echantillon)			
# Créer le graphique
plot(echantillon,v)			
# Enregistrer le graphique dans exo24_f1.ps
print -dps exo24_f1.ps			

echantillon = -3:0.1:3		
v = f2(echantillon)	
plot(echantillon,v)
print -dps exo24_f2.ps			

echantillon = 10^(-2):0.1:pi	
v = f3(echantillon)	
plot(echantillon,v)
print -dps exo24_f3.ps			

# Notez la différence avec ce zoom sur la partie 0->0.5 
# avec un pas de 0.001 au lieu de 0.1

echantillon = 10^(-2):0.001:0.4	
v = f3(echantillon)	
plot(echantillon,v)
print -dps exo24_f3_zoom.ps			

# Il y a une oscillation infinie qu'on devine maintenant 
# mais qui était presque invisible sur le graphique avec un pas de 0.1.
