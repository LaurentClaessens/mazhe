% Ici, nous avons des données expérimentales, et puis une courbe théorique
% La stratégie sera la suivante :
% 1. Nous mettons les données expérimentales dans les vecteurs x et y.
% 2. Nous calculeront la courbe théorique avec un polyfit.
% 3. Pour tracer la courbe théorique, nous allons procéder comme d'habitude.
%		Nous commencerons par créer un vecteur d'abcisse X
%		et puis nous calculerons le vecteur d'ordonnées correspondant Y.

x = [290,300,310,320,330]
y = [1.15053,1.14950,1.1478,1.14656,1.14527]

% Pour trouver le polynôme de degré 3 qui passe le mieux par les points
% donnés par les vecteurs x et y, il faut utiliser la commande polyfit.
p = polyfit(x,y,3)
% 5.1667e-08  -4.8093e-05   1.4770e-02  -3.4821e-01

% Juste pour s'amuser à voir à quoi ressemble le polynôme, écrivons-le :
polyout(p,"T")

X = 250:350
Y = polyval(p,X)	
% polyval est la commande pour évaluer un polynôme en un point.
% Ici, on l'évalue en tous les points d'abscisse qu'on veut tracer.

plot(X,Y,':',x,y,'o')
print -dps exo32.ps
% Noter que je trace de 250 à 350 de façon très arbitraire. 
% Rien dans les données expérimentales ne montre la croissance de la 
% fonction entre 250 et 280, ni celle entre 340 et 350.
% D'un point de vue scientifique, la méfiance est de rigueur lorsqu'on
% extrapole des données en-dehors du domaine des expériences.

% Pour évaluer la valeur de p au point 316 : 
polyval(p,316)	%1.1470
