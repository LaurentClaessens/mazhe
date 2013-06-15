from scipy import stats

N=stats.norm
print N.mean()      # 0
print N.var()       # 1

xi = N.isf(0.95)
print xi            # -1.64485

N.cdf(xi)           # Vérification : 0.05

# Graphiques de la fonction de densité et la cumulative.
P=plot(N.cdf,x,-10,10)
Q=plot(N.pdf,x,-10,10,color="red")
show(P+Q)
