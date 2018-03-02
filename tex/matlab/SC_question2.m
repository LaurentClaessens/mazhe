printf ("Bonjour, comment ça va ?\n")

p = [4,-20,25,-4,20,-25]

v = roots(p)
racines = v'			# Le ' est pour la transposée parce que les boucles sur les vecteurs colonnes ne
				#  ne fonctionnent pas comme on le croirait.

reelles = []

for i = 1:length(racines)	# Faire une boucle sur les racines trouvées.
	if (imag(racines(i))==0)
		reelles = [reelles [real(racines(i))] ]		# Étendre le vecteur reelles par la partie réelle de racine(i)
	endif
endfor

# La fonction prod retourne le produit

produit_des_reelles = prod(reelles)


y = polyout(p,'x')

plot(y)
print -deps exo2.eps

printf("J'ai fini, à bientôt")
