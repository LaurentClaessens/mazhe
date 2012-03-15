#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys

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
from phystricksBateau import Bateau
from phystricksFonctionXtrois import FonctionXtrois
from phystricksFonctionEtDerive import FonctionEtDerive
from phystricksSurfaceDerive import SurfaceDerive
from phystricksRechercheTangente import RechercheTangente
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
from phystricksExoCourone import ExoCourone
from phystricksIntRectangle import IntRectangle
from phystricksIntTriangle import IntTriangle
from phystricksIntEcourbe import IntEcourbe
from phystricksIntBoutCercle import IntBoutCercle
from phystricksIntDeuxCarres import IntDeuxCarres
from phystricksExPolygone import ExPolygone
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

# Il me semble que la figure IntCourbePolaire est inutile
def AllFigures():
    figures_list=[MoulinEau,IntegraleSimple,ExoMagnetique,CurvilignesPolaires,Refraction,
            MomentForce,Parallelogramme,CouroneExam,SurfacePrimiteGeog,SurfaceEntreCourbes,
            DivergenceTrois,DivergenceDeux,DivergenceUn,ArcCercleAngle,ExoXLVL,Laurin,
            ChampGraviation,FnCosApprox,NiveauHyperbole,Bateau,FonctionXtrois,FonctionEtDerive,
            SurfaceDerive,RechercheTangente,DerivTangente,ExoUnSurxPolaire,DessinExp,DessinLim,
            ExoProjection,ExoPolaire,CoordPolaires,TriangleRectangle,CercleTnu,QCb,
            DefinitionCartesiennes,ProjectionScalaire,CercleTrigono,TgCercleTrigono,
            SurfaceHorizVerti,SurfaceCercle,ExoCourone,IntRectangle,IntTriangle,CoinPasVar,
            IntEcourbe,IntBoutCercle,IntDeuxCarres,ExPolygone,CercleImplicite,QQa,
            ConeRevolution,ChoixInfini,ProjPoly,trigoWedd,DisqueConv,ExempleNonRang,
            ToreRevolution,ExSinLarge,ContourGreen,ContourSqL,ContourTgNDivergence,ratrap,
            MaxVraissLp,BiaisOuPas,ChiSquared,ChiSquaresQuantile,MethodeNewton,
            ExoVarj]


    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"mes notes de mathématique")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        ExoVarj()
