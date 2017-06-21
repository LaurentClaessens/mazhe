#! /usr/bin/sage -python
# -*- coding: utf8 -*-

# The 'recall' files are in the directory <mazhe>/src_phystricks
# The 'pstricks' files are in directory : <mazhe>/auto/pictures_tex

from phystricks import *
import sys

from phystricksCWKJooppMsZXjw import CWKJooppMsZXjw
from phystricksDNRRooJWRHgOCw import DNRRooJWRHgOCw
from phystricksDNHRooqGtffLkd import DNHRooqGtffLkd
from phystricksXOLBooGcrjiwoU import XOLBooGcrjiwoU
from phystricksGYODoojTiGZSkJ import GYODoojTiGZSkJ
from phystricksEELKooMwkockxB import EELKooMwkockxB
from phystricksUCDQooMCxpDszQ import UCDQooMCxpDszQ
from phystricksIOCTooePeHGCXH import IOCTooePeHGCXH
from phystricksSJAWooRDGzIkrj import SJAWooRDGzIkrj
from phystricksLMHMooCscXNNdU import LMHMooCscXNNdU
from phystricksYQIDooBqpAdbIM import YQIDooBqpAdbIM
from phystricksZOCNoowrfvQXsr import ZOCNoowrfvQXsr
from phystricksTIMYoochXZZNGP import TIMYoochXZZNGP
from phystricksQSKDooujUbDCsu import QSKDooujUbDCsu
from phystricksPLTWoocPNeiZir import PLTWoocPNeiZir
from phystricksDGFSooWgbuuMoB import DGFSooWgbuuMoB
from phystricksFCUEooTpEPFoeQ import FCUEooTpEPFoeQ
from phystricksERPMooZibfNOiU import ERPMooZibfNOiU
from phystricksOQTEoodIwAPfZE import OQTEoodIwAPfZE
from phystricksQMWKooRRulrgcH import QMWKooRRulrgcH
from phystricksKKJAooubQzgBgP import KKJAooubQzgBgP
from phystricksSYNKooZBuEWsWw import SYNKooZBuEWsWw
from phystricksUMEBooVTMyfD import UMEBooVTMyfD
from phystricksUIEHooSlbzIJ import UIEHooSlbzIJ
from phystricksYYECooQlnKtD import YYECooQlnKtD
from phystricksUGCFooQoCihh import UGCFooQoCihh
from phystricksWIRAooTCcpOV import WIRAooTCcpOV
from phystricksHFAYooOrfMAA import HFAYooOrfMAA
from phystricksVBOIooRHhKOH import VBOIooRHhKOH
from phystricksGWOYooRxHKSm import GWOYooRxHKSm
from phystricksNOCGooYRHLCn import NOCGooYRHLCn
from phystricksJWINooSfKCeA import JWINooSfKCeA
from phystricksBNHLooLDxdPA import BNHLooLDxdPA
from phystricksMBFDooRFPyNW import CQIXooBEDnfK
from phystricksMBFDooRFPyNW import KGQXooZFNVnW
from phystricksSQNPooPTrLRQ import SQNPooPTrLRQ
from phystricksGVDJooYzMxLW import GVDJooYzMxLW  
from phystricksQOBAooZZZOrl import QOBAooZZZOrl
from phystricksVSZRooRWgUGu import VSZRooRWgUGu
from phystricksDDCTooYscVzA import DDCTooYscVzA
from phystricksLLVMooWOkvAB import LLVMooWOkvAB
from phystricksVDFMooHMmFZr import VDFMooHMmFZr
from phystricksUUNEooCNVOOs import UUNEooCNVOOs
from phystricksROAOooPgUZIt import ROAOooPgUZIt
from phystricksYHJYooTEXLLn import YHJYooTEXLLn
from phystricksPONXooXYjEot import PONXooXYjEot
from phystricksVWFLooPSrOqz import VWFLooPSrOqz
from phystricksCMMAooQegASg import CMMAooQegASg
from phystricksHCJPooHsaTgI import HCJPooHsaTgI
from phystricksCURGooXvruWV import CURGooXvruWV
from phystricksVNBGooSqMsGU import VNBGooSqMsGU
from phystricksKKLooMbjxdI import KKLooMbjxdI
from phystricksBEHTooWsdrys import BEHTooWsdrys
from phystricksHGQPooKrRtAN import HGQPooKrRtAN
from phystricksZGUDooEsqCWQ import ZGUDooEsqCWQ
from phystricksYQVHooYsGLHQ import YQVHooYsGLHQ
from phystricksTKXZooLwXzjS import TKXZooLwXzjS
from phystricksAMDUooZZUOqa import AMDUooZZUOqa
from phystricksLYORooNKDHqt import LYORooNKDHqt
from phystricksASHYooUVHkak import ASHYooUVHkak
from phystricksFNBQooYgkAmS import FNBQooYgkAmS
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
from phystricksParallelogrammeOM import ParallelogrammeOM
from phystricksDivergenceTrois import DivergenceTrois
from phystricksDivergenceDeux import DivergenceDeux
from phystricksDivergenceUn import DivergenceUn
from phystricksChampGraviation import ChampGraviation
from phystricksFnCosApprox import FnCosApprox
from phystricksNiveauHyperbole import NiveauHyperbole
from phystricksNiveauHyperbole import NiveauHyperboleDeux
from phystricksBateau import Bateau
from phystricksFonctionXtroisOM import FonctionXtroisOM
from phystricksFonctionEtDeriveOM import FonctionEtDeriveOM
from phystricksRechercheTangente import VGZooJnvvZc
from phystricksDerivTangenteOM import DerivTangenteOM
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
from phystricksBQXKooPqSEMN import BQXKooPqSEMN
from phystricksooIHLPooKLIxcH import ooIHLPooKLIxcH
from phystricksUEGEooHEDIJVPn import UEGEooHEDIJVPn


