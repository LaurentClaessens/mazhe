from phystricks import *
def ExerciceGraphes():
    fig = GenericFigure("ExerciceGraphes")

    ssfig=[]
    pspict=[]
    liste_noms=["logarithme","lnvalabsolue","lnxplusun","valabsolueln","unplusln","sqrtln","lnsqrt"]
    for i in range(1,8):
        ssfig.append( fig.new_subfigure("","label"+liste_noms[i-1])) 
    for i in range(len(liste_noms)):
        pspict.append( ssfig[i].new_pspicture(liste_noms[i]) )

    r=1
    eps=exp(-2)
    # Fonctions
    x=var('x')
        
    f1=ln(x)
    f2=ln(abs(x))
    f3=ln(x+r)
    f4=ln(x)+r
    f5=abs(ln(x))
    f6=sqrt(ln(x))
    f7=ln(x**2)

        # Graphes
    F=[phyFunction(f1).graph(eps,2),(phyFunction(f2).graph(eps,2),phyFunction(f2).graph(-2, -eps)),phyFunction(f3).graph(eps-1,2),phyFunction(f4).graph(eps,2),phyFunction(f5).graph(eps,3),phyFunction(f6).graph(1,3),(phyFunction(f7).graph(eps,2),phyFunction(f7).graph(-2, -eps))]


        # Figures
    for i in range(0,len(pspict)):
        pspict[i].DrawGraphs(F[i])
        pspict[i].DrawDefaultAxes()
        pspict[i].dilatation(1)

        pspict[0].BB.AddX(-0.5)
        pspict[0].BB.AddY(3.5)

    pspict[1].BB.AddX(-2)
    pspict[1].BB.AddY(3)

    pspict[2].BB.AddX(-2)
    pspict[2].BB.AddY(3)

    pspict[3].BB.AddX(-1)
    pspict[3].BB.AddY(3)

    pspict[4].BB.AddX(-2)
    pspict[4].BB.AddY(3)
    pspict[4].BB.AddY(-3)

    pspict[5].BB.AddX(-2)
    pspict[5].BB.AddY(3)
    pspict[5].BB.AddY(-3)

    pspict[6].BB.AddX(-2)
    pspict[6].BB.AddY(3)

    
    fig.conclude()
    fig.write_the_file()
