#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
import fonctionsSimplifiantes


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
    mainC = fonctionsSimplifiantes.repereDebut(mainC, xmin, ymin, xmax, ymax)
    mainC += r'''\addplot[color=red,domain=-10:10, samples=300]{\{a}*x + \{b}};
\addplot[color=blue,domain=-10:10, samples=300]{\{c}*x + \{d}};\\
\node[text=red] at (7, 9) {$f(x)$};\\
\node[text=blue] at (7, 7) {$g(x)$};\\
\node[text=black, cross=3pt] at (\{xA}, \{yA}) {};\\
\node[text=black, right] at (\{xA}, \{yA}) {A};\\
'''
    mainC = fonctionsSimplifiantes.repereFin(mainC)
    mainC += r'''\begin{enumerate}[resume]
\item À l'intersection des deux droites, on a $f(x)=g(x)$. Soit, $\{a} x \{signB} \{absB} =
\{c} x \{signD} \{absD}$\\
C'est à dire $x=\dfrac{\{difBD}}{\{difCA}} \{egOrAprX} \{xA}$\\
Et donc $y=f(\{xA}) \{egOrAprY} \{yA}$ ou $y = g(\{xA}) \{egOrAprY} \{yA}$\\
Le point d'intersection est donc le point A(\{xA}, \{yA}).
\end{enumerate}
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


