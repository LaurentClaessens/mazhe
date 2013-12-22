#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from phystricks import *
import sys


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
        LesSubFigures,NiveauHyperbole,NiveauHyperboleDeux,JGuKEjH,FWJuNhU,QXyVaKD
        ]


def AllFigures():
    tests=main.FigureGenerationSuite(figures_list,first=0,title=u"mes notes de mathématique")
    tests.generate()
    tests.summary()

if __name__=="__main__":
    if "--all" in sys.argv :
        AllFigures()
    else:
        ProjPoly()
