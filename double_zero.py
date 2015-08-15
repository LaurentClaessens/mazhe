#! /usr/bin/env python3
# -*- coding: utf8 -*-

mazhe=open("mazhe.tex",'r').read()

def rename(f1,f2,mazhe):
    text=open(f1,'r').read()
    gf1=f1.replace('.tex',"")
    gf2=f2.replace('.tex',"")
    mazhe=mazhe.replace(gf1,gf2)
    new=open(f2,'w')
    new.write(text)
    new.close()
    return mazhe




file_list=["0010_groupes.tex", "0015_groupes.tex", "0020_StructAnneaux.tex", "0030_StructCorps.tex", "0033_StructCorps.tex", "0035_StructCorps.tex", "0036_StructCorps.tex", "0050_topologie.tex", "0040_topologieR.tex", "0110_espace_vecto_norme.tex", "0113_espace_vecto_norme.tex", "0115_espace_vecto_norme.tex", "0087_VectoMatrice.tex", "0090_EspacesVecto.tex", "0095_EspacesVecto.tex", "0100_representations.tex", "0103_representations.tex", "0105_representations.tex", "0130_Chap_analyse_R.tex", "0135_Chap_analyse_R.tex", "0140_Chap_calcul_differentiel.tex", "0142_Chap_calcul_differentiel.tex", "0143_Chap_calcul_differentiel.tex", "0144_Chap_calcul_differentiel.tex", "0180_suites_series_fonctions.tex", "0181_suites_series_fonctions.tex", "0182_suites_series_fonctions.tex", "0170_Chap_integrales_multiples.tex", "0145_Chap_courbes_parametre.tex", "0210_series_fonctions.tex", "0212_series_fonctions.tex", "0215_series_fonctions.tex", "0190_inversion_locale.tex", "0195_inversion_locale.tex", "0200_Newton.tex", "0230_Hilbert.tex", "0240_analyse_fonctionnelle.tex", "0245_analyse_fonctionnelle.tex", "0250_AnalyseComplexe.tex", "0255_AnalyseComplexe.tex", "0260_Fourier.tex", "0265_Fourier.tex", "0267_distributions.tex", "0270_Equations_diff.tex", "0275_Equations_diff.tex", "0290_vars_al.tex", "0295_vars_al.tex", "0297_vars_al.tex", "0300_statistiques.tex", "0310_Markov.tex", "0320_Martingales.tex", "0330_ProcessusPoisson.tex", "0350_liste_developpements.tex", "0060_mazhe.tex", "0061_mazhe.tex", "0062_mazhe.tex", "0063_mazhe.tex", "0064_mazhe.tex", "0065_helgaLie.tex", "0410_fibre_bundle.tex", "0411_fibre_bundle.tex", "0070_iwasawa.tex", "0076_mazhe.tex", "0430_helga.tex", "0470_algebre.tex", "0471_algebre.tex", "0440_homo.tex", "0442_homo.tex", "0441_homo.tex", "0520_CliffordSpin.tex", "0521_CliffordSpin.tex", "0530_Fibre_QFT.tex", "0550_cstar.tex", "0551_cstar.tex", "0552_cstar.tex", "0560_VN_algebras.tex", "0561_VN_algebras.tex", "0562_VN_algebras.tex", "0563_VN_algebras.tex", "0610_BTZ.tex", "0612_BTZ.tex", "0611_BTZ.tex", "0613_BTZ.tex", "0523_DiracAdS.tex", "0524_DiracAdS.tex", "0640_noncommutative_geometry.tex", "0641_noncommutative_geometry.tex", "0720_matlab.tex", "0450_choses_finales.tex"]


def new_name(f,i):
    fa=str(i)+f[ f.find("_"): ]
    return fa

for i,f in enumerate(file_list):
    nn=new_name(f,i+46)
    print(nn)
    mazhe=rename(f,nn,mazhe)

print(mazhe)
fm=open("mazhe.tex",'w')
fm.write(mazhe)
fm.close()