# De analyseCTU
from phystricksCFMooGzvfRP import CFMooGzvfRP
from phystricksHLJooGDZnqF import HLJooGDZnqF
from phystricksGCNooKEbjWB import GCNooKEbjWB
from phystricksLBGooAdteCt import LBGooAdteCt
from phystricksDZVooQZLUtf import DZVooQZLUtf
from phystricksWJBooMTAhtl import WJBooMTAhtl
from phystricksWUYooCISzeB import WUYooCISzeB
from phystricksRPNooQXxpZZ import RPNooQXxpZZ
from phystricksXJMooCQTlNL import XJMooCQTlNL
from phystricksNWDooOObSHB import NWDooOObSHB
from phystricksJSLooFJWXtB import JSLooFJWXtB
from phystricksUQZooGFLNEq import UQZooGFLNEq
from phystricksKKRooHseDzC import KKRooHseDzC
from phystricksUNVooMsXxHa import UNVooMsXxHa
from phystricksGMIooJvcCXg import GMIooJvcCXg
from phystricksJJAooWpimYW import JJAooWpimYW
from phystricksFGRooDhFkch import FGRooDhFkch
from phystricksTWHooJjXEtS import TWHooJjXEtS
from phystricksTVXooWoKkqV import TVXooWoKkqV
from phystricksSBTooEasQsT import SBTooEasQsT
from phystricksBIFooDsvVHb import BIFooDsvVHb
from phystricksCELooGVvzMc import CELooGVvzMc
from phystricksPVJooJDyNAg import PVJooJDyNAg
from phystricksVANooZowSyO import VANooZowSyO
from phystricksXTGooSFFtPu import XTGooSFFtPu

figures_list_1=[]
figures_list_2=[]
figures_list_3=[]

def append_picture(fun,number):
    figures_list_1.append(fun)
    if number>=2 :
        figures_list_2.append(fun)
    if number>=3 :
        figures_list_3.append(fun)


