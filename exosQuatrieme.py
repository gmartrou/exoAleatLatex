#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
import numpy as np
from math import *
from fonctionsSupplementaires import *
from fonctionsSimplifiantes import *


def pythagore1(fileExercices, fileCorrections):
    """En connaissant la longueur de l'hypoténuse et d'un autre côté, trouver la longueur du troisième côté."""
    
    a = random.randint(1, 10)
    b = random.randint(a + 1, 15)
    ac = a ** 2
    bc = b ** 2
    di = sqrt(bc - ac)
    ro = round(di, 2)

    main = r'''\exo{Théorème de Pythagore}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AC = \{a} cm.\\%
BC = \{b} cm.\\%
Combien mesure AB ?%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangle_rectangle1.png}%
\end{minipage}%
'''

    mainC = r'''\cor{Théorème de Pythagore}%
ABC est un triangle rectangle en A.\\%
Donc, d'après le théorème de Pythagore :\\%
BC$^2$ = AB$^2$ + AC$^2$\\%
\{bc} = AB$^2$ + \{ac}\\%
AB$^2$ = \{bc} - \{ac}\\%
AB$^2$ = \{di}\\%
AB = $\sqrt{\{di}}$ cm\\%
'''
    if di == ro:
        mainC += r'''AB = \{di} cm\\%
'''
    else:
        mainC += r'''AB $\simeq$ \{ro} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def pythagore2(fileExercices, fileCorrections):
    """Calculer la longueur de l'hypoténuse en connaissant les deux autres longueurs."""
    
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    ac = a**2
    bc = b**2
    sumSq = ac + bc
    sqSum = sqrt(sumSq)
    ro = round(sqSum, 2)

    main = r'''\exo{Théorème de Pythagore}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AB = \{a} cm.\\%
AC = \{b} cm.\\%
Combien mesure BC ?%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangle_rectangle1.png}%
\end{minipage}%
'''

    mainC = r'''\cor{Théorème de Pythagore}%
ABC est un triangle rectangle en A.\\%
Donc, d'après le théorème de Pythagore :\\%
BC$^2$ = AB$^2$ + AC$^2$\\%
BC$^2$ = \{ac} + \{bc}\\%
BC$^2$ = \{sumSq}\\%
BC = $\sqrt{\{sumSq}}$ cm\\%
'''
    if sumSq == ro:
        mainC += r'''BC = \{sqSum} cm\\%
'''
    else:
        mainC += r'''BC $\simeq$ \{sqSum} cm\\%
'''
    localV = locals()
    return endExercice(main, mainC, fileExercices, fileCorrections, localV)


def pythagore3(fileExercices, fileCorrections):
    """En connaissant la longueur de l'hypoténuse et d'un autre côté, trouver la longueur du troisième côté."""
    
    a = random.randint(1, 10)
    b = random.randint(a + 1, 15)
    ac = a**2
    bc = b**2
    di = bc - ac
    sqDi = sqrt(di)
    ro = round(sqDi, 2)

    main = r'''\exo{Théorème de Pythagore}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AB = \{a} cm\\%
BC = \{b} cm.\\%
Combien mesure AC ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangle_rectangle1.png}%
\end{minipage}%
'''

    mainC = r'''\cor{Théorème de Pythagore}%
ABC est un triangle rectangle en A.\\%
Donc, d'après le théorème de Pythagore :\\%
BC$^2$ = AB$^2$ + AC$^2$\\%
\{bc} = \{ac} + AC$^2$\\%
AC$^2$ = \{bc} - \{ac}\\%
AC$^2$ = \{di}\\%
AC = $\sqrt{\{di}}$ cm\\%
'''
    if sqDi == ro:
        mainC += r'''AC = \{di} cm
