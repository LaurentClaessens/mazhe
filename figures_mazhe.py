#! /usr/bin/sage -python
# -*- coding: utf8 -*-

# Il faut en tout cas refaire la figure PHTVjfk

from phystricks import *
import sys

"""

Dans un premier temps, je ne fais que la partie sur l'agrégation.

Compiler les figures
Vérifier les "does not contain"
Compiler le document sans external
Copier les fichiers .aux dans un répertoire à part.
Compiler les figures
Compiler le document avec external
"""

from phystricksUZGooBzlYxr import UZGooBzlYxr
from phystricksACUooQwcDMZ import ACUooQwcDMZ
from phystricksZTTooXtHkci import ZTTooXtHkci
from phystricksFXVooJYAfif import FXVooJYAfif
from phystricksWHCooNZAmYB import WHCooNZAmYB
from phystricksQIZooQNQSJj import QIZooQNQSJj
from phystricksUYJooCWjLgK import UYJooCWjLgK
from phystricksEHDooGDwfjC import EHDooGDwfjC
from phystricksALIzHFm import ALIzHFm
from phystricksTZCISko import TZCISko
from phystricksNEtAchr import NEtAchr
from phystricksRQsQKTl import RQsQKTl
from phystricksDynkinpWjUbE import DynkinpWjUbE
from phystricksHasseAGdfdy import HasseAGdfdy
from phystricksDynkinNUtPJx import DynkinNUtPJx
from phystricksDynkinrjbHIu import DynkinrjbHIu
from phystricksDynkinqlgIQl import DynkinqlgIQl
from phystricksADUGmRR import ADUGmRRA
from phystricksADUGmRR import ADUGmRRB
from phystricksADUGmRR import ADUGmRRC
from phystricksTGdUoZR import TGdUoZR
from phystricksTGdUoZR import AIFsOQO
from phystricksTGdUoZR import GBnUivi
from phystricksTGdUoZR import IYAvSvI
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

