#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import numpy as np

import exosQuatrieme
import exosSeconde

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
# header += r'''\enteteLSMI{\today}{Interrogation n°10 : tableaux de signes : sujet A}%''' + '\n\n'
# headerC += r'''\enteteLSMI{\today}{Correction de l'interrogation n°10 : les tableaux de signes : sujet A}%''' + '\n\n'

footer = r'''\end{document}'''
main = ''

footerC = r'''\end{document}'''
mainC = ''

# Chapitres 4ème
cosinus = [exosQuatrieme.cosinus1,
           exosQuatrieme.cosinus2,
           exosQuatrieme.cosinus3,
           exosQuatrieme.cosinus4,
           ]
puissances = [exosQuatrieme.puissance1,
              exosQuatrieme.puissance2,
              exosQuatrieme.puissance3,
              ]
equations = [exosQuatrieme.equation1,
             exosQuatrieme.equation2,
             exosQuatrieme.equation3]
pythagore = [exosQuatrieme.pythagore1,
             exosQuatrieme.pythagore2,
             exosQuatrieme.pythagore3,
             exosQuatrieme.pythagore4,
             exosQuatrieme.pythagore5,
             ]
fractions = [exosQuatrieme.fraction1,
             ]

calculLitteral = [exosQuatrieme.doubleDeveloppement,
                  ]


# Chapitres 2nd

fonctionsAffines = [exosSeconde.fonctionsAffineIntersection,
                    ]

tableauDeSigne = [exosSeconde.tableauDeSigneUn1,
                  exosSeconde.tableauDeSigneUn2,
                  exosSeconde.tableauDeSigneUn3,
                  exosSeconde.tableauDeSigneUn4,
                  exosSeconde.tableauDeSigneDeux1,
                  exosSeconde.tableauDeSigneDeux2,
                  exosSeconde.tableauDeSigneDeux3,
                  exosSeconde.tableauDeSigneDeux4,
                  ]
vecteurs = [exosSeconde.vecteursParall1,
            exosSeconde.vecteursParall2,
            exosSeconde.vecteursCalculCoord1,
            exosSeconde.vecteursDroitesColineaires,
            ]

# Niveaux
quatrieme = [cosinus,
             pythagore,
             equations,
             puissances,
             fractions,
             calculLitteral,
             ]

seconde = [tableauDeSigne,
           vecteurs,
           fonctionsAffines,
           ]

niveau = quatrieme

#nombreExercices = 6
nombreDevoirs = 1

for j in range(1,nombreDevoirs+1):
    if j < 10:
        j = str(0) + str(j)
    else:
        j = str(j)
    header = headerBase
    headerC = headerBase
    main = ''
    mainC = ''
    header += r'''\enteteLSMI{}{Interrogation Surprise : sujet n°''' + j + '''}%''' + '\n\n'
    headerC += r'''\enteteLSMI{}{Correction de l'interrogation Surprise : sujet n°''' + j + '''}%''' + '\n\n'
    
    nomFichierExo = 'exercices' + str(j)
    nomFichierCor = 'corrections' + str(j)
    for chapitre in niveau:
        exo = np.random.choice(chapitre)
        main, mainC = exo(main, mainC)

    # for i in range(40):
    #     exo = np.random.choice([exosQuatrieme.calculLitteral])
    #     main, mainC = exo(main, mainC)

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
