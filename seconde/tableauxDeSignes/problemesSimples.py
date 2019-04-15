#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
import fonctionsSimplifiantes
from fonctionsSimplifiantes import signT
from seconde.tableauxDeSignes.traceurDeTableau import tableauSigneAffine
from seconde.tableauxDeSignes.traceurDeTableau import tableauSigne


def tableauDeSigneUn1(fileExercices, fileCorrections):
    """Tableau de signe simple avec une seule expression du premier degré ax+b <= 0"""
    a, b = -1, -1
    
    while a in [-1, 0, 1] or b == 0 or -b/a != round(-b/a, 3):
        a = random.randint(-6, 6)
        b = random.randint(-6, 6)
    
    posNeg = 'négative'
    negPos = 'positive'
    posNegM = 'négatif'
    if a > 0:
        posNeg = 'positive'
        negPos = 'négative'
        posNegM = 'positif'
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%' + '\n'
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = \{a}x \{signT(b)} \{abs(b)}$%
\item En déduire les valeurs pour lesquelles $f(x) \leq 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $f(x) = 0$ est \{-b/a}.\\%
Le coefficient devant $x$ est \{posNegM}, donc la fonction sera \{posNeg} après \{-b/a}
et \{negPos} avant.\\
On a donc le tableau de signes suivant :\\%
'''
    mainC += tableauSigneAffine(a, b)
    if a > 0:
        mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open  left]{-\infty}{\{-b/a}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open right]{\{-b/a}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneUn2(fileExercices, fileCorrections):
    """Tableau de signe simple avec une seule expression du premier degré ax+b < 0"""
    
    VAnnul = 1 / 3
    a, b = 0, 0
    
    while VAnnul != round(VAnnul, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        bAbs = abs(b)
        VAnnul = -b / a
    
    posNeg = 'négative'
    negPos = 'positive'
    posNegM = 'négatif'
    if a > 0:
        posNeg = 'positive'
        negPos = 'négative'
        posNegM = 'négatif'
    
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%' + '\n'
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = \{a}x \{signB} \{bAbs}$%
\item En déduire les valeurs pour lesquelles $f(x) < 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $f(x) = 0$ est \{VAnnul}.\\%
Le coefficient devant $x$ est \{posNegM}, donc la fonction sera \{posNeg} après \{VAnnul}
et \{negPos} avant.\\
On a donc le tableau de signes suivant :\\%
'''
    mainC += tableauSigneAffine(a, b)
    if a > 0:
        mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneUn3(fileExercices, fileCorrections):
    """Tableau de signe simple avec une seule expression du premier degré ax+b >= 0"""
    
    VAnnul = 1 / 3
    a, b = 0, 0
    
    while VAnnul != round(VAnnul, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        bAbs = abs(b)
        VAnnul = -b / a
    
    posNeg = 'négative'
    negPos = 'positive'
    posNegM = 'négatif'
    if a > 0:
        posNeg = 'positive'
        negPos = 'négative'
        posNegM = 'positif'
    
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%' + '\n'
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = \{a}x \{signB} \{bAbs}$%
\item En déduire les valeurs pour lesquelles $f(x) \geq 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $f(x) = 0$ est \{VAnnul}.\\%
Le coefficient devant $x$ est \{posNegM}, donc la fonction sera \{posNeg} après \{VAnnul}
et \{negPos} avant.\\
On a donc le tableau de signes suivant :\%
'''
    mainC += tableauSigneAffine(a, b)
    if a < 0:
        mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open  left]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open right]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneUn4(fileExercices, fileCorrections):
    """Tableau de signe simple avec une seule expression du premier degré ax+b > 0"""
    
    VAnnul = 1 / 3
    a, b = 0, 0
    
    while VAnnul != round(VAnnul, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        bAbs = abs(b)
        VAnnul = -b / a
    
    posNeg = 'négative'
    negPos = 'positive'
    posNegM = 'négatif'
    if a > 0:
        posNeg = 'positive'
        negPos = 'négative'
        posNegM = 'positif'
    
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%' + '\n'
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = \{a}x \{signB} \{bAbs}$%
\item En déduire les valeurs pour lesquelles $f(x) > 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $f(x) = 0$ est \{VAnnul}.\\%
Le coefficient devant $x$ est \{posNegM}, donc la fonction sera \{posNeg} après \{VAnnul}
et \{negPos} avant.\\
On a donc le tableau de signes suivant :\%
'''
    mainC += tableauSigneAffine(a, b)
    if a < 0:
        mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneDeux1(fileExercices, fileCorrections):
    """Tableau de signe pour une expression du second degré
    (produit de deux expressions du premier degré). f(x)<=0"""
    
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = ' - ', ' - '
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = random.randint(2, 6)
        c2 = random.randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = random.randint(1, 6)
        d2 = random.randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
    if b > 0:
        signB = ' + '
    if d > 0:
        signD = ' + '
    
    absB = abs(b)
    absD = abs(d)
    
    posNegA = 'négative'
    negPosA = 'positive'
    posNegMA = 'négatif'
    if a > 0:
        posNegA = 'positive'
        negPosA = 'négative'
        posNegMA = 'positif'
    
    posNegC = 'négative'
    negPosC = 'positive'
    posNegMC = 'négatif'
    if c > 0:
        posNegC = 'positive'
        negPosC = 'négative'
        posNegMC = 'positif'
    
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    if c > 0:
        signC = ' + '
        signMC = ' - '
    else:
        signC = ' - '
        signMC = ' + '
    if signA == signC:
        signFD = ' + '
        signFM = ' - '
    else:
        signFD = ' - '
        signFM = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = (\{a}x \{signB} \{absB})(\{c} x \{signD}
\{absD})$%
\item En déduire les valeurs pour lesquelles $f(x) \leq 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $\{a} x \{signB} \{absB} = 0$ est \{VAnnul1}.\\%
Le coefficient devant $x$ est \{posNegMA}, donc $\{a} x \{signB} \{absB}$ sera \{posNegA} après \{VAnnul1}
et \{negPosA} avant.\\%

La valeur de $x$ pour laquelle $\{c} x \{signD} \{absD} = 0$ est \{VAnnul2}.\\%
Le coefficient devant $x$ est \{posNegMC}, donc $\{c} x \{signD} \{absD}$ sera \{posNegC} après \{VAnnul2}
et \{negPosC} avant.\\%

On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
'''
    if VAnnul1 < VAnnul2:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $\{VAnnul2}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, t,\{signA}}%
\tkzTabLine{, \{signMC}, t, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c < 0:
            mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour
$x\in\interval[open  left]{-\infty}{\{VAnnul1}} \cup \interval[open  right]{\{VAnnul2}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour
$x\in\interval{\{VAnnul1}}{\{VAnnul2}}$%
'''
    elif VAnnul2 < VAnnul1:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul2}$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, t, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z, \{signC}, t,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c < 0:
            mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour
