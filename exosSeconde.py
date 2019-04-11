#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
from fonctionsSimplifiantes import *


def fonctionsAffineIntersection(fileExercices, fileCorrections):
    """Calcul du point d'intersection de deux fonctions affines."""
    
    a, b, c, d = 0, 0, 0, 0
    while b == d or a == c:
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        b = np.random.choice([b1, b2])
        c1 = random.randint(1, 6)
        c2 = random.randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = random.randint(2, 6)
        d2 = random.randint(-6, -1)
        d = np.random.choice([d1, d2])
    difBD = d - b
    difCA = a - c
    signB, signD = ' + ', ' + '
    absB, absD = b, d
    if b < 0:
        signB = r' - '
        absB = abs(b)
    if d < 0:
        signD = r' - '
        absD = abs(d)

    xmin = -10
    ymin = -10
    xmax = 10
    ymax = 10
    xA = (d - b) / (a - c)
    yA = a * xA + b
    egOrAprX = '\simeq'
    egOrAprY = '\simeq'
    if xA == int(xA):
        xA = int(xA)
        egOrAprX = '='
    elif xA != round(xA, 2):
        xA = round(xA, 2)
    else:
        egOrAprX = '='

    if yA == int(yA):
        yA = int(yA)
        egOrAprY = '='
    elif yA != round(yA, 2):
        yA = round(yA, 2)
    else:
        egOrAprY = '='

    main = r'''\exo{Intersection de fonctions affines}%
Soit $f$ et $g$ les fonctions définies sur $\R$ par $f(x) = \{a} x \{signB} \{absB}$ et 
$g(x) = \{c} x \{signD} \{absD}$.
\medskip%
\begin{enumerate}%
\item Tracer les courbes représentatives des fonctions $f$ et $g$ dans le plan muni d'un repère.%
\item Calculer les coordonnées du point d'intersection des deux courbes.%
\end{enumerate}%    
'''
    mainC = r'''\cor{Intersection de fonctions affines}
\medskip%
\begin{enumerate}%
\item Les courbes représentantes des fonctions $f$ et $g$ sont sur le graphique ci-après :
\end{enumerate}
'''
    mainC = repereDebut(mainC, xmin, ymin, xmax, ymax)
    mainC += r'''\addplot[color=red,domain=-10:10, samples=300]{\{a}*x + \{b}};
\addplot[color=blue,domain=-10:10, samples=300]{\{c}*x + \{d}};\\
\node[text=red] at (7, 9) {$f(x)$};\\
\node[text=blue] at (7, 7) {$g(x)$};\\
\node[text=black, cross=3pt] at (\{xA}, \{yA}) {};\\
\node[text=black, right] at (\{xA}, \{yA}) {A};\\
'''
    mainC = repereFin(mainC)
    mainC += r'''\begin{enumerate}[resume]
\item À l'intersection des deux droites, on a $f(x)=g(x)$. Soit, $\{a} x \{signB} \{absB} = 
\{c} x \{signD} \{absD}$\\
C'est à dire $x=\dfrac{\{difBD}}{\{difCA}} \{egOrAprX} \{xA}$\\
Et donc $y=f(\{xA}) \{egOrAprY} \{yA}$ ou $y = g(\{xA}) \{egOrAprY} \{yA}$\\
Le point d'intersection est donc le point A(\{xA}, \{yA}).
\end{enumerate}
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def tableauDeSigneUn1(fileExercices, fileCorrections):
    """Tableau de signe simple avec une seule expression du premier degré ax+b <= 0"""
    
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
\item En déduire les valeurs pour lesquelles $f(x) \leq 0$%
\end{enumerate}%
'''
    mainC = r'''\cor{Tableau de Signes}%
\begin{enumerate}%
\item La valeur de $x$ pour laquelle $f(x) = 0$ est \{VAnnul}.\\%
Le coefficient devant $x$ est \{posNegM}, donc la fonction sera \{posNeg} après \{VAnnul}
et \{negPos} avant.\\
On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $ \{VAnnul} $, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, }%' + '\n'
\end{tikzpicture}%
\end{center}%
'''
    if a > 0:
        mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open  left]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open right]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
\begin{center}%
\begin{tikzpicture}%
\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $ \{VAnnul} $, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, }%' + '\n'
\end{tikzpicture}%
\end{center}%
'''
    if a > 0:
        mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $ \{VAnnul} $, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, }%' + '\n'
\end{tikzpicture}%
\end{center}%
'''
    if a < 0:
        mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open  left]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open right]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
