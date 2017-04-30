u = 1:6				# u = 1:1:6 fait la même chose.
A = eye(6)+(u'*u)/4

B = A

B(2,3) = A(2,3)+2
B(:,2) = log(2)*B(:,2)		# B(:,2) représente la deuxième colone de B

C = inv(B)*B
comparaison = eye(6)-C

erreur_max = max(max(abs(comparaison)))		
# max appliqué à une matrice retourne le vecteur 
# qui contient le plus grand de chaque colonne.
# Donc il faut appliquer deux fois max pour prendre le max de ces max

solution = A\u'

verification = A*solution - u'
erreur_max = max(abs(verification))
