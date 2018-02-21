# Dans un cas réel, vous avez nettement intérêt à
# créer une classe 'Vecteur' qui implémente somme, différence
# et norme.
def N(v):
    return abs( v[0] )+abs(v[1])

def parall(v,w):
    # La différence v-w
    d=( v[0]-w[0],v[1]-w[1] )
    # La somme v+w
    s=( v[0]+w[0],v[1]+w[1] )

    return N(d)**2+N(s)**2-2*N(v)**2-2*N(w)**2