On a donc le tableau de signes suivant :\\%
\begin{center}%
\begin{tikzpicture}%
\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $ \{VAnnul} $, $+\infty$}%
\tkzTabLine{, \{signMA}, z, \{signA}, }%' + '\n'
\end{tikzpicture}%
\end{center}%
'''
    if a < 0:
        mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{-\infty}{\{VAnnul}}$%
'''
    else:
        mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{\{VAnnul}}{+\infty}$
'''
    mainC += r'''\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
        if a*c < 0:
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
        if a*c < 0:
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
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
        if a*c < 0:
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
        if a*c < 0:
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
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
        if a*c > 0:
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
        if a*c > 0:
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
        if a*c > 0:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x\in \R$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) \geq 0$ pour $x=\{VAnnul1}$%
'''
    mainC += r'''\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
        if a*c > 0:
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
        if a*c > 0:
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
        if a*c > 0:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x\neq \{VAnnul1}$%
'''
        else:
            mainC += r'''\item On peut en déduire que $f(x) > 0$ pour $x=\emptyset$%
'''
    mainC += r'''\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def vecteursParall1(fileExercices, fileCorrections):
    """Exo vecteur (prouver qu'il s'agit d'un parallèlogramme)"""
    
    xA = random.randint(-5, -1)
    yA = random.randint(-5, -1)
    xB = random.randint(-5, -1)
    yB = random.randint(1, 5)
    xC = random.randint(1, 5)
    yC = random.randint(1, 5)
    xD = xA + xC - xB
    yD = yA + yC - yB
    xBA = xA - xB
    yBA = yA - yB
    xCD = xD - xC
    yCD = yD - yC

    main = r'''\exo{Vecteurs et parallèlogrammes.}%
Dans le plan muni d'un repère $\left( {{\mathrm{O}};\vec{\imath}, 
\vec{\jmath}} \right)$, on considère les points $A\left(\{xA}; \{yA}\right)$, $B\left(\{xB}; \{yB}
\right)$, $C\left(\{xC}; \{yC}\right)$ et $D\left(\{xD}; \{yD}\right)$.\\%
Le quadrilatère ABCD est-il un parallèlogramme ?%
'''
    mainC = r'''\cor{Vecteurs et parallèlogrammes.}%
'''
    mainC = repereDebut(mainC, -6, -8, 9, 6)
    mainC += r'''\path[draw, red] (\{xA}, \{yA})  coordinate [label= left:$A$] (A) -- 
(\{xB}, \{yB})  coordinate [label=above:$B$] (B) -- (\{xC}, \{yC})  coordinate [label=right:$C$] (C) -- 
(\{xD}, \{yD})  coordinate [label=right:$D$] (D) -- cycle;%
'''
    mainC = repereFin(mainC)
    mainC += r'''$\coordv{BA}{x_A - x_B}{y_A - y_B}$. Donc, $\coordv{BA}{\{xA} - (\{xB})}{\{yA} - \{yB}}$. 
Ainsi, $\coordv{BA}{\{xBA}}{\{yBA}}$\\%

$\coordv{CD}{x_D - x_C}{y_D - y_C}$. Donc, $\coordv{CD}{\{xD} - \{xC}}{\{yD} - \{yC}}$. 
Ainsi, $\coordv{CD}{\{xCD}}{\{yCD}}$\\%

$\vv{BA}=\vv{CD}$, donc, ABCD est un parallèlogramme.
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def vecteursParall2(fileExercices, fileCorrections):
    """Exo vecteur (prouver qu'il ne s'agit pas d'un parallèlogramme)"""
    
    xA = random.randint(-5, -1)
    yA = random.randint(-5, -1)
    xB = random.randint(-5, -1)
    yB = random.randint(1, 5)
    xC = random.randint(1, 5)
    yC = random.randint(1, 5)
    xD = xA + xC - xB
    yD = yA + yC - yB

    perturbation = [-2, -1, 1, 2]
    xD += np.random.choice(perturbation)
    yD += np.random.choice(perturbation)

    xBA = xA - xB
    yBA = yA - yB
    xCD = xD - xC
    yCD = yD - yC

    main = r'''\exo{Vecteurs et parallèlogrammes.}%
Dans le plan muni d'un repère $\left( {{\mathrm{O}};\vec{\imath}, 
\vec{\jmath}} \right)$, on considère les points $A\left(\{xA}; \{yA}\right)$, $B\left(\{xB}; \{yB}
\right)$, $C\left(\{xC}; \{yC}\right)$ et $D\left(\{xD}; \{yD}\right)$.\\%
Le quadrilatère ABCD est-il un parallèlogramme ?%
'''
    mainC = r'''\cor{Vecteurs et parallèlogrammes.}%
