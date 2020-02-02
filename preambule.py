#!/usr/bin/python
# -*- coding: utf-8 -*-

# Permet d'importer des modules dans d'autres dossiers.
from __future__ import absolute_import
# Afin de compiler
import os
import subprocess
# Pour choisir aléatoirement des exercices
import numpy as np
import random

import exosQuatrieme
import exosSeconde



headerBase = r'''\documentclass[a4paper,12pt, answers]{exam}
\usepackage[T1]{fontenc} 
\usepackage{fontspec}
\usepackage[french]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{array}

\usepackage{wrapfig}
\usepackage{adjustbox}
\usepackage{cutwin}
\newlength{\strutheight}
\settoheight{\strutheight}{\strut}


\usepackage{tikz}

\usepackage{pgfplots}

\usetikzlibrary{shapes.arrows}

\usepackage{pst-labo}

\usepackage[left=2cm,right=2cm,top=1cm,bottom=2cm]{geometry}

\setlength{\parindent}{0cm}
\newcommand{\enteteLFM}[1]{
		\begin{minipage}{0.25\textwidth}
		%\includegraphics[width=\textwidth]{logoPDF.pdf}\\
		\includegraphics[width=\textwidth]{Logo.ps}\\
		\end{minipage}%
		\begin{minipage}{0.05\textwidth}
			~
		\end{minipage}%
		\begin{minipage}{0.7\textwidth}
		\begin{flushright}
		\textbf{Nom :} \makebox[0.8\textwidth]{\dotfill} \\
		\textbf{Classe :} \makebox[0.8\textwidth]{\dotfill} \\
		\textbf{Date :} \makebox[0.8\textwidth]{\dotfill} \\
		\end{flushright}
		\end{minipage}
		
  	\hrule%
  	\begin{center} \textbf{\textsf{\Large #1 }} \end{center}\vspace*{-0.12cm}
  		\hrule
  		\vspace*{0.25cm}
	}
	\qformat{\underline{\textbf{Exercice \thequestion : \thequestiontitle}}\\
}

\newcommand{\enteteLFMCompetences}[2]{
		\begin{minipage}{0.25\textwidth}
		%\includegraphics[width=\textwidth]{logoPDF.pdf}\\
		\includegraphics[width=\textwidth]{Logo.ps}\\
		\end{minipage}%
		\begin{minipage}{0.05\textwidth}
			~
		\end{minipage}%
		\begin{minipage}{0.7\textwidth}
		\begin{flushright}
			\begin{tabular}{|l|c|c|}
				\multicolumn{3}{l}{\textbf{Compétences évaluées :}}\\
				\hline
				D1.1 & Écrire. & ~~~\\
				\hline
				D4 & Connaître, restituter et mobiliser des connaissances. & ~~~ \\
				\hline
				D4 & Mener une démarche scientifique, résoudre un problème. & ~~~\\
				\hline
			\end{tabular}
		\end{flushright}
		\end{minipage}
		
		\vspace*{0.25cm}
		\textbf{Nom :} \makebox[0.8\textwidth]{\dotfill} \hfill 				\textbf{#1}....\\
		\vspace*{0.25cm}
  	\hrule%
  	\begin{center} \textbf{\textsf{\Large #2 }} \end{center}\vspace*{-0.12cm}
  		\hrule
  		\vspace*{0.25cm}
	}
	\qformat{\underline{\textbf{Exercice \thequestion : \thequestiontitle}}\\
}

\renewcommand{\thepartno}{\arabic{partno}}
\renewcommand{\partlabel}{\thepartno.}
\renewcommand{\thesubpart}{\alph{subpart}}



% {2} = Cutout starts in row 2
% {0pt} = Cutout is flush left (0pt from left edge)
% {0.50\linewidth} = text covers 0.50\linewidth relative to right margin
% {4} = cutout extends 8 rows

%Commandes pour faire un tableau de compétence sur la droite de la page avec un nombre illimité de compétences.
\makeatletter
\newcommand{\tabComp}[1]{%
	\hfill \begin{tabular}{|c|c|}
		\hline
    	#1 & ~~~\checknextarg
}

\newcommand{\gobblenextarg}[1]{\\
\hline
#1 & ~~~\@ifnextchar\bgroup{
\gobblenextarg
}{\\
\hline
\end{tabular}
}
}

\newcommand{\checknextarg}{
		\@ifnextchar\bgroup{
			\gobblenextarg
			}{\\
    		\hline
    	\end{tabular}
	}
}
\makeatother

\usepackage{framed}

\newcommand{\solPerso}[2]{%
    \ifprintanswers
        #1
    \else
        #2
    \fi
}

\usepackage{siunitx}
\usepackage{amsmath}
\renewcommand{\solutiontitle}{}
'''
headerBase += r'\begin{document}%' + '\n\n'

header = headerBase
headerC = headerBase
# header += r'''\enteteLSMI{\today}{Interrogation n°10 : tableaux de signes : sujet A}%''' + '\n\n'
# headerC += r'''\enteteLSMI{\today}{Correction de l'interrogation n°10 : les tableaux de signes : sujet A}%''' + '\n\n'

footer = r'''\end{questions}
\end{document}'''
main = ''

footerC = r'''\end{questions}
\end{document}'''
mainC = ''