append_picture(UUNEooCNVOOs,3)
append_picture(NOCGooYRHLCn,3)
append_picture(YQIDooBqpAdbIM,3)
append_picture(SurfacePrimiteGeog,2)
append_picture(XOLBooGcrjiwoU,2)
append_picture(DynkinrjbHIu,2)
append_picture(HCJPooHsaTgI,2)
append_picture(LMHMooCscXNNdU,2)
append_picture(IntervalleUn,2)
append_picture(UGCFooQoCihh,2)
append_picture(UEGEooHEDIJVPn,2)
append_picture(BiaisOuPas,2)
append_picture(DisqueConv,2)
append_picture(VBOIooRHhKOH,2)
append_picture(GWOYooRxHKSm,2)
append_picture(ExoUnSurxPolaire,2)
append_picture(QPcdHwP,2)
append_picture(LBGooAdteCt,2)
append_picture(CbCartTuii,2)
append_picture(CercleTrigono,2)
append_picture(ExoCUd,2)
append_picture(AMDUooZZUOqa,2)
append_picture(ExoParamCD,2)
append_picture(XJMooCQTlNL,2)
append_picture(Laurin,2)
append_picture(DTIYKkP,2)
append_picture(UYJooCWjLgK,2)
append_picture(Grapheunsurunmoinsx,2)
append_picture(SuiteInverseAlterne,2)
append_picture(HFAYooOrfMAA,2)
append_picture(HLJooGDZnqF,2)
append_picture(SolsSinpA,2)
append_picture(trigoWedd,2)
append_picture(BoulePtLoin,2)
append_picture(Mantisse,2)
append_picture(TgCercleTrigono,2)
append_picture(SJAWooRDGzIkrj,2)
append_picture(UMEBooVTMyfD,2)
append_picture(GBnUivi,2)
append_picture(SurfaceEntreCourbes,2)
append_picture(ProjectionScalaire,2)
append_picture(AdhIntFr,2)
append_picture(Cardioideexo,2)
append_picture(RPNooQXxpZZ,2)
append_picture(CSCv,2)
append_picture(QIZooQNQSJj,2)
append_picture(IntTrois,2)
append_picture(examssepti,2)
append_picture(FnCosApprox,2)
append_picture(Refraction,2)
append_picture(MCQueGF,2)
append_picture(LLVMooWOkvAB,2)
append_picture(CSCii,2)
append_picture(CheminFresnel,2)
append_picture(VSZRooRWgUGu,2)
append_picture(BIFooDsvVHb,2)
append_picture(ADUGmRRA,2)
append_picture(UneCellule,2)
append_picture(IntEcourbe,2)
append_picture(IOCTooePeHGCXH,2)
append_picture(QSKDooujUbDCsu,2)
append_picture(NiveauHyperboleDeux,2)
append_picture(CSCiv,2)
append_picture(ConeRevolution,2)
append_picture(DNRRooJWRHgOCw,2)
append_picture(CFMooGzvfRP,2)
append_picture(AccumulationIsole,2)
append_picture(LAfWmaN,2)
append_picture(TZCISko,2)
append_picture(DefinitionCartesiennes,2)
append_picture(DistanceEuclide,2)
append_picture(ASHYooUVHkak,2)
append_picture(GVDJooYzMxLW,2)
append_picture(CercleTnu,2)
append_picture(IsomCarre,2)
append_picture(VANooZowSyO,2)
append_picture(CSCiii,2)
append_picture(DNHRooqGtffLkd,2)
append_picture(TracerUn,2)
append_picture(DynkinpWjUbE,2)
append_picture(AdhIntFrTrois,2)
append_picture(VNBGooSqMsGU,2)
append_picture(GMIooJvcCXg,2)
append_picture(ADUGmRRB,2)
append_picture(UnSurxInt,2)
append_picture(MNICGhR,2)
append_picture(FNBQooYgkAmS,2)
append_picture(Trajs,2)
append_picture(ExampleIntegration,2)
append_picture(KGQXooZFNVnW,2)
append_picture(XTGooSFFtPu,2)
append_picture(CurvilignesPolaires,2)
append_picture(JWINooSfKCeA,2)
append_picture(IntBoutCercle,2)
append_picture(senotopologo,2)
append_picture(ratrap,2)
append_picture(CSCvi,2)
append_picture(IYAvSvI,2)
append_picture(FGWjJBX,2)
append_picture(ExSinLarge,2)
append_picture(KKLooMbjxdI,2)
append_picture(SYNKooZBuEWsWw,2)
append_picture(ExempleArcParam,2)
append_picture(CWKJooppMsZXjw,2)
append_picture(YHJYooTEXLLn,2)
append_picture(TIMYoochXZZNGP,2)
append_picture(NWDooOObSHB,2)
append_picture(FGRooDhFkch,2)
append_picture(ToreRevolution,2)
append_picture(BNHLooLDxdPA,2)
append_picture(ChoixInfini,2)
append_picture(ExoPolaire,2)
append_picture(Polirettangolo,2)
append_picture(EHDooGDwfjC,2)
append_picture(ROAOooPgUZIt,2)
append_picture(KKRooHseDzC,2)
append_picture(CourbeRectifiable,2)
append_picture(SuiteUnSurn,2)
append_picture(ExoXLVL,2)
append_picture(FCUEooTpEPFoeQ,2)
append_picture(TGdUoZR,2)
append_picture(PartieEntiere,2)
append_picture(WJBooMTAhtl,2)
append_picture(PHTVjfk,2)
append_picture(RLuqsrr,2)
append_picture(DessinLim,2)
append_picture(ALIzHFm,2)
append_picture(MomentForce,2)
append_picture(LEJNDxI,2)
append_picture(NiveauHyperbole,2)
append_picture(WIRAooTCcpOV,2)
append_picture(AdhIntFrDeux,2)
append_picture(YYECooQlnKtD,2)
append_picture(GCNooKEbjWB,2)
append_picture(ExoVarj,2)
append_picture(AdhIntFrSix,2)
append_picture(PLTWoocPNeiZir,2)
append_picture(TVXooWoKkqV,2)
append_picture(MCKyvdk,2)
append_picture(AireParabole,2)
append_picture(SFdgHdO,2)
append_picture(WHCooNZAmYB,2)
append_picture(Bateau,2)
append_picture(RegioniPrimoeSecondoTipo,2)
append_picture(ExoMagnetique,2)
append_picture(CouroneExam,2)
append_picture(WUYooCISzeB,2)
append_picture(VWFLooPSrOqz,2)
append_picture(ChiSquared,2)
append_picture(QOBAooZZZOrl,2)
append_picture(ParallelogrammeOM,2)
append_picture(SurfaceHorizVerti,2)
append_picture(RQsQKTl,2)
append_picture(HNxitLj,2)
append_picture(FonctionXtroisOM,2)
append_picture(OQTEoodIwAPfZE,2)
append_picture(IntTriangle,2)
append_picture(LesSpheres,2)
append_picture(JSLooFJWXtB,2)
append_picture(RGjjpwF,2)
append_picture(UNVooMsXxHa,2)
append_picture(CbCartTui,2)
append_picture(CURGooXvruWV,2)
append_picture(DeuxCercles,2)
append_picture(JJAooWpimYW,2)
append_picture(UZGooBzlYxr,2)
append_picture(QCb,2)
append_picture(TriangleUV,2)
append_picture(FonctionEtDeriveOM,2)
append_picture(ProjPoly,2)
append_picture(TWHooJjXEtS,2)
append_picture(ContourSqL,2)
append_picture(IntegraleSimple,2)
append_picture(HGQPooKrRtAN,2)
append_picture(YWxOAkh,2)
append_picture(CornetGlace,2)
append_picture(QMWKooRRulrgcH,2)
append_picture(CoordPolaires,2)
append_picture(MethodeChemin,2)
append_picture(MaxVraissLp,2)
append_picture(CycloideA,2)
append_picture(PVJooJDyNAg,2)
append_picture(DZVooQZLUtf,2)
append_picture(UQZooGFLNEq,2)
append_picture(SBTooEasQsT,2)
append_picture(AIFsOQO,2)
append_picture(QuelCote,2)
append_picture(ACUooQwcDMZ,2)
append_picture(HasseAGdfdy,2)
append_picture(NEtAchr,2)
append_picture(CbCartTuiii,2)
append_picture(UIEHooSlbzIJ,2)
append_picture(STdyNTH,2)
append_picture(ExoProjection,2)
append_picture(ADUGmRRC,2)
append_picture(DerivTangenteOM,2)
append_picture(DistanceEnsemble,2)
append_picture(examsseptii,2)
append_picture(IWuPxFc,2)
append_picture(DynkinqlgIQl,2)
append_picture(FWJuNhU,2)
append_picture(QXyVaKD,2)
append_picture(SolsEqDiffSin,2)
append_picture(ExampleIntegrationdeux,2)
append_picture(CQIXooBEDnfK,2)
append_picture(ChiSquaresQuantile,2)
append_picture(MethodeNewton,2)
append_picture(CELooGVvzMc,2)
append_picture(ParamTangente,2)
append_picture(KKJAooubQzgBgP,2)
append_picture(IntRectangle,2)
append_picture(BQXKooPqSEMN,2)
append_picture(EJRsWXw,2)
append_picture(CercleImplicite,2)
append_picture(ZTTooXtHkci,2)
append_picture(EELKooMwkockxB,2)
append_picture(GYODoojTiGZSkJ,2)
append_picture(ERPMooZibfNOiU,2)
append_picture(TriangleRectangle,2)
append_picture(ExPolygone,2)
append_picture(CoinPasVar,2)
append_picture(DynkinNUtPJx,2)
append_picture(Differentielle,2)
append_picture(ooIHLPooKLIxcH,2)
append_picture(TangentSegment,2)
append_picture(PONXooXYjEot,2)