'''
    mainC = repereDebut(mainC, -6, -8, 9, 6)
    mainC += r'''\path[draw, red] (\{xA}, \{yA})  coordinate [label= left:$A$] (A) -- 
(\{xB}, \{yB})  coordinate [label=above:$B$] (B) -- (\{xC}, \{yC})  coordinate [label=right:$C$] (C) -- 
(\{xD}, \{yD})  coordinate [label=right:$D$] (D) -- cycle;%
'''
    mainC = repereFin(mainC)
    mainC += r'''$\coordv{BA}{x_A - x_B}{y_A - y_B}$. Donc, $\coordv{BA}{\{xA} - (\{xB})}{\{yA} - \{yB}}$. 
Ainsi, $\coordv{BA}{\{xBA}}{\{yBA}}$\\%

$\coordv{CD}{x_D - x_C}{y_D - y_C}$. Donc, $\coordv{CD}{\{xD} - \{xC}}{\{yD} - \{yC}}$. 
Ainsi, $\coordv{CD}{\{xCD}}{\{yCD}}$\\%

$\vv{BA} \neq \vv{CD}$, donc, ABCD n'est pas un parallèlogramme.%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def vecteursCalculCoord1(fileExercices, fileCorrections):
    """Exo vecteur (Calculer les coordonnées d'un point à partir d'une expression vectorielle)"""
    
    xA = random.randint(-5, -1)
    yA = random.randint(-5, -1)
    xB = random.randint(-5, -1)
    yB = random.randint(1, 5)
    xC = random.randint(1, 5)
    yC = random.randint(1, 5)
    coeff1, coeff2 = 0, 0
    signC2 = ' - '
    while coeff1 in [-1, 0, 1] or coeff2 in [-1, 0, 1]:
        coeff1 = random.randint(-5, 5)
        coeff2 = random.randint(-5, 5)
        if coeff2 >= 0:
            signC2 = ' + '
    absC2 = abs(coeff2)

    xAB = xB - xA
    yAB = yB - yA

    xCA = xA - xC
    yCA = yA - yC

    absC2 = abs(coeff2)

    dX = coeff1 * (xB - xA) + coeff2 * (xA - xC)
    dY = coeff1 * (yB - yA) + coeff2 * (yA - yC)
    absdX = abs(dX)
    absdY = abs(dY)

    signdX = ' - '
    signdY = ' - '
    if dX >= 0:
        signdX = ' + '
    if dY >= 0:
        signdY = ' + '

    xD = xB + dX
    yD = yB + dY

    main = r'''\exo{Vecteurs et coordonnées.}%
Dans le plan muni d'un repère $\left( {{\mathrm{O}};\vec{\imath}, 
\vec{\jmath}} \right)$, on considère les points $A\left(\{xA}; \{yA}\right)$, $B\left(\{xB}; \{yB}
\right)$ et $C\left(\{xC}; \{yC}\right)$.\\%
Calculez les coordonnées du point D tel que :%
\begin{center}%
$\vv{BD} = \{coeff1} \vv{AB} \{signC2} \{absC2} \vv{CA}$%
\end{center}%
'''
    mainC = r'''\cor{Vecteurs et coordonnées.}%
\begin{enumerate}%
\item On calcule les coordonnées des vecteurs $\vv{AB}$ et $\vv{CA}$\\%
$\coordv{AB}{x_B - x_A}{y_B - y_A}$. Donc, $\coordv{AB}{\{xB} - (\{xA})}{\{yB} - \{yA}}$. 
Ainsi, $\coordv{AB}{\{xAB}}{\{yAB}}$\\%

$\coordv{CA}{x_A - x_C}{y_A - y_C}$. Donc, $\coordv{CA}{\{xA} - \{xC}}{\{yA} - \{yC}}$. 
Ainsi, $\coordv{CA}{\{xCA}}{\{yCA}}$\\%

\item On calcule maintenant, grâce à ces vecteurs, les coordonnées du vecteurs $\vv{BD}$\\%
$\vv{BD}=\{coeff1} \vv{AB} \{signC2} \{absC2} \vv{CA}$.
'''
    if xB > xA:
        mainC += r'''Donc, $\coordv{BD}{\{coeff1} \times \{xAB} \{signC2} \{absC2} \times (\{xCA})}{
\{coeff1} \times \{yAB} \{signC2} \{absC2} \times(\{yCA})}$.
'''
    else:
        mainC += r'''Donc, $\coordv{BD}{\{coeff1} \times \{xAB} \{signC2} \{absC2} \times\{xCA}}{
\{coeff1} \times \{yAB} \{signC2} \{absC2} \times (\{yCA})}$. 
'''

    mainC += r'''Soit, $\coordv{BD}{\{dX}}{\{dY}}$.\\%
\item À partir des coordonnées de B et $\vv{BD}$, on calcule ceux du point D.\\%
On a $\coord{B}{\{xB}}{\{yB}}$ et $\coordv{BD}{\{dX}}{\{dY}}$. 
Donc $\coord{D}{\{xB} \{signdX} \{absdX}}{\{yB} \{signdY} \{absdY}}$\\%

Et, finalement, $\coord{D}{\{xD}}{\{yD}}$%
\end{enumerate}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def vecteursDroitesColineaires(fileExercices, fileCorrections):
    """Exercice sur les vecteurs, le but est de vérifier que les deux droites sont colinéaires."""
    
    xA, yA, xB, yB, xC, yC, xAB, yAB = 0, 0, 0, 0, 100, 100, 0, 0
    while xC > 8 or yC > 8:
        xA = random.randint(-5, -1)
        yA = random.randint(-5, -1)
        xB = random.randint(xA + 1, 1)
        yB = random.randint(yA + 1, 1)
        xAB = xB - xA
        yAB = yB - yA
        coeff = random.randint(2, 3)
        xC = xB + coeff * xAB
        yC = yB + coeff * yAB
    xCB = xB - xC
    yCB = yB - yC
    if xA < 0:
        xAtext = "(" + str(xA) + ")"
    else:
        xAtext = str(xA)
    if yA < 0:
        yAtext = "(" + str(yA) + ")"
    else:
        yAtext = str(yA)
    if xC < 0:
        xCtext = "(" + str(xC) + ")"
    else:
        xCtext = str(xC)
    if yC < 0:
        yCtext = "(" + str(yC) + ")"
    else:
        yCtext = str(yC)

    if yCB < 0:
        yCBtext = "(" + str(yCB) + ")"
    else:
        yCBtext = str(yCB)
    if xCB < 0:
        xCBtext = "(" + str(xCB) + ")"
    else:
        xCBtext = str(xCB)
    if yAB < 0:
        yABtext = "(" + str(yAB) + ")"
    else:
        yABtext = str(yAB)
    det = xAB * yCB - yAB * xCB

    main = r'''\exo{Vecteurs et colinéarité.}%