from phystricksJGuKEjH import JGuKEjH
from phystricksMCKyvdk import MCKyvdk
from phystricksIWuPxFc import IWuPxFc
from phystricksMCQueGF import MCQueGF
from phystricksYWxOAkh import YWxOAkh
from phystricksLAfWmaN import LAfWmaN
from phystricksMaxVraissLp import MaxVraissLp
from phystricksBiaisOuPas import BiaisOuPas
from phystricksChiSquared import ChiSquared
from phystricksChiSquaresQuantile import ChiSquaresQuantile
from phystricksratrap import ratrap
from phystricksCouroneExam import CouroneExam
from phystricksContourTgNDivergence import ContourTgNDivergence
from phystricksContourSqL import ContourSqL
from phystricksContourGreen import ContourGreen
from phystricksExSinLarge import ExSinLarge
from phystricksToreRevolution import ToreRevolution
from phystricksConeRevolution import ConeRevolution
from phystricksExPolygone import ExPolygone
from phystricksIntegraleSimple import IntegraleSimple
from phystricksExoMagnetique import ExoMagnetique
from phystricksCurvilignesPolaires import CurvilignesPolaires
from phystricksRefraction import Refraction
from phystricksMomentForce import MomentForce
from phystricksParallelogramme import Parallelogramme
from phystricksDivergenceTrois import DivergenceTrois
from phystricksDivergenceDeux import DivergenceDeux
from phystricksDivergenceUn import DivergenceUn
from phystricksArcCercleAngle import ArcCercleAngle
from phystricksChampGraviation import ChampGraviation
from phystricksFnCosApprox import FnCosApprox
from phystricksNiveauHyperbole import NiveauHyperbole
from phystricksNiveauHyperbole import NiveauHyperboleDeux
from phystricksBateau import Bateau
from phystricksFonctionXtrois import FonctionXtrois
from phystricksFonctionEtDerive import FonctionEtDerive
from phystricksSurfaceDerive import SurfaceDerive
from phystricksRechercheTangente import VGZooJnvvZc
from phystricksDerivTangente import DerivTangente
from phystricksCoordPolaires import CoordPolaires
from phystricksDefinitionCartesiennes import DefinitionCartesiennes
from phystricksProjectionScalaire import ProjectionScalaire
from phystricksCercleTrigono import CercleTrigono
from phystricksTgCercleTrigono import TgCercleTrigono
from phystricksExoPolaire import ExoPolaire
from phystricksExoProjection import ExoProjection
from phystricksExoUnSurxPolaire import ExoUnSurxPolaire
from phystricksSurfaceHorizVerti import SurfaceHorizVerti
from phystricksSurfaceCercle import SurfaceCercle
from phystricksIntRectangle import IntRectangle
from phystricksIntTriangle import IntTriangle
from phystricksIntEcourbe import IntEcourbe
from phystricksIntBoutCercle import IntBoutCercle
from phystricksIntDeuxCarres import IntDeuxCarres
from phystricksMoulinEau import MoulinEau
from phystricksMethodeNewton import MethodeNewton
from phystricksSurfacePrimiteGeog import SurfacePrimiteGeog
from phystricksSurfaceEntreCourbes import SurfaceEntreCourbes
from phystricksChoixInfini import ChoixInfini
from phystricksProjPoly import ProjPoly
from phystrickstrigoWedd import trigoWedd
from phystricksDisqueConv import DisqueConv
from phystricksCercleImplicite import CercleImplicite
from phystricksExempleNonRang import ExempleNonRang
from phystricksCercleTnu import CercleTnu
from phystricksExoXLVL import ExoXLVL
from phystricksFWJuNhU import FWJuNhU
from phystricksDessinLim import DessinLim
from phystricksQQa import QQa
from phystricksQCb import QCb
from phystricksLaurin import Laurin
from phystricksCoinPasVar import CoinPasVar
from phystricksExoVarj import ExoVarj
from phystricksTriangleUV import TriangleUV
from phystricksKScolorD import KScolorD
from phystricksIsomCarre import IsomCarre
from phystricksCheminFresnel import CheminFresnel
from phystricksSuiteUnSurn import SuiteUnSurn
from phystricksSpiraleLimite import SpiraleLimite
from phystricksCornetGlace import CornetGlace
from phystricksCSCvi import CSCvi
from phystricksCSCii import CSCii
from phystricksCSCiii import CSCiii
from phystricksCSCiv import CSCiv
from phystricksCSCv import CSCv
from phystricksCardioideexo import Cardioideexo
from phystricksOsculateur import Osculateur
from phystricksQuelCote import QuelCote
from phystricksAdhIntFr import AdhIntFr
from phystricksAdhIntFrDeux import AdhIntFrDeux
from phystricksAdhIntFrTrois import AdhIntFrTrois
from phystricksAdhIntFrSix import AdhIntFrSix
from phystricksDifferentielle import Differentielle
from phystricksMethodeChemin import MethodeChemin
from phystricksDeuxCercles import DeuxCercles
from phystricksIntTrois import IntTrois
from phystricksTraceCycloide import TraceCycloide
from phystricksArcLongueurFinesse import ArcLongueurFinesse
from phystricksTangentSegment import TangentSegment
from phystricksBoulePtLoin import BoulePtLoin
from phystricksIntervalleUn import IntervalleUn
from phystricksUneCellule import UneCellule
from phystricksDistanceEuclide import DistanceEuclide
from phystricksLesSpheres import LesSpheres
from phystricksDistanceEnsemble import DistanceEnsemble
from phystricksAccumulationIsole import AccumulationIsole
from phystricksSenoTopologo import SenoTopologo
from phystricksRegioniPrimoeSecondoTipo import RegioniPrimoeSecondoTipo
from phystricksPolirettangolo import Polirettangolo
from phystricksParamTangente import ParamTangente
from phystricksExampleIntegrationdeux import ExampleIntegrationdeux
from phystricksExampleIntegration import ExampleIntegration
from phystricksCardioid import Cardioid
from phystricksCycloideA import CycloideA
from phystricksSuiteInverseAlterne import SuiteInverseAlterne
from phystricksCourbeRectifiable import CourbeRectifiable
from phystricksExempleArcParam import ExempleArcParam
from phystricksexamssepti import examssepti
from phystricksexamsseptii import examsseptii
from phystricksExoParamCD import ExoParamCD
from phystricksCbCartTui import CbCartTui
from phystricksCbCartTuii import CbCartTuii
from phystricksCbCartTuiii import CbCartTuiii
from phystricksPHTVjfk import PHTVjfk
from phystrickssenotopologo import senotopologo
from phystricksQXyVaKD import QXyVaKD
from phystricksTriangleRectangle import TriangleRectangle
from phystricksTracerUn import TracerUn
from phystricksExerciceGraphesbis import ExerciceGraphesbis
from phystricksGrapheunsurunmoinsx import Grapheunsurunmoinsx
from phystricksExoCUd import ExoCUd
from phystricksUnSurxInt import UnSurxInt
from phystricksAireParabole import AireParabole
from phystricksPartieEntiere import PartieEntiere
from phystricksMantisse import Mantisse
from phystricksDS2010ExoGraph import DS2010ExoGraph
from phystricksSolsEqDiffSin import SolsEqDiffSin
from phystricksSolsSinpA import SolsSinpA
from phystricksTrajs import Trajs

