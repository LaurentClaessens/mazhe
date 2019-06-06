# -*- coding: utf8 -*-
from phystricks import *
def CurvilignesPolaires():

    fig = GenericFigure("CurvilignesPolaires")

    def Vision(fig,rayon,theta,caption):
        ssfig=fig.new_subfigure(caption)
        pspict=ssfig.new_pspicture("")

        O=Point(0,0)
        C=Circle(O,rayon).graph(theta-30,theta+30)
        C.parameters.color="brown"
        C.parameters.style="dashed"

        P=C.get_point(theta)
        l=Segment(O,P).add_size(-rayon+0.5,1.5)
        l.parameters=C.parameters

        vr=C.get_normal_vector(theta)
        vtheta=C.get_tangent_vector(theta)
        vr.parameters.color="red"
        vtheta.parameters.color="red"

        vr.put_mark(0.3,vr.advised_mark_angle(pspict),r"$e_{r}$",pspict=pspict)
        vtheta.put_mark(0.3,45,r"$e_{\theta}$",pspict=pspict)

        pspict.DrawGraphs(C,l,vr,vtheta)

    Vision(fig,2,30,u"Base locale.") 
    Vision(fig,1.5,200,u"Base locale.") 

    fig.conclude()
    fig.write_the_file()