Dans le plan muni d'un repère $\left( {{\mathrm{O}}; \vec{\imath},\vec{\jmath}} \right)$, 
on considère les points $A\left(\{xA}; \{yA}\right)$, $B\left(\{xB}; \{yB}\right)$ 
et $C\left(\{xC}; \{yC}\right)$.\\
Les points A, B et C sont-ils alignés ?%
'''
    mainC = r'''\cor{Vecteurs et colinéarité.}%
'''
    mainC = repereDebut(mainC, xA-1, yA-1, max(xC+1, 1), max(yC+1, 1))
    mainC += r'''\node[text=red, cross=3pt, label=right:\textcolor{red}{A}] at (\{xA}, \{yA}) {};\\
\node[text=red, cross=3pt, label=right:\textcolor{red}{B}] at (\{xB}, \{yB}) {};\\
\node[text=red, cross=3pt, label=right:\textcolor{red}{C}] at (\{xC}, \{yC}) {};\\
'''
    mainC = repereFin(mainC)
    mainC += r'''\begin{enumerate}%
\item On calcule les coordonnées des vecteurs $\vv{AB}$ et $\vv{CB}$\\%
$\coordv{AB}{x_B - x_A}{y_B - y_A}$. 
Donc, $\coordv{AB}{\{xB} - \{xAtext}}{\{yB} - \{yAtext}}$. Ainsi, $\coordv{AB}{\{xAB}}{\{yAB}}$\\%
$\coordv{CB}{x_B - x_C}{y_B - y_C}$. 
Donc, $\coordv{CB}{\{xB} - \{xCtext}}{\{yB} - \{yCtext}}$. Ainsi, $\coordv{CB}{\{xCB}}{\{yCB}}$\\%
\item On calcule maintenant le déterminant de ces vecteurs.\\%
det($\vv{AB}$, $\vv{CB}$)=$x_{AB} \times y_{CB} - y_{AB} \times x_{CB}$=\{xAB} $\times$ \{yCBtext} - 
\{yABtext} $\times$ \{xCBtext} = \{det}\\%
Le déterminant de ces deux vecteurs étant nul, ils sont colinéaires.%
\end{enumerate}
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def probasMaladies(fileExercices, fileCorrections):
    """Description de l'exercice."""

    # Définition des variables.
    annee = random.randint(1700, 1850)
    ville = np.random.choice(['Berlin', 'Pékin', 'Paris', 'Stokholm', 'Bucarest', 'Rome', 'Madrid',
                              'Brest', 'Londres', 'Rouen', 'Gênes'])
    listeMaladies = ['lèpre', 'peste', 'diphtérie', 'pneumonie', 'rage',
                     'rougeole', 'tuberculose', 'méningite']
    malA = np.random.choice(listeMaladies)
    listeMaladies.remove(malA)
    malB = np.random.choice(listeMaladies)
    pApercent = pBpercent = 0
    while pApercent == pBpercent:
        pApercent = random.randint(3, 40)
        pBpercent = random.randint(3, 40)
    pTpercent = random.randint(1, min(pApercent, pBpercent) - 1)
    pA = pApercent/100
    pB = pBpercent/100
    pAinterB = pTpercent/100
    pAinterBBar = 1 - pAinterB
    pAunionB = pA + pB - pAinterB
    pAunionBBar = 1 - pAunionB
    pAonly = pA - pAinterB
    pAonlyBar = 1 - pAonly
    pBonly = pB - pAinterB
    pAxorB = pAunionB - pAinterB
    # Fin des variables.

    # Enoncé de l'exercice.
    main = r'''\exo{Des maladies dangereuses}%
En \{annee}, les habitants de \{ville} subissent une épidémie. Les deux maladies décimants la ville sont
\{malA} et \{malB}.\\%

On estime que  \{pApercent}\% des habitants sont atteints de \{malA}, \{pBpercent}\% 
des animaux sont atteints de \{malB}
et \{pTpercent}\% des animaux sont atteints des deux maladies à la fois.\\%

On prend un habitant au hasard dans la ville.\\%

\begin{enumerate}[label=\alph*)]%
    \item Calculer la probabilité qu'il soit atteint seulement de \{malA}.%
    \item Calculer la probabilité qu'il ne soit pas malade.%
    \item Calculer la probabilité qu'il soit malade mais seulement atteint d'une des deux maladies%
\end{enumerate}%
'''
    # Fin de l'énoncé.

    # Fichier texte de la correction.
    mainC = r'''\cor{Nom de l'exercice}%
Notons A : "L'habitant de \{ville} est atteint de \{malA}"\\%
Notons B : "L'habitant de \{ville} est atteint de \{malB}"\\%

Les données de l'énoncé nous disent que :\\%
p(A) = \{pA}\\%
p(B) = \{pB}\\%
p(A $\cap$ B) = \{pAinterB}\\%
Afin de bien se représenter le problème, on peut faire les schémas suivants :\\%
\begin{center}
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesSecondes/proba13.png}%
\end{minipage}%
\begin{minipage}{0.32\textwidth}%
\includegraphics[width = \textwidth]{imagesSecondes/proba23.png}%
\end{minipage}%
\begin{minipage}{0.32\textwidth}%
\includegraphics[width = \textwidth]{imagesSecondes/proba3.png}%
\end{minipage}%
\end{center}
\begin{enumerate}[label=\alph*)]%
\item La probabilité que l'on cherche est la probabilité qu'il soit atteint de \{malA} ET pas de \{malB}.\\%
On cherche donc p($A \cap \bar{B}$).\\%
En observant les schémas on observe que p(A $\cap$ $\bar{B}$) = p(A) - p(A $\cap$ B) = 
\{pA} - \{pAinterB} = \{pAonly}.\\%
\item La probabilité cherchée est p($\overline{A \cup B}$) = 1 - p($A \cup B$).\\%
Or, p($A \cup B$) = p(A) + p(B) - p($A \cap B$) = \{pA} + \{pB} - \{pAinterB} = \{pAunionB}.\\%
Donc, p($\overline{A \cup \bar{B}}$) = 1 - \{pAunionB} = \{pAunionBBar}.\\%
\item La probabilité recherchée est la probabilité qu'il soit malade moins la probabilité qu'il soit atteint 
des deux à la fois soit p($A \cap \bar{B}$) + p($B \cap \bar{A}$) = p($A \cup B$) - p($A \cap B$) = 
\{pAunionB} - \{pAinterB} = \{pAxorB}.\\%
\end{enumerate}
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def exercice(fileExercices, fileCorrections):
    """Description de l'exercice."""

    # Définition des variables.

    # Fin des variables.

    # Enoncé de l'exercice.
    main = r'''\exo{Nom de l'exercice}
'''
    # Fin de l'énoncé.

    # Fichier texte de la correction.
    mainC = r'''\cor{Nom de l'exercice}
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())
