#!/usr/bin/python
# -*- coding: utf-8 -*-

# Permet d'importer des modules dans d'autres dossiers.
from __future__ import absolute_import
# Afin de compiler
import os
import subprocess
# Pour choisir aléatoirement des exercices
import numpy as np

import exosQuatrieme
import exosSeconde
import seconde.tableauxDeSignes.problemesSimples
import seconde.probas.problemes

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