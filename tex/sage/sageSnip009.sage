var('y')

# les fonctions coordonnées
F1(x,y)=x/(x**2+y**2)
F2(x,y)=-y/(x**2+y**2)

# La matrice différentielle :
A=matrix( [  [F1.diff(x).simplify_full(),F1.diff(y).simplify_full()],[F2.diff(x).simplify_full(),F2.diff(y).simplify_full()]   ] )

# Quelqu'un peut expliquer pourquoi ceci ne fonctionne pas ?
# A=matrix( [  [F1.diff(x),F1.diff(y)],[F2.diff(x),F2.diff(y)]   ] ).simplify_full()

# A^tA
S=A.transpose()*A
S=S.simplify_full()     # Mais ça, ça marche !!
print(S)
