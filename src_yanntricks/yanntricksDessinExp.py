from yanntricks import *
def DessinExp():
    pspict,fig = MultiplePictures("DessinExp",6)

    x=var('x')

    F=[]
    F.append(phyFunction(exp(x)).graph(-3,2))
    F.append(phyFunction(exp(-x)).graph(-2,3))
    F.append(phyFunction(-exp(x)).graph(-3,2))
    F.append(phyFunction(-exp(-x)).graph(-2,3))
    F.append(phyFunction(exp(x-2)).graph(-1,4))
    F.append(phyFunction(exp(x)-2).graph(-3,2))

    for i,f in enumerate(F):
    pspict[i].mother.caption="La fonction ${0}$".format(latex(f.sage))
    pspict[i].DrawGraphs(f)
    pspict[i].DrawDefaultAxes()
    pspict[i].dilatation(1)

    fig.conclude()
    fig.write_the_file()

