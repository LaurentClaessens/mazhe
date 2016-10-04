annee =	 [1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007]
cons =	[72231 73588 72377 74916 74847 74478 77031 80326 81255 81659 81533]

consommation = cons*365/(10^6)
p = polyfit(annee,consommation,1)

long_terme = 1997:2050
theorie = polyval(p,long_terme)

plot(annee,consommation,'o',long_terme,theorie)
print -dps petrole.ps

% Consomation extrapolée année par année : 
extracons = polyval(p,2009:2050)
% Consomation en 2050 :
polyval(p,2050)

% Somme de notre consommation entre 2009 et 2050 :
sum(extracons)