$x\in\interval[open  left]{-\infty}{\{VAnnul2}} \cup \interval[open  right]{\{VAnnul1}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval{\{VAnnul1}}{\{VAnnul2}}$%
'''
    
    else:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a}x\{signB}\{absB}$ /1,
$\{c}x\{signD}\{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if signFD == ' - ':
            mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x\in \R$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x=\{VAnnul1}$%
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneDeux2(fileExercices, fileCorrections):
    """Tableau de signe pour une expression du second degré
    (produit de deux expressions du premier degré). f(x)<0"""
    
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = ' - ', ' - '
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = random.randint(2, 6)
        c2 = random.randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = random.randint(1, 6)
        d2 = random.randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
    if b > 0:
        signB = ' + '
    if d > 0:
        signD = ' + '
    
    absB = abs(b)
    absD = abs(d)
    
    posNegA = 'négative'
    negPosA = 'positive'
    posNegMA = 'négatif'
    if a > 0:
        posNegA = 'positive'
        negPosA = 'négative'
        posNegMA = 'positif'
    
    posNegC = 'négative'
    negPosC = 'positive'
    posNegMC = 'négatif'
    if c > 0:
        posNegC = 'positive'
        negPosC = 'négative'
        posNegMC = 'positif'
    
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    if c > 0:
        signC = ' + '
        signMC = ' - '
    else:
        signC = ' - '
        signMC = ' + '
    if signA == signC:
        signFD = ' + '
        signFM = ' - '
    else:
        signFD = ' - '
        signFM = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = (\{a}x \{signB} \{absB})(\{c} x \{signD}
\{absD})$%
\item En déduire les valeurs pour lesquelles $f(x) < 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $\{a} x \{signB} \{absB} = 0$ est \{VAnnul1}.\\%
Le coefficient devant $x$ est \{posNegMA}, donc $\{a} x \{signB} \{absB}$ sera \{posNegA} après \{VAnnul1}
et \{negPosA} avant.\\%

La valeur de $x$ pour laquelle $\{c} x \{signD} \{absD} = 0$ est \{VAnnul2}.\\%
Le coefficient devant $x$ est \{posNegMC}, donc $\{c} x \{signD} \{absD}$ sera \{posNegC} après \{VAnnul2}
et \{negPosC} avant.\\%

On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
'''
    if VAnnul1 < VAnnul2:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $\{VAnnul2}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, t,\{signA}}%
