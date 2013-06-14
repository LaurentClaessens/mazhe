from scipy import stats

X=stats.expon(scale=5)
print(X.mean())     # retourne 5

P=plot( X.pdf,x,0,10 )
show(P)             # Affiche le graphique