# Suppression août 2014
#from figure_devoir1 import exercice1A1
#from figure_devoir1 import exercice1A2
#from figure_devoir1 import exercice4
#from phystricksExerciceGraphes import ExerciceGraphes              # Remplacé par ACUooQwcDMZ
#from phystricksIntCourbePolaire import IntCourbePolaire
#from phystricksExoCourone import ExoCourone
#from phystricksExampleChangementVariables import ExampleChangementVariables
#from phystricksAIFsOQO import AIFsOQO  # Il n'est pas dans le fichier phystricksAIFsOQO.
#from phystricksDessinExp import DessinExp
#from phystricksDS2010exo1 import DS2010exo1
#from phystricksDS2010bisExoGraph import DS2010bisExoGraph

figures_list=[]
figures_list.append(MoulinEau)
figures_list.append(IntegraleSimple)
figures_list.append(ExoMagnetique)
figures_list.append(CurvilignesPolaires)
figures_list.append(Refraction)
figures_list.append(IsomCarre)
figures_list.append(MomentForce)
figures_list.append(CouroneExam)
figures_list.append(SurfacePrimiteGeog)
figures_list.append(SurfaceEntreCourbes)
figures_list.append(DivergenceTrois)
figures_list.append(DivergenceDeux)
figures_list.append(DivergenceUn)
figures_list.append(ArcCercleAngle)
figures_list.append(ExoXLVL)
figures_list.append(Laurin)
figures_list.append(ChampGraviation)
figures_list.append(FnCosApprox)
figures_list.append(Bateau)
figures_list.append(FonctionXtrois)
figures_list.append(FonctionEtDerive)
figures_list.append(SurfaceDerive)
figures_list.append(DerivTangente)
figures_list.append(ExoUnSurxPolaire)
figures_list.append(DessinLim)
figures_list.append(ExoProjection)
figures_list.append(ExoPolaire)
figures_list.append(TriangleRectangle)
figures_list.append(CercleTnu)
figures_list.append(QCb)
figures_list.append(ProjectionScalaire)
figures_list.append(CercleTrigono)
figures_list.append(TgCercleTrigono)
figures_list.append(SurfaceHorizVerti)
figures_list.append(SurfaceCercle)
figures_list.append(KScolorD)
figures_list.append(CheminFresnel)
figures_list.append(IntRectangle)
figures_list.append(IntTriangle)
figures_list.append(CoinPasVar)
figures_list.append(IntEcourbe)
figures_list.append(IntBoutCercle)
figures_list.append(IntDeuxCarres)
figures_list.append(ExPolygone)
figures_list.append(CercleImplicite)
figures_list.append(QQa)
figures_list.append(ConeRevolution)
figures_list.append(ChoixInfini)
figures_list.append(ProjPoly)
figures_list.append(trigoWedd)
figures_list.append(DisqueConv)
figures_list.append(ExempleNonRang)
figures_list.append(ToreRevolution)
figures_list.append(ExSinLarge)
figures_list.append(ContourGreen)
figures_list.append(ContourSqL)
figures_list.append(ContourTgNDivergence)
figures_list.append(ratrap)
figures_list.append(MaxVraissLp)
figures_list.append(BiaisOuPas)
figures_list.append(ChiSquared)
figures_list.append(ChiSquaresQuantile)
figures_list.append(MethodeNewton)
figures_list.append(ExoVarj)
figures_list.append(TriangleUV)
figures_list.append(DefinitionCartesiennes)
figures_list.append(CoordPolaires)
figures_list.append(Parallelogramme)
figures_list.append(CbCartTui)
figures_list.append(CbCartTuii)
figures_list.append(CbCartTuiii)
figures_list.append(SuiteUnSurn)
figures_list.append(SpiraleLimite)
figures_list.append(IntTrois)
figures_list.append(CornetGlace)
figures_list.append(Differentielle)
figures_list.append(CSCiv)
figures_list.append(CSCvi)
figures_list.append(CSCii)
figures_list.append(CSCiii)
figures_list.append(CSCv)
figures_list.append(Cardioideexo)
figures_list.append(DistanceEuclide)
figures_list.append(LesSpheres)
figures_list.append(IntervalleUn)
figures_list.append(DistanceEnsemble)
figures_list.append(AccumulationIsole)
figures_list.append(MethodeChemin)
figures_list.append(ExempleArcParam)
figures_list.append(CourbeRectifiable)
figures_list.append(SuiteInverseAlterne)
figures_list.append(CycloideA)
figures_list.append(Cardioid)
figures_list.append(ParamTangente)
figures_list.append(Polirettangolo)
figures_list.append(RegioniPrimoeSecondoTipo)
figures_list.append(ExampleIntegration)
figures_list.append(ExampleIntegrationdeux)
figures_list.append(ArcLongueurFinesse)
figures_list.append(TangentSegment)
figures_list.append(BoulePtLoin)
figures_list.append(UneCellule)
figures_list.append(SenoTopologo)
figures_list.append(AdhIntFr)
figures_list.append(AdhIntFrDeux)
figures_list.append(AdhIntFrTrois)
figures_list.append(AdhIntFrSix)
figures_list.append(DeuxCercles)
figures_list.append(TraceCycloide)
figures_list.append(QuelCote)
figures_list.append(Osculateur)
figures_list.append(examssepti)
figures_list.append(examsseptii)
figures_list.append(LAfWmaN)
figures_list.append(YWxOAkh)
figures_list.append(MCQueGF)
figures_list.append(PHTVjfk)
figures_list.append(IWuPxFc)
figures_list.append(MCKyvdk)
figures_list.append(senotopologo)
figures_list.append(NiveauHyperbole)
figures_list.append(NiveauHyperboleDeux)
figures_list.append(JGuKEjH)
figures_list.append(FWJuNhU)
figures_list.append(QXyVaKD)
figures_list.append(HasseAGdfdy)
figures_list.append(DynkinpWjUbE)
figures_list.append(DynkinNUtPJx)
figures_list.append(DynkinrjbHIu)
figures_list.append(DynkinqlgIQl)
figures_list.append(ADUGmRRA)
figures_list.append(ADUGmRRB)
figures_list.append(ADUGmRRC)
figures_list.append(TGdUoZR)
figures_list.append(GBnUivi)
figures_list.append(FGWjJBX)
figures_list.append(RQsQKTl)
figures_list.append(MNICGhR)
figures_list.append(LEJNDxI)
figures_list.append(RGjjpwF)
figures_list.append(STdyNTH)
figures_list.append(QPcdHwP)
figures_list.append(HNxitLj)
figures_list.append(NEtAchr)
figures_list.append(EJRsWXw)
figures_list.append(RLuqsrr)
figures_list.append(DTIYKkP)
figures_list.append(SFdgHdO)
figures_list.append(IYAvSvI)
figures_list.append(TZCISko)
figures_list.append(ALIzHFm)
figures_list.append(TracerUn)
figures_list.append(ACUooQwcDMZ)
figures_list.append(ExerciceGraphesbis)
figures_list.append(Grapheunsurunmoinsx)
figures_list.append(ExoCUd)
figures_list.append(UnSurxInt)
figures_list.append(AireParabole)
figures_list.append(PartieEntiere)
figures_list.append(Mantisse)
figures_list.append(SolsEqDiffSin)
figures_list.append(SolsSinpA)
figures_list.append(Trajs)
figures_list.append(UYJooCWjLgK)
figures_list.append(WHCooNZAmYB)
figures_list.append(QIZooQNQSJj)
figures_list.append(FXVooJYAfif)
figures_list.append(ExoParamCD)
figures_list.append(ZTTooXtHkci)
figures_list.append(EHDooGDwfjC)
figures_list.append(UZGooBzlYxr)
figures_list.append(AIFsOQO)
figures_list.append(VGZooJnvvZc)
"""
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
figures_list.append(<++>)
"""

def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"(almost) all I know in mathematics and physics")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        ProjPoly()