\tkzTabLine{, \{signMC}, t, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c < 0:
            mainC += r'''\item On peut en déduire que $f(x) < 0$ pour
$x\in\interval[open]{-\infty}{\{VAnnul1}} \cup \interval[open]{\{VAnnul2}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) < 0$ pour
$x\in\interval[open]{\{VAnnul1}}{\{VAnnul2}}$%
'''
    elif VAnnul2 < VAnnul1:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul2}$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, t, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z, \{signC}, t,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c < 0:
            mainC += r'''\item On peut en déduire que $f(x) < 0$ pour
$x\in\interval[open]{-\infty}{\{VAnnul2}} \cup \interval[open]{\{VAnnul1}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{\{VAnnul2}}{\{VAnnul1}}$%
'''
    
    else:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a}x\{signB}\{absB}$ /1,
$\{c}x\{signD}\{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if signFD == ' - ':
            mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x\neq \{VAnnul1}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x=\varnothing$%
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneDeux3(fileExercices, fileCorrections):
    """Tableau de signe pour une expression du second degré
    (produit de deux expressions du premier degré). f(x)>=0"""
    
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = ' - ', ' - '
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = random.randint(2, 6)
        c2 = random.randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = random.randint(1, 6)
        d2 = random.randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
    if b > 0:
        signB = ' + '
    if d > 0:
        signD = ' + '
    
    absB = abs(b)
    absD = abs(d)
    
    posNegA = 'négative'
    negPosA = 'positive'
    posNegMA = 'négatif'
    if a > 0:
        posNegA = 'positive'
        negPosA = 'négative'
        posNegMA = 'positif'
    
    posNegC = 'négative'
    negPosC = 'positive'
    posNegMC = 'négatif'
    if c > 0:
        posNegC = 'positive'
        negPosC = 'négative'
        posNegMC = 'positif'
    
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    if c > 0:
        signC = ' + '
        signMC = ' - '
    else:
        signC = ' - '
        signMC = ' + '
    if signA == signC:
        signFD = ' + '
        signFM = ' - '
    else:
        signFD = ' - '
        signFM = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = (\{a}x \{signB} \{absB})(\{c} x \{signD}
\{absD})$%
\item En déduire les valeurs pour lesquelles $f(x) \geq 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $\{a} x \{signB} \{absB} = 0$ est \{VAnnul1}.\\%
Le coefficient devant $x$ est \{posNegMA}, donc $\{a} x \{signB} \{absB}$ sera \{posNegA} après \{VAnnul1}
et \{negPosA} avant.\\%

La valeur de $x$ pour laquelle $\{c} x \{signD} \{absD} = 0$ est \{VAnnul2}.\\%
Le coefficient devant $x$ est \{posNegMC}, donc $\{c} x \{signD} \{absD}$ sera \{posNegC} après \{VAnnul2}
et \{negPosC} avant.\\%

On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
'''
    if VAnnul1 < VAnnul2:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $\{VAnnul2}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, t,\{signA}}%
\tkzTabLine{, \{signMC}, t, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c > 0:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour
$x\in\interval[open  left]{-\infty}{\{VAnnul1}} \cup \interval[open  right]{\{VAnnul2}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour
$x\in\interval{\{VAnnul1}}{\{VAnnul2}}$%
'''
    elif VAnnul2 < VAnnul1:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul2}$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, t, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z, \{signC}, t,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c > 0:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour
