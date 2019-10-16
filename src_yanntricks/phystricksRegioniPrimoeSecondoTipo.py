from yanntricks import *
def RegioniPrimoeSecondoTipo():
    fig = GenericFigure("RegioniPrimoeSecondoTipo")

    ssfig1=fig.new_subfigure(r'''Une region du premier type''', 'primotipo')
    ssfig2=fig.new_subfigure(r'''Une region du deuxi\`eme type''', 'secondotipo')
    pspict1=ssfig1.new_pspicture('regun')
    pspict2=ssfig2.new_pspicture('regdeux')

    pspicts=[pspict1,pspict2]

    a=1
    b=4
    m=float(b+a)/2
    x=var('x')
    f=phyFunction(sin(x+1)+2)
    g=phyFunction(-(x-2)**(2)+6)
    F=f.graph(a,b)
    G=g.graph(a,b)
    F.parameters.color="red"
    G.parameters.color="red"
    reg=SurfaceBetweenFunctions(f,g,a,b)
    reg.parameters.hatched()
    reg.parameters.hatch.color="red"
    reg.Isegment.parameters.style="dashed"
    reg.Fsegment.parameters.style="dashed"
    reg.curve1.parameters.style="solid"
    reg.curve1.parameters.color="blue"
    reg.curve2.parameters.style="solid"
    reg.curve2.parameters.color="blue"

    Xa=Point(a,0)
    Xb=Point(b,0)
    Xa.put_mark(0.3,-90,"$a$",pspicts=pspicts)
    Xb.put_mark(0.3,-90,"$b$",pspicts=pspicts)
    Mf=f.get_point(m)
    Mf.put_mark(0.3,Mf.advised_mark_angle(pspicts),"$g_1$",pspicts=pspicts)
    Mg=g.get_point(m)
    Mg.put_mark(0.3,Mg.advised_mark_angle(pspicts),"$g_2$",pspicts=pspicts)
    Mf.parameters.symbol=""
    Mg.parameters.symbol=""
    Sa=Segment(f.get_point(a),Xa)
    Sa.parameters.style="dotted"
    Sb=Segment(f.get_point(b),Xb)
    Sb.parameters.style="dotted"

    pspict1.axes.no_graduation()
    pspict1.DrawGraphs(reg,Xa,Xb,Mf,Mg,Sa,Sb,F,G)
    pspict1.DrawDefaultAxes()
    pspict1.dilatation(1)
    
    c=0
    d=4
    m=float(d+c)/2
    x=var('x')
    S=ParametricCurve(sin(x)+2,x+1).graph(c,d)
    P1=S.get_point(d)
    P4=S.get_point(c)
    R=ParametricCurve(((x-1)/3)**2+5,x+1).graph(c,d)
    P2=R.get_point(c)
    P3=R.get_point(d)
    Q=Segment(P1,P3)
    T=Segment(P4,P2)
    reg2=CustomSurface(S,Q,T,R)
    reg2.parameters.hatched()
    reg2.parameters.hatch.color="blue"
    Q.parameters.style="dashed"
    T.parameters.style="dashed"

    Xc=Point(0,S.get_point(c).y)
    Xd=Point(0,S.get_point(d).y)
    Xc.put_mark(0.3,180,"$c$",pspicts=pspicts)
    Xd.put_mark(0.3,180,"$d$",pspicts=pspicts)
    MS=S.get_point(m)
    MS.put_mark(0.3,MS.advised_mark_angle(pspicts).degree+180,"$h_1$",pspicts=pspicts)
    MR=R.get_point(m)
    MR.put_mark(0.3,0,"$h_2$",pspicts=pspicts)
    MS.parameters.symbol=""
    MR.parameters.symbol=""
    Sc=Segment(S.get_point(c),Xc)
    Sc.parameters.style="dotted"
    Sd=Segment(S.get_point(d),Xd)
    Sd.parameters.style="dotted"

    pspict2.axes.no_graduation()
    pspict2.DrawGraphs(reg2, S,Q,T,R,Xc,Xd,MS,MR,Sc,Sd)
    pspict2.DrawDefaultAxes()
    pspict2.dilatation(1)

    fig.conclude()
    fig.write_the_file()

