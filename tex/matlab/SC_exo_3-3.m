x = [21,236,384,2.6*10^3,1.8*10^4,3.9*10^4,5.8*10^5]
y = [13,3.7,4.4,1.7,0.92,0.58,0.15]

lnx = log(x)
lny = log(y)

% Une droite, est un polynôme de degré 1.
droite = polyfit(lnx,lny,1)
% -0.42109   3.84651

abcisses = [2,15]
ordonnees = polyval(droite,abcisses)

plot(abcisses,ordonnees,':',lnx,lny,'o')
print -dps exo33.ps
