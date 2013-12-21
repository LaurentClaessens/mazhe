#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

from phystricksNEtAchr import NEtAchr
#from phystricksAIFsOQO import AIFsOQO
from phystricksRQsQKTl import RQsQKTl
from phystricksDynkinpWjUbE import DynkinpWjUbE
from phystricksHasseAGdfdy import HasseAGdfdy
from phystricksDynkinNUtPJx import DynkinNUtPJx
from phystricksDynkinrjbHIu import DynkinrjbHIu
from phystricksDynkinqlgIQl import DynkinqlgIQl
from phystricksADUGmRR import ADUGmRR_A,ADUGmRR_B,ADUGmRR_C
from phystricksTGdUoZR import TGdUoZR
from phystricksTGdUoZR import AIFsOQO
from phystricksTGdUoZR import GBnUivi
from phystricksFGWjJBX import FGWjJBX
from phystricksMNICGhR import MNICGhR
from phystricksMNICGhR import LEJNDxI
from phystricksMNICGhR import RGjjpwF
from phystricksMNICGhR import STdyNTH
from phystricksQPcdHwP import QPcdHwP
from phystricksHNxitLj import HNxitLj
from phystricksEJRsWXw import EJRsWXw
from phystricksRLuqsrr import RLuqsrr
from phystricksDTIYKkP import DTIYKkP
from phystricksSFdgHdO import SFdgHdO

figures_list=[
        HasseAGdfdy,DynkinpWjUbE,DynkinNUtPJx,DynkinrjbHIu,DynkinqlgIQl,ADUGmRR_A,ADUGmRR_B,ADUGmRR_C,TGdUoZR,GBnUivi,FGWjJBX,RQsQKTl,MNICGhR,LEJNDxI,RGjjpwF,STdyNTH,QPcdHwP,HNxitLj,AIFsOQO,NEtAchr,EJRsWXw,RLuqsrr,DTIYKkP,SFdgHdO
        ]

def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"(almost) all I know in mathematics and physics")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        ProjPoly()