append_picture(FXVooJYAfif,1)
append_picture(VGZooJnvvZc,2)
append_picture(LYORooNKDHqt,2)
append_picture(TKXZooLwXzjS,1)
append_picture(YQVHooYsGLHQ,1)
append_picture(ZGUDooEsqCWQ,1)
append_picture(CMMAooQegASg,1)
append_picture(VDFMooHMmFZr,1)
append_picture(DDCTooYscVzA,1)
append_picture(SQNPooPTrLRQ,1)
append_picture(BEHTooWsdrys,1)
append_picture(MoulinEau,1)
append_picture(DivergenceTrois,1)
append_picture(DivergenceDeux,1)
append_picture(DivergenceUn,1)
append_picture(ChampGraviation,1)
append_picture(SurfaceCercle,1)
append_picture(KScolorD,1)
append_picture(IntDeuxCarres,1)
append_picture(QQa,1)
append_picture(ExempleNonRang,1)
append_picture(ContourGreen,1)
append_picture(ContourTgNDivergence,1)
append_picture(SpiraleLimite,1)
append_picture(Cardioid,1)
append_picture(ArcLongueurFinesse,1)
append_picture(SenoTopologo,1)
append_picture(TraceCycloide,2)
append_picture(Osculateur,1)
append_picture(JGuKEjH,1)
append_picture(ExerciceGraphesbis,2)
append_picture(DGFSooWgbuuMoB,1)
append_picture(ZOCNoowrfvQXsr,1)
append_picture(UCDQooMCxpDszQ,1)

"""
append_picture(<++>,1)
append_picture(<++>,1)
append_picture(<++>,1)
"""

def AllFigures():
    figures_list=figures_list_1
    if "--pass-number=2" in sys.argv :
        figures_list=figures_list_2
    if "--pass-number=3" in sys.argv :
        figures_list=figures_list_3

    tests=FigureGenerationSuite(figures_list,first=0,title=u"(almost) everything I know in mathematics and physics")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        pass
