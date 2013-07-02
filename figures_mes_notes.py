#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

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
#from phystricksIntCourbePolaire import IntCourbePolaire
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
from phystricksRechercheTangente import TangenteQuestion
from phystricksRechercheTangente import TangenteDetail
from phystricksRechercheTangente import LesSubFigures
from phystricksDerivTangente import DerivTangente
from phystricksCoordPolaires import CoordPolaires
from phystricksDefinitionCartesiennes import DefinitionCartesiennes
from phystricksProjectionScalaire import ProjectionScalaire
from phystricksCercleTrigono import CercleTrigono
from phystricksTriangleRectangle import TriangleRectangle
from phystricksTgCercleTrigono import TgCercleTrigono
from phystricksExoPolaire import ExoPolaire
from phystricksExoProjection import ExoProjection
from phystricksExoUnSurxPolaire import ExoUnSurxPolaire
from phystricksSurfaceHorizVerti import SurfaceHorizVerti
from phystricksSurfaceCercle import SurfaceCercle
#from phystricksExoCourone import ExoCourone
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
from phystricksDessinExp import DessinExp
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
from phystricksExampleChangementVariables import ExampleChangementVariables
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
from phystricksDS2010exo1 import DS2010exo1
from phystricksPHTVjfk import PHTVjfk
from phystrickssenotopologo import senotopologo

from figure_devoir1 import exercice1A1,exercice1A2,exercice4
from phystricksTriangleRectangle import TriangleRectangle  # Il faudrait aussi le remettre dans figures_list

figures_list=[MoulinEau,IntegraleSimple,ExoMagnetique,CurvilignesPolaires,Refraction,IsomCarre, MomentForce,CouroneExam,SurfacePrimiteGeog,
        SurfaceEntreCourbes, DivergenceTrois,DivergenceDeux,DivergenceUn,ArcCercleAngle,ExoXLVL,Laurin, ChampGraviation,FnCosApprox,
        Bateau,FonctionXtrois,FonctionEtDerive, SurfaceDerive,DerivTangente,ExoUnSurxPolaire,DessinExp,DessinLim, ExoProjection,
        ExoPolaire,TriangleRectangle,CercleTnu,QCb, ProjectionScalaire,CercleTrigono,TgCercleTrigono, SurfaceHorizVerti,SurfaceCercle,KScolorD,
        CheminFresnel, IntRectangle,IntTriangle,CoinPasVar, IntEcourbe,IntBoutCercle,IntDeuxCarres,ExPolygone,CercleImplicite,QQa, ConeRevolution,
        ChoixInfini,ProjPoly,trigoWedd,DisqueConv,ExempleNonRang, ToreRevolution,ExSinLarge,ContourGreen,ContourSqL,ContourTgNDivergence,ratrap,
        MaxVraissLp,BiaisOuPas,ChiSquared,ChiSquaresQuantile,MethodeNewton, ExoVarj,TriangleUV, DefinitionCartesiennes,CoordPolaires,Parallelogramme,
        ExoParamCD,CbCartTui,CbCartTuii,CbCartTuiii, exercice1A1,exercice1A2,exercice4,DS2010exo1, SuiteUnSurn, SpiraleLimite, IntTrois, CornetGlace,
        Differentielle, CSCiv, CSCvi, CSCii, CSCiii, CSCv, Cardioideexo, DistanceEuclide, LesSpheres, IntervalleUn, DistanceEnsemble, AccumulationIsole,
        MethodeChemin, ExempleArcParam, CourbeRectifiable, SuiteInverseAlterne, CycloideA, Cardioid,  ParamTangente, Polirettangolo,
        RegioniPrimoeSecondoTipo,ExampleIntegration, ExampleIntegrationdeux, ExampleChangementVariables, ArcLongueurFinesse, TangentSegment,
        BoulePtLoin, UneCellule, SenoTopologo, AdhIntFr, AdhIntFrDeux, AdhIntFrTrois, AdhIntFrSix, DeuxCercles, TraceCycloide, QuelCote, Osculateur,
        examssepti,examsseptii,LAfWmaN,YWxOAkh,MCQueGF,PHTVjfk,IWuPxFc,TriangleRectangle,MCKyvdk,senotopologo,TangenteQuestion,TangenteDetail,
        LesSubFigures,NiveauHyperbole,NiveauHyperboleDeux,JGuKEjH
        ]

# Il me semble que la figure IntCourbePolaire est inutile
def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"mes notes de mathématique")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        ProjPoly()