'''
    else:
        mainC += r'''AC $\simeq$ \{ro} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def pythagore4(fileExercices, fileCorrections):
    """En connaissant les longueurs des 3 côtés d'un triangle, montrer qu'il est rectangle."""
    
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    c = sqrt(a ** 2 + b ** 2)
    ac = a**2
    bc = b**2
    cc = c**2
    sumSq = ac + bc
    c = round(c, 3)

    main = r'''\exo{Théorème de Pythagore}%
ABC est un triangle.\\%
AB = \{a} cm.\\%
AC = \{b} cm.\\%
BC = \{c} cm.\\%
ABC est-il rectangle ? (Si les valeurs sont juste à 1 chiffre après la virgule, cela sera suffisant).\\%
'''
    mainC = r'''\cor{Théorème de Pythagore}%
BC est le plus grand côté.\\%
BC$^2$ = \{c}$^2$\\%
BC$^2$ = \{cc}\\%
AB$^2$ + AC$^2$ = \{ac} + \{bc}\\%
AB$^2$ + AC$^2$ = \{sumSq}\\%
'''
    if sumSq != cc:
        mainC += r'''\`{A} 1 chiffre après la virgule près, on a :\\%
'''
    mainC += r'''BC$^2$ = AB$^2$ + AC$^2$\\%
Donc, d'après la réciproque du théorème de Pythagore ABC est rectangle en B.\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def pythagore5(fileExercices, fileCorrections):
    """En connaissant les longueurs des 3 côtés d'un triangle, dire s'il est ou non rectangle (en
    général, il ne l'est pas)."""
    
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    if random.random() > 0.5:
        c = sqrt(a ** 2 + b ** 2) + random.random()
    else:
        c = sqrt(a ** 2 + b ** 2) - random.random()
    c = round(c, 3)
    ac = a**2
    bc = b**2
    cc = c**2
    sumSq = ac + bc
    
    main = r'''\exo{Théorème de Pythagore}%
