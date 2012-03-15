from phystricks import *
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

    for i,psp in enumerate(pspict):
        print i
        list_to_be_drawn = [a for a in psp.record_draw_graph if a.take_graph]
        for x in list_to_be_drawn:
            print x.graph
            print x.graph.bounding_box(psp)


    fig.conclude()
    fig.write_the_file()