$x\in\interval[open  left]{-\infty}{\{VAnnul2}} \cup \interval[open  right]{\{VAnnul1}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval{\{VAnnul1}}{\{VAnnul2}}$%
'''
    
    else:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a}x\{signB}\{absB}$ /1,
$\{c}x\{signD}\{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c > 0:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in \R$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x=\{VAnnul1}$%
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneDeux4(fileExercices, fileCorrections):
    """Tableau de signe pour une expression du second degré
    produit de deux expressions du premier degré). f(x)>0"""
    
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = ' - ', ' - '
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = random.randint(2, 6)
        c2 = random.randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = random.randint(1, 6)
        d2 = random.randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
    if b > 0:
        signB = ' + '
    if d > 0:
        signD = ' + '
    
    absB = abs(b)
    absD = abs(d)
    
    posNegA = 'négative'
    negPosA = 'positive'
    posNegMA = 'négatif'
    if a > 0:
        posNegA = 'positive'
        negPosA = 'négative'
        posNegMA = 'positif'
    
    posNegC = 'négative'
    negPosC = 'positive'
    posNegMC = 'négatif'
    if c > 0:
        posNegC = 'positive'
        negPosC = 'négative'
        posNegMC = 'positif'
    
    if a > 0:
        signA = ' + '
        signMA = ' - '
    else:
        signA = ' - '
        signMA = ' + '
    if c > 0:
        signC = ' + '
        signMC = ' - '
    else:
        signC = ' - '
        signMC = ' + '
    if signA == signC:
        signFD = ' + '
        signFM = ' - '
    else:
        signFD = ' - '
        signFM = ' + '
    
    main = r'''\exo{Tableau de Signes}%
\begin{enumerate}%
\item Tracez le tableau de signes de la fonction $f$ définie par : $f(x) = (\{a}x \{signB} \{absB})(\{c} x \{signD}
\{absD})$%
\item En déduire les valeurs pour lesquelles $f(x) > 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $\{a} x \{signB} \{absB} = 0$ est \{VAnnul1}.\\%
Le coefficient devant $x$ est \{posNegMA}, donc $\{a} x \{signB} \{absB}$ sera \{posNegA} après \{VAnnul1}
et \{negPosA} avant.\\%

La valeur de $x$ pour laquelle $\{c} x \{signD} \{absD} = 0$ est \{VAnnul2}.\\%
Le coefficient devant $x$ est \{posNegMC}, donc $\{c} x \{signD} \{absD}$ sera \{posNegC} après \{VAnnul2}
et \{negPosC} avant.\\%

On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
'''
    if VAnnul1 < VAnnul2:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $\{VAnnul2}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, t,\{signA}}%
\tkzTabLine{, \{signMC}, t, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c > 0:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour
$x\in\interval[open]{-\infty}{\{VAnnul1}} \cup \interval[open]{\{VAnnul2}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour
$x\in\interval[open]{\{VAnnul1}}{\{VAnnul2}}$%
'''
    elif VAnnul2 < VAnnul1:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a} x \{signB} \{absB}$ /1,
$\{c} x \{signD} \{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul2}$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, t, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z, \{signC}, t,\{signC}}%
\tkzTabLine{, \{signFD}, z, \{signFM}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c > 0:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour
$x\in\interval[open]{-\infty}{\{VAnnul2}} \cup \interval[open]{\{VAnnul1}}{+\infty}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{\{VAnnul1}}{\{VAnnul2}}$%
'''
    
    else:
        mainC += r'''\tkzTabInit{$x$ / 1 , $\{a}x\{signB}\{absB}$ /1,
$\{c}x\{signD}\{absD}$ /1, $f(x)$ / 1}{$-\infty$, $\{VAnnul1}$, $+\infty$}%
\tkzTabLine{, \{signMA}, z,\{signA}}%
\tkzTabLine{, \{signMC}, z,\{signC}}%
\tkzTabLine{, \{signFD}, z,\{signFD}}%
\end{tikzpicture}%
\end{center}%
'''
        if a * c > 0:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\neq \{VAnnul1}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x=\emptyset$%
'''
    mainC += r'''\end{enumerate}%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneBasique(fileExercices, fileCorrections):
    main = r'''Tracez le tableau de signe de :
'''
    # mainC = tableauSigne(3, [(2, 3), (-2, 2), (1, -1), (7, -2), (1, 7), (-3, 4), (6, -1), (12, 1), (-9, 2)])
    mainC = tableauSigne(3, [(2, 3), (-2, 2), (1, -1)])
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
