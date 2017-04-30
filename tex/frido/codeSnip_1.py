from __future__ import division

def bissection(f, a, b, toll, mmax):
    """
    f : une fonction
    a,b : les limites de l'intervalle
    toll : la tolérance. C'est l'amplitude de l'intervalle à partir duquel nous nous arrêtons.
    nmax : le nombre maximum d'itérations.

    Nous supposons que \( b>a\).

    Retourne un tuple (x,n) où 'x' est la solution approchée et 'n' est le nombre d'itérations effectuées
    """
    n = -1
    amp = toll + 1 # Pour s'assurer que l'on entre dans le cycle
    while amp > toll and n < nmax :
        n = n + 1
        amp=abs(b - a)
        x = a + amp / 2
        if f(a) * f(x) < 0:
            b = x
        elif f(a)*f(x) > 0:
            a = x
        else :      # Problème ZERO
            amp = 0
    return (x, n)
