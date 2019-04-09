#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import subprocess
import numpy

from exosQuatrieme import *
from exosSeconde import *

headerBase = r'''\documentclass[10pt, a4paper]{article}
\usepackage[utf8x]{inputenc}
\usepackage[french]{babel}
\usepackage[T1]{fontenc}
\usepackage{adjustbox}
\newcounter{nexo}           % déclaration du numéro d'exo
\setcounter{nexo}{0}        % initialisation du numero
\newcommand{\exo}[1]{
  \refstepcounter{nexo} 
  \par{{\section*{Exercice \arabic{nexo} : #1}}}\noindent}
\newcommand{\cor}[1]{
  \refstepcounter{nexo}
  \par{{\section*{Correction \arabic{nexo} : #1}}}\noindent}
\newcommand{\vv}[1]{\overrightarrow{#1}}
\newcommand{\coord}[3]{#1\begin{pmatrix}
  #2 \\
  #3
  \end{pmatrix}}
\newcommand{\coordv}[3]{\vv{#1}\begin{pmatrix}
  #2 \\
  #3
  \end{pmatrix}}
\usepackage{graphicx}
\usepackage{eurosym}
\usepackage{textcomp}
\usepackage{amsmath}
\usepackage{geometry}
\geometry{tmargin=0.6cm,lmargin=1cm,rmargin=1cm,bmargin=1.5cm}
\usepackage{xcolor}
\usepackage{dsfont}
\newcommand{\R}{\mathds {R}}
\usepackage{tikz,tkz-tab}
\usetikzlibrary{shapes.misc}
\tikzset{cross/.style={cross out, draw=red, minimum size=2*(#1-\pgflinewidth), inner sep=0pt, outer sep=0pt},
%default radius will be 1pt. 
cross/.default={1pt}}
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\usepackage{interval}
\setlength\parindent{0pt}
\usepackage{enumitem}
'''
headerBase += r'\input{enteteLSMIsansnomTS}%' + '\n'
headerBase += r'\begin{document}%' + '\n\n'

header = headerBase
headerC = headerBase
header += r'''\enteteLSMI{\today}{Interrogation n°10 : tableaux de signes : sujet A}%''' + '\n\n'
headerC += r'''\enteteLSMI{\today}{Correction de l'interrogation n°10 : les tableaux de signes : sujet A}%''' + '\n\n'
# \input{AlgoEntete}

footer = r'''\end{document}'''
main = ''

footerC = r'''\end{document}'''
mainC = ''


# Chapitres 4ème
cosinus = [cosinus1, cosinus2, cosinus3, cosinus4]
puissances = [puissance1, puissance2, puissance3]
equations = [equation1, equation2, equation3]
pythagore = [pythagore1, pythagore2, pythagore3, pythagore4, pythagore5]
fractions = [fraction1]


# Chapitre 2nd
#tableauDeSigne = [tableauDeSigneUn1, tableauDeSigneUn2, tableauDeSigneUn3, tableauDeSigneUn4, tableauDeSigne2,
#                  tableauDeSigne3, tableauDeSigne4, tableauDeSigne5]
#vecteurs = [vecteurs1, vecteurs2]

# Niveaux
quatrieme = [cosinus, pythagore, equations, puissances, fractions]
#seconde = [tableauDeSigne, vecteurs]

niveau = quatrieme

nombreExercices = 20
nombreDevoirs = 1

for j in range(nombreDevoirs):
    if j < 10:
        j = str(0) + str(j)
    nomFichierExo = 'exercices' + str(j)
    nomFichierCor = 'corrections' + str(j)
    # for i in range(nombreExercices):
    # for chapitre in chapitres:
    #    for i in range(nombreExercices):
    #        chapitre = np.random.choice(niveau)
    #        exo = np.random.choice(chapitre)
    #        for exo in tableauDeSigne:
    #            chapitre = pythagore
    #            exo = tableauDeSigne2
    #        (main, mainC) = exo(main, mainC, correction = True, separes = True)

    for i in range(40):
        exo = np.random.choice([equation2])
        main, mainC = exo(main, mainC)

    #exo = np.random.choice([tableauDeSigneUn1, tableauDeSigneUn2, tableauDeSigneUn3, tableauDeSigneUn4])
    #(main, mainC) = exo(main, mainC)
    #for i in range(3):
    #    main += r'\vspace{10cm}'
    #    exo = np.random.choice([tableauDeSigneDeux1, tableauDeSigneDeux2, tableauDeSigneDeux3, tableauDeSigneDeux4])
    #    (main, mainC) = exo(main, mainC)


    contentExercices = header + main + footer

    with open(nomFichierExo + '.tex', 'w', encoding='utf-8') as f:
        f.write(contentExercices)

    # commandLine =
    subprocess.check_call(['pdflatex', nomFichierExo+'.tex'])
    os.unlink(nomFichierExo+'.aux')
    os.unlink(nomFichierExo+'.log')
    # os.unlink(nomFichierExo+'.tex')

    contentCorrections = headerC + mainC + footerC

    with open(nomFichierCor + '.tex', 'w', encoding='utf-8') as f:
        f.write(contentCorrections)

    # commandLine =
    subprocess.check_call(['pdflatex', nomFichierCor + '.tex'])

    os.unlink(nomFichierCor+'.aux')
    os.unlink(nomFichierCor+'.log')
    # os.unlink(nomFichierCor+'.tex')
