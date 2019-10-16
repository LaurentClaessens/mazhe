from yanntricks import *
def ExerciceGraphesbis():
    fig = GenericFigure("ExerciceGraphesbis")

    ssfig1 = fig.new_subfigure("","cosinus")
    pspict1 = ssfig1.new_pspicture("cosinus")
    ssfig2 = fig.new_subfigure("", "valabsoluecosinus")
    pspict2 =ssfig2.new_pspicture("valabsoluecosinus")
    ssfig3 = fig.new_subfigure("", "cosxplusun")
    pspict3 = ssfig3.new_pspicture("cosxplusun")
    ssfig4 = fig.new_subfigure("","sinus" )
    pspict4 = ssfig4.new_pspicture("sinus")
    ssfig5 = fig.new_subfigure("", "cosex")
    pspict5 = ssfig5.new_pspicture("cosex")
    ssfig7 = fig.new_subfigure("","sqrtcos" )
    pspict7 = ssfig7.new_pspicture("sqrtcos")
    ssfig9 = fig.new_subfigure("","cosquattrox" )
    pspict9 = ssfig9.new_pspicture("cosquattrox")

    x=var('x')
    r=1
    eps=exp(-2)

    # Fonctions
    f1=cos(x)
    f2=abs(cos(x))
    f3=cos(x)+1
    f4=cos(x+pi/2)
    f5=cos(exp(x))
    f7=sqrt(cos(x))
    f9=cos(4*x)

        # Graphes
    F1=phyFunction(f1).graph(-pi, 3*pi/2)
    F2=phyFunction(f2).graph(-pi, 3*pi/2)
    F3=phyFunction(f3).graph(-pi,3*pi/2)
    F4=phyFunction(f4).graph(-pi,3*pi/2)
    F5=phyFunction(f5).graph(-pi,3*pi/2)
    F7a=phyFunction(f7).graph(-pi/2, pi/2)
    F7b=phyFunction(f7).graph(3*pi/2, 2*pi)
    F9=phyFunction(f9).graph(-pi, 3*pi/2)

        # Figures
    pspict1.dilatation(.7)
    pspict1.DrawGraphs(F1)
    pspict1.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict1.axes.Dx=0.5
    pspict1.DrawDefaultAxes()

    pspict2.dilatation(.7)
    pspict2.DrawGraphs(F2)
    pspict2.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict2.axes.Dx=0.5
    pspict2.DrawDefaultAxes()

    pspict3.dilatation(.5)
    pspict3.DrawGraphs(F3)
    pspict3.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict3.axes.Dx=0.5
    pspict3.DrawDefaultAxes()

    pspict4.dilatation(.7)
    pspict4.DrawGraphs(F4)
    pspict4.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict4.axes.Dx=0.5
    pspict4.DrawDefaultAxes()

    pspict5.dilatation(.7)
    F5.linear_plotpoints=1000
    pspict5.DrawGraphs(F5)
    pspict5.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict5.axes.Dx=0.5
    pspict5.DrawDefaultAxes()


    pspict7.comment="The function is drawn in two parts"
    pspict7.dilatation(.7)
    pspict7.DrawGraphs(F7a)
    pspict7.DrawGraphs(F7b)  
    pspict7.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict7.axes.Dx=0.5
    pspict7.DrawDefaultAxes()

    pspict9.dilatation(.7)
    pspict9.DrawGraphs(F9)
    pspict9.axes.axes_unitX=AxesUnit(pi,"\\pi")
    pspict9.axes.Dx=0.5
    pspict9.DrawDefaultAxes()


    fig.conclude()
    fig.write_the_file()