ABC est un triangle.\\%
AB = \{a} cm.\\%
AC = \{b} cm.\\%
BC = \{c} cm.\\%
ABC est-il rectangle ? (Si les valeurs sont juste \`{a} 1 chiffre après la virgule, c'est bon)\\%
'''
    mainC = r'''\cor{Théorème de Pythagore}%
BC est le plus grand côté.\\%
BC$^2$ = \{c}$^2$\\%
BC$^2$ = \{cc}\\%
AB$^2$ + AC$^2$ = \{ac} + \{bc}\\%
AB$^2$ + AC$^2$ = \{sumSq}\\%
'''
    
    if sumSq == c**2:
        mainC += r'''\`{A} 1 chiffre après la virgule près, on a :\\%
BC$^2$ = AB$^2$ + AC$^2$\\%
Donc, d'après la réciproque du théorème de Pythagore ABC est rectangle en B.\\%
'''
    else:
        mainC += r'''On a :\\%
BC$^2$ $\neq$ AB$^2$ + AC$^2$\\%
Donc, d'après la contraposée du théorème de Pythagore ABC n'est pas rectangle.\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())
    

def equation1(fileExercices, fileCorrections):
    """Résolution d'équation du type ax + b = cx + d"""
    
    aa = random.randint(2, 15)
    ab = random.randint(-15, -2)
    a = np.random.choice([aa, ab])
    ba = random.randint(1, 15)
    bb = random.randint(-15, -1)
    b = np.random.choice([ba, bb])
    ca = random.randint(2, 15)
    cb = random.randint(-15, -2)
    c = np.random.choice([ca, cb])
    da = random.randint(1, 15)
    db = random.randint(-15, -1)
    d = np.random.choice([da, db])
    signB = ' + '
    signD = ' + '
    absB = b
    absD = d
    retireAjouteB = 'retire'
    retireAjouteD = 'retire'
    if b < 0:
        signB = ' - '
        absB = abs(b)
        retireAjouteB = 'ajoute'
    if d < 0:
        signD = ' - '
        absD = abs(d)
        retireAjouteD = 'ajoute'
    absA = a
    retireAjouteA = 'retire'
    if a < 0:
        absA = abs(a)
        retireAjouteA = 'ajoute'

    absC = c
    retireAjouteC = 'retire'
    if c < 0:
        absC = abs(c)
        retireAjouteC = 'ajoute'
        
    cMa = c - a
    bMd = b - d
    aMc = a - c
    dMb = d - b
    
    solution = (b - d) / (c - a)
    roSolution = round(solution, 2)
    
    valeurExacte = False
    if roSolution == solution:
        valeurExacte = True
        
    main = r'''\exo{Résolution d'équation}%
Trouver la valeur de $x$ vérifiant :\\%
$\{a} x \{signB} \{absB} = \{c} x \{signD} \{absD}$\\%
'''
    
    mainC = r'''\cor{Résolution d'équation}%
$\{a} x \{signB} \{absB} = \{c} x \{signD} \{absD}$\\%
'''
    if a <= c:
        mainC += r'''On \{retireAjouteA} $\{absA} x$ de chaque côté : %
'''
        if a == c:
            mainC += r'''$\{b} = \{d}$\\%
'''
            if b == d:
                mainC += r'''Cela est vrai pour toutes les valeurs de $x$\\%
'''
            else:
                mainC += r'''Cela n'est vrai pour aucune valeur de $x$\\%
'''
        else:
            mainC += r'''$\{b} = \{cMa} x \{signD} \{absD}$\\%
On \{retireAjouteD} \{absD} de chaque côté : $\{bMd} = \{cMa} x$\\%
On divise par \{cMa} de chaque côté : $\dfrac{\{bMd}}{\{cMa}}=x$\\%
'''
    else:
        mainC += r'''On \{retireAjouteC} $\{absC} x$ de chaque côté : %
$\{aMc} x \{signB} \{absB} = \{d}$\\%
On \{retireAjouteB} \{absB} de chaque côté : $\{aMc} x = \{dMb}$\\%
On divise par \{aMc} de chaque côté : $x = \dfrac{\{dMb}}{\{aMc}}$\\%'
'''
    if a != c and valeurExacte:
        if b == d:
            mainC += r'''$x = 0$\\%
'''
        else:
            mainC += r'''$x = \{solution}$\\%
'''
    else:
        if a != c:
            mainC += r'''$x \simeq \{roSolution}$\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def equation2(fileExercices, fileCorrections):
    """Exercice type de calcul d'âge en connaisant la différence et quand un âge sera
    le multiple de l'autre."""

    pasBon = True
    a, b, c, ans = 0, 0, 0, 0
    while pasBon:
        a = random.randint(1, 30)
        b = random.randint(31, 60)
        c = random.randint(2, 4)
        ans = (b - c * a) / (c - 1)
        if (ans == int(ans)) and ((b - a) > 1):
            ans = int(ans)
            pasBon = False
    listePrenoms = ['Paul', 'Pierre', 'Marie', 'Margot', 'Fanny',
                    'Jean', 'Julie', 'Adrien', 'Thomas', 'Suzanne', 'Philippe']
    nomA = np.random.choice(listePrenoms)
    listePrenoms.remove(nomA)
    nomB = np.random.choice(listePrenoms)
    bMa = b - a
    an = 'ans'
    if ans == 1 or ans == -1:
        an = 'an'
    DansIlYA = 'Dans'
    avoir = 'aura'
    if b / a > c:
        DansIlYA = 'Il y a'
        avoir = 'avait'
    signAns = ' + '
    absAns = ans
    ansText = str(ans)
    cAns = c * ans
    absCAns = cAns
    if ans < 0:
        signAns = ' - '
        absAns = abs(ans)
        ansText = '(' + str(ans) + ')'
        absCAns = abs(cAns)
    bMaPans = b - a + ans
    cM1 = c - 1
    bMaPansMcans = b - a + ans - c * ans
    
    main = r'''\exo{Résolution d'équation}
\{nomA} a \{bMa} ans de plus que \{nomB}.\\%
\{DansIlYA} \{ans) \{an} \{nomA} \{avoir} \{c} fois l'âge de \{nomB}.\\%
Quels sont leurs âges respectifs actuellement ?\\%
'''
    
    mainC = r'''\cor{Résolution d'équation}%
Notons $x$ : "L'âge de \{nomA}"\\%
Notons $y$ : "L'âge de \{nomB}"\\%
On a les deux équations suivantes : \\%
\begin{equation*}%
\begin{cases}%
$x = y + \{bMa}$\\%
$x \{signAns} \{absAns} = \{c}(y \{signAns} \{absAns})$\\%
\end{cases}%
\end{equation*}%
On remplace $x$ par $y + \{bMa}$ dans la deuxième équation.\\%
$y + \{bMa} \{signAns} \{absAns} = \{c}(y \{signAns} \{absAns})$\\%
$y + \{bMaPans} = \{c}(y \{signAns} \{absAns})$\\%
On développe : $y + \{bMaPans} = \{c}y + \{c} \times \{ansText}$\\%
$y + \{bMaPans} = \{c}y \{signAns} \{absCAns}$\\%
On retire $y$ de chaque côté : $\{bMaPans} = \{cM1}y \{signAns} \{absCAns}$\\%
On retire \{cAns} de chaque côté : $\{bMaPansMcans} = \{cM1}y$\\%
On divise par \{cM1} de chaque côté : $y = \dfrac{\{bMaPansMcans}}{\{cM1}}$\\%
$y = \{a}$\\%
\{nomB} a \{a} ans.\\%
Et donc, \{nomA} a \{b} ans.\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def equation3(fileExercices, fileCorrections):
    """Exercice type de calcul du nombre d'enfants et d'adultes en fonction
    de la recette d'une salle de spectacle."""
    
    nP = random.randint(100, 400)   # Nombre de personnes.
    nA = random.randint(1, nP - 1)  # Nombre d'adultes.
    nE = int(nP - nA)               # Nombre d'enfants.
    pE = random.randint(2, 7)       # Prix de la place enfant.
    pA = random.randint(8, 13)      # Prix de la place adulte.
    rE = int(nE*pE)                 # Recette due aux enfants.
    rA = int(nA*pA)                 # Recette due aux adultes.
    tot = pE * nE + pA * nA         # Recette totale.
    totA = pA * nP                  # Recette totale si seulement des adultes étaient présents.
    peMpa = pE - pA
    totMtota = tot - totA
    
    main = r'''\exo{Résolution d'équation}%
\{nP} personnes vont à un spectacle.\\%
Les adultes payent \{pA} € la place et les enfants \{pE} €.\\%
La recette de la salle est de \{tot} €.\\%
Combien d'enfants étaient présents ?\\%
'''
    mainC = r'''\cor{Résolution d'équation}%
Notons $x$:"Le nombre d'enfants"\\%
Notons $y$:"Le nombre d'adultes"\\%
On a les deux équations suivantes : %
\begin{equation*}%
\begin{cases}%
x + y = \{nP}\\%
\{pE}x + \{pA} y = \{tot}%
\end{cases}%
\end{equation*}%
On remplace $y$ par \{nP} - $x$ (Cela permet de garder seulement l'inconnue que l'on cherche)\\%
$\{pE} x + \{pA}(\{nP} - x) = \{tot}$\\%
On développe : $\{pE} x + \{pA} \times \{nP} - \{pA} x = \{tot}$\\%
$\{peMpa} x + \{totA} = \{tot}$\\%
On retire \{totA} de chaque côté : $\{peMpa} x = \{totMtota}$\\%
On divise par \{peMpa} de chaque côté : $x = \dfrac{\{totMtota}}{\{peMpa}}$\\%
$x = \{nE}$\\%
Il y avait \{nE} enfants présents.\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def puissance1(fileExercices, fileCorrections):
    """Calcul de puissance de puissances de 10."""
    
    a = random.randint(-30, 30)
    b = random.randint(-30, 30)
    aTb = a*b
    bText = str(b)
    if b < 0:
        bText = '(' + str(b) + r')'
    
    main = r'''\exo{Puissances}%
Faites le calcul suivant (le résultat doit être sous forme d'une puissance de 10).\\
\begin{center}%
$(10^{\{a}})^{\{b}} =$\\%
\end{center}%
'''
    mainC = r'''\cor{Puissances}%
\begin{center}%
$(10^{\{a}})^{\{b}} = 10^{\{a} \times \{bText}} = 10^{\{aTb}}$
\end{center}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def puissance2(fileExercices, fileCorrections):
    """Calcul de multiplication de puissances de 10."""
    
    a = random.randint(-30, 30)
    b = random.randint(-30, 30)
    aPb = a + b
    bText = str(b)
    if b < 0:
        bText = '(' + str(b) + r')'
    
    main = r'''\exo{Puissances}%
Faites le calcul suivant (le résultat doit être sous forme d'une puissance de 10).\\
\begin{center}%
$10^{\{a}} \times 10^{\{b}} =$\\%
\end{center}%
'''
    mainC = r'''\cor{Puissances}%
\begin{center}%
$10^{\{a}} \times 10^{\{b}} = 10^{\{a} + \{bText}} = 10^{\{aPb}}$
\end{center}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def puissance3(fileExercices, fileCorrections):
    """Calcul de division de puissances de 10."""
    
    a = random.randint(-30, 30)
    b = random.randint(-30, 30)
    aMb = a - b
    bText = str(b)
    if b < 0:
        bText = '(' + str(b) + r')'
    
    main = r'''\exo{Puissances}%
Faites le calcul suivant (le résultat doit être sous forme d'une puissance de 10).\\
\begin{center}%
$\dfrac{10^{\{a}}}{10^{\{b}}}=$\\%
\end{center}%
'''
    mainC = r'''\cor{Puissances}%
\begin{center}%
$\dfrac{10^{\{a}}}{10^{\{b}}}= 10^{\{a} - \{bText}} = 10^{\{aMb}}$
\end{center}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def cosinus1(fileExercices, fileCorrections):
    """Calcul du côté adjacent d'un triangle en connaissant l'angle (alpha) et l'hypoténuse."""
    
    a = random.randint(5, 30)
    b = random.randint(10, 80)
    br = b * 2 * pi / 360
    
    c = round(a * cos(br), 2)
    
    main = r'''
\exo{Cosinus}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AB = \{a} cm et l'angle $\alpha$ mesure \{b}\textdegree\\%
Combien mesure AC ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Cosinus}%
cos($\alpha$)=$\dfrac{AC}{AB}$\\%
Donc, AC = AB $\times$ cos($\alpha$)\\%
AC $\simeq$ \{c} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def cosinus2(fileExercices, fileCorrections):
    """Calcul de la longueur de l'hypoténuse d'un triangle en connaissant l'angle (alpha) et le côté adjacent."""
    
    a = random.randint(5, 30)
    b = random.randint(10, 80)
    br = b * 2 * pi / 360
    
    c = round(a / cos(br), 2)
    
    main = r'''
\exo{Cosinus}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AC = \{a} cm et l'angle $\alpha$ mesure \{b}\textdegree\\%
Combien mesure AB ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Cosinus}%
cos($\alpha$)=$\dfrac{AC}{AB}$\\%
Donc, AC = $\dfrac{AB}{cos(\alpha)}$\\%
AC $\simeq$ \{c} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def cosinus3(fileExercices, fileCorrections):
    """Calcul du côté adjacent d'un triangle en connaissant l'angle (beta) et l'hypoténuse."""
    
    a = random.randint(5, 30)
    b = random.randint(10, 80)
    br = b * 2 * pi / 360
    
    c = round(a * cos(br), 2)
    
    main = r'''
\exo{Cosinus}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AB = \{a} cm et l'angle $\beta$ mesure \{b}\textdegree\\%
Combien mesure BC ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Cosinus}%
cos($\beta$)=$\dfrac{BC}{AB}$\\%
Donc, AC = AB $\times$ cos($\beta$)\\%
AC $\simeq$ \{c} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def cosinus4(fileExercices, fileCorrections):
    """Calcul de la longueur de l'hypoténuse d'un triangle en connaissant l'angle (beta) et le côté adjacent."""
    
    a = random.randint(5, 30)
    b = random.randint(10, 80)
    br = b * 2 * pi / 360
    
    c = round(a / cos(br), 2)
    
    main = r'''
\exo{Cosinus}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
BC = \{a} cm et l'angle $\beta$ mesure \{b}\textdegree\\%
Combien mesure AB ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Cosinus}%
cos($\beta$)=$\dfrac{BC}{AB}$\\%
Donc, AC = $\dfrac{AB}{cos(\beta)}$\\%
AC $\simeq$ \{c} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def cosinus5(fileExercices, fileCorrections):
    """Calculez les mesures manquantes à partir de deux mesures données."""
    
    a = random.randint(5, 30)
    beta = random.randint(10, 80)
    alpha = 90 - beta
    betaR = beta * 2 * pi / 360
    alphaR = pi/2 - betaR
    CH = a*cos(alphaR)
    c = round(a / cos(betaR), 2)
    AC = CH / cos(betaR)
    AH = AC*cos(alphaR)
    
    main = r'''
\exo{Longueur à trouver}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
BC = \{a} cm et l'angle $\theta$ mesure \{beta}°\\%
Combien mesure AH ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/PythagoreDoubleTriangleA.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Longueur à trouver}%
La somme des angles dans un triangle mesurant 180°, l'angle $\alpha$ mesure \{alpha}°\\%
cos($\alpha$)=$\dfrac{CH}{BC}$\\%
Donc, CH = AB $\times$ cos($\alpha$) $\simeq$ \{CH} cm\\%
cos($\theta$)=$\dfrac{CH}{AC}$\\%
Donc, AC = $\dfrac{CH}{cos(\theta)} \simeq$ \{AC} cm\\%
cos($\alpha$)=$\dfrac{AH}{AC}$\\%
Donc, AH = AC $\times$ cos($\alpha$) $\simeq$ \{AH} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def cosinus6(fileExercices, fileCorrections):
    """Calculez les mesures manquantes à partir de deux mesures données."""
    
    AC = random.randint(5, 30)
    theta = random.randint(10, 80)
    alpha = 90 - theta
    thetaR = theta * 2 * pi / 360
    alphaR = pi / 2 - thetaR
    CH = AC * cos(thetaR)
    BC = round(CH / cos(alphaR), 2)
    BH = BC * cos(thetaR)
    
    main = r'''
\exo{Longueur à trouver}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AC = \{AC} cm et l'angle $\alpha$ mesure \{alpha}°\\%
Combien mesure BH ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/PythagoreDoubleTriangleA.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Longueur à trouver}%
La somme des angles dans un triangle mesurant 180°, l'angle $\theta$ mesure \{theta}°\\%
cos($\theta$)=$\dfrac{CH}{AC}$\\%
Donc, CH = AC $\times$ cos($\theta$) $\simeq$ \{CH} cm\\%
cos($\alpha$)=$\dfrac{CB}{CH}$\\%
Donc, BC = $\dfrac{CH}{cos(\theta)} \simeq$ \{BC} cm\\%
cos($\theta$)=$\dfrac{BC}{BH}$\\%
Donc, BH = $\dfrac{BC}{cos(\theta)} \simeq$ \{BH} cm\\%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def fraction1(fileExercices, fileCorrections):
    """Addition d'un nombre quelconque de fractions (à fixer dans l'énoncé)."""

    nums = []
    dens = []
    signs = []
    # nbrTerms = random.randint(3, 4)
    nbrTerms = 3
    for i in range(nbrTerms):
        aa = random.randint(1, 30)
        ab = random.randint(-30, -1)
        nums.append(np.random.choice([aa, ab]))
        ba = random.randint(1, 30)
        bb = random.randint(-30, -1)
        dens.append(np.random.choice([ba, bb]))
        signs.append(np.random.choice([r' + ', r' - ']))
    
    main = r'''\exo{Addition de fractions}%
Faites le calcul suivant (le résultat doit être sous forme de fraction).\\%
\begin{center}%
$A='''
    
    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            main += r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
        else:
            main += signs[i] + r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
    main += r'$%' + '\n'
    main += r'\end{center}%' + '\n'
    main += '\n'

    mainC = r'\cor{Addition de fractions}%' + '\n'
    mainC += r'\begin{center}%' + '\n'
    mainC += r'$A = '
    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            mainC += r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
        else:
            mainC += signs[i] + r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
    mainC += r'$%' + '\n'
    mainC += r'\end{center}%' + '\n'
    for i in range(nbrTerms):
        if signs[i] == r' + ':
            if dens[i] / nums[i] < 0:
                signs[i] = r' - '
        else:
            if dens[i] / nums[i] < 0:
                signs[i] = r' + '
        dens[i] = abs(dens[i])
        nums[i] = abs(nums[i])
    ppcmVal = PPCM(dens)
    mainC += r'\begin{center}%' + '\n'
    mainC += r'$A = '
    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            mainC += r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
        else:
            mainC += signs[i] + r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
    mainC += r'$%' + '\n'
    mainC += r'\end{center}%' + '\n'
    mainC += r'\begin{center}%' + '\n'
    mainC += r'$A = '
    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            mainC += r'\dfrac{' + str(nums[i]) + r'\textcolor{red}{\times ' + \
                     str(int(ppcmVal / dens[i])) + r'}}{' + str(dens[i]) + r'\textcolor{red}{\times ' + \
                     str(int(ppcmVal / dens[i])) + r'}}'
        else:
            mainC += signs[i] + r'\dfrac{' + str(nums[i]) + r'\textcolor{red}{\times ' + \
                     str(int(ppcmVal / dens[i])) + r'}}{' + str(dens[i]) + r'\textcolor{red}{\times ' + \
                     str(int(ppcmVal / dens[i])) + r'}}'
    mainC += r'$%' + '\n'
    mainC += r'\end{center}%' + '\n'
    mainC += r'\begin{center}%' + '\n'
    mainC += r'$A = '
    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            mainC += r'\dfrac{' + str(int(nums[i] * ppcmVal / dens[i])) + r'}{' + \
                     str(int(ppcmVal)) + r'}'
        else:
            mainC += signs[i] + r'\dfrac{' + str(int(nums[i] * ppcmVal / dens[i])) + r'}{' + \
                     str(int(ppcmVal)) + r'}'

    mainC += r'$%' + '\n'
    mainC += r'\end{center}%' + '\n'
    mainC += r'\begin{center}%' + '\n'
    mainC += r'$A = \dfrac{'
    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            mainC += str(int(nums[i] * ppcmVal / dens[i]))
        else:
            mainC += signs[i] + str(int(nums[i] * ppcmVal / dens[i]))
    mainC += r'}{' + str(int(ppcmVal)) + r'}%' + '\n'
    mainC += r'$%' + '\n'
    mainC += r'\end{center}%' + '\n'
    numerator = 0
    for i in range(nbrTerms):
        if signs[i] == r' + ':
            numerator += nums[i]
        else:
            numerator -= nums[i]
    mainC += r'\begin{center}%' + '\n'
    mainC += r'$A = \dfrac{' + str(int(numerator))
    mainC += r'}{' + str(int(ppcmVal)) + r'}$%' + '\n'
    mainC += r'\end{center}%' + '\n'
    pgcdVal = PGCD([numerator, ppcmVal])
    if pgcdVal == 1:
        if numerator < 0:
            mainC += r'\begin{center}%' + '\n'
            mainC += r'$A=-\dfrac{' + str(int(abs(numerator / pgcdVal)))
            mainC += r'}{' + str(int(ppcmVal / pgcdVal)) + r'}$%' + '\n'
            mainC += r'\end{center}%' + '\n'
    else:
        if numerator < 0:
            mainC += r'\begin{center}%' + '\n'
            mainC += r'$A=-\dfrac{' + str(int(abs(numerator / pgcdVal)))
            mainC += r'}{' + str(int(ppcmVal / pgcdVal)) + r'}$%' + '\n'
            mainC += r'\end{center}%' + '\n'
        else:
            mainC += r'\begin{center}%' + '\n'
            mainC += r'$A=\dfrac{' + str(int(numerator / pgcdVal))
            mainC += r'}{' + str(int(ppcmVal / pgcdVal)) + r'}$%' + '\n'
            mainC += r'\end{center}%' + '\n'
    mainC += '\n'
    
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def doubleDeveloppement(fileExercices, fileCorrections):
    """Exercice type de calcul litteral. Développer et réduire (ax + b)(cx + d)"""

    a1 = random.randint(2, 6)
    a2 = random.randint(-6, -2)
    a = np.random.choice([a1, a2])
    b1 = random.randint(1, 6)
    b2 = random.randint(-6, -1)
    b = np.random.choice([b1, b2])
    c1 = random.randint(2, 6)
    c2 = random.randint(-6, -2)
    c = np.random.choice([c1, c2])
    d1 = random.randint(1, 6)
    d2 = random.randint(-6, -1)
    d = np.random.choice([d1, d2])
    
    signA, signB, signC, signD = ' + ', ' + ', ' + ', ' + '
    aText = r'\textcolor{red}{' + str(a) + 'x}'
    bText = r'\textcolor{blue}{' + str(b) + '}'
    cText = r'\textcolor{brown}{' + str(c) + '}'
    dText = r'\textcolor{violet}{' + str(d) + 'x}'
    absA, absB, absC, absD = a, b, c, d
    if a < 0:
        aText = r'(\textcolor{red}{' + str(a) + r'x})'
        absA = abs(a)
        signA = ' - '
    if b < 0:
        bText = r'(\textcolor{blue}{' + str(b) + r'})'
        absB = abs(b)
        signB = ' - '
    if c < 0:
        cText = r'(\textcolor{brown}{' + str(c) + r'})'
        absC = abs(c)
        signC = ' - '
    if d < 0:
        dText = r'(\textcolor{violet}{' + str(d) + r'x})'
        absD = abs(d)
        signD = ' - '
    ac = a*c
    ad = a*d
    bc = b*c
    bd = b*d

    signAC, signAD, signBC, signBD = ' + ', ' + ', ' + ', ' + '
    absAC, absAD, absBC, absBD = ac, ad, bc, bd
    if ac < 0:
        signAC = ' - '
        absAC = abs(ac)
    if ad < 0:
        signAD = ' - '
        absAD = abs(ad)
    if bc < 0:
        signBC = ' - '
        absBC = abs(bc)
    if bd < 0:
        signBD = ' - '
        absBD = abs(bd)
    acPbd = ac + bd
    signAcpbd = ' + '
    absAcpbd = acPbd
    if acPbd < 0:
        signAcpbd = ' - '
        absAcpbd = abs(acPbd)
        
    main = r'''\exo{Double développement}%
Développer et réduire l'expression suivante.\\
\begin{center}%
$A = (\{a} x \{signB} \{absB})(\{c}  \{signD} \{absD} x)$\\%
\end{center}%
'''
    mainC = r'''\cor{Double développement}%
\begin{center}%
$A = (\textcolor{red}{\{a} x} \textcolor{blue}{\{signB} \{absB}})
(\textcolor{brown}{\{c}} \textcolor{violet}{\{signD} \{absD} x})$\\%
$A = \{aText} \times \{cText} + \{aText} \times \{dText} +
\{bText} \times \{cText} + \{bText} \times \{dText}$\\
$A = \{ac}x \{signAD} \{absAD} x^2 \{signBC} \{absBC} \{signBD} \{absBD} x$\\
$A = \{ad} x^2 \{signAcpbd} \{absAcpbd} x \{signBC} \{absBC}$\\
\end{center}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())


def pileOuFace(fileExercices, fileCorrections):
    """Exercice type de calcul litteral. Développer et réduire (ax + b)(cx + d)"""

    elPerLign = 10
    n = random.randint(10, 50)
    nLign = (n - 1) // elPerLign + 1
    listePrenoms = ['Paul', 'Pierre', 'Marie', 'Margot', 'Fanny',
                    'Jean', 'Julie', 'Adrien', 'Thomas', 'Suzanne', 'Philippe']
    nomA = np.random.choice(listePrenoms)
    listePrenoms.remove(nomA)
    nomB = np.random.choice(listePrenoms)

    nP = 0
    nF = 0
    compteur = 0

    main = r'''\exo{Pile ou Face ?}%
Deux amis, \{nomA} et \{nomB} jouent à "Pile ou Face". Ils ont effectué les \{n} lancers suivants :\\%
\begin{center}
\begin{tabular}{|*{10}{c|}}
'''
    for i in range(nLign):
        main += r'''\hline
'''
        for j in range(i*10, min((i+1)*10, n)):
            pOf = np.random.choice([r'pile', r'face'])
            if pOf == 'pile':
                nP += 1
            else:
                nF += 1
            if (j+1) % 10 == 0:
                pOf += r'''\\%
'''
            else:
                pOf += r'&'
            main += pOf
        fP = nP/n   # Fréquence d'apparition des piles
        fF = nF/n   # Fréquence d'apparition des faces
    for j in range((10 - 1) - (n % 10)):
        main += r'&'
    main += r'''\\
\hline%
'''
    main += r'''\end{tabular}
\end{center}
\{nomA} affirme que le fréquence statistique d'apparition des piles est plus importantes que la probabilité 
théorique.
'''

    mainC = r'''\cor{Double développement}%
\begin{center}%
test
\end{center}%
'''
    return endExercice(main, mainC, fileExercices, fileCorrections, locals())
