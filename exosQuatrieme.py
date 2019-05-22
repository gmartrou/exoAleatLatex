#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
import numpy as np
from math import *
import fonctionsSupplementaires
import fonctionsSimplifiantes


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, localV)


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
    

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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
\exo{Mesures manquantes}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
BC = \{a} cm et l'angle $\theta$ mesure \{beta}°\\%
Combien mesure AH ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/PythagoreDoubleTriangleA.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Mesures manquantes}%
La somme des angles dans un triangle mesurant 180°, l'angle $\alpha$ mesure \{alpha}°\\%
cos($\alpha$)=$\dfrac{CH}{BC}$\\%
Donc, CH = AB $\times$ cos($\alpha$) $\simeq$ \{CH} cm\\%
cos($\theta$)=$\dfrac{CH}{AC}$\\%
Donc, AC = $\dfrac{CH}{cos(\theta)} \simeq$ \{AC} cm\\%
cos($\alpha$)=$\dfrac{AH}{AC}$\\%
Donc, AH = AC $\times$ cos($\alpha$) $\simeq$ \{AH} cm\\%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
\exo{Mesures manquantes}%
\begin{minipage}{0.6\textwidth}%
ABC est le triangle ci-contre.\\%
AC = \{AC} cm et l'angle $\alpha$ mesure \{alpha}°\\%
Combien mesure BH ?\\%
\end{minipage}%
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{imagesQuatrieme/PythagoreDoubleTriangleA.png}%
\end{minipage}\\%
'''
    mainC = r'''\cor{Mesures manquantes}%
La somme des angles dans un triangle mesurant 180°, l'angle $\theta$ mesure \{theta}°\\%
cos($\theta$)=$\dfrac{CH}{AC}$\\%
Donc, CH = AC $\times$ cos($\theta$) $\simeq$ \{CH} cm\\%
cos($\alpha$)=$\dfrac{CB}{CH}$\\%
Donc, BC = $\dfrac{CH}{cos(\theta)} \simeq$ \{BC} cm\\%
cos($\theta$)=$\dfrac{BC}{BH}$\\%
Donc, BH = $\dfrac{BC}{cos(\theta)} \simeq$ \{BH} cm\\%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    ppcmVal = fonctionsSupplementaires.PPCM(dens)
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
    pgcdVal = fonctionsSupplementaires.PGCD([numerator, ppcmVal])
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
    
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def pileOuFace(fileExercices, fileCorrections):
    """Exercice type de statistique/probabilité"""

    elPerLign = 10
    n = random.randint(20, 50)
    nLign = (n - 1) // elPerLign + 1
    listePrenoms = ['Paul', 'Pierre', 'Marie', 'Margot', 'Fanny',
                    'Jean', 'Julie', 'Adrien', 'Thomas', 'Suzanne', 'Philippe']
    nomA = np.random.choice(listePrenoms)
    listePrenoms.remove(nomA)
    nomB = np.random.choice(listePrenoms)
    fP = 0
    nP = 0
    nF = 0
    compteur = 0

    main = r'''\exo{Pile ou Face ?}%
Deux amis, \{nomA} et \{nomB} jouent à "Pile ou Face". Ils ont effectué les \{n} lancers suivants :\\%
\begin{center}
\begin{tabular}{|*{\{elPerLign}}{c|}}
'''
    for i in range(nLign):
        main += r'''\hline
'''
        for j in range(i*elPerLign, min((i+1)*elPerLign, n)):
            pOf = np.random.choice([r'pile', r'face'])
            if pOf == 'pile':
                nP += 1
            else:
                nF += 1
            if (j+1) % elPerLign == 0:
                pOf += r'''\\%
'''
            else:
                pOf += r'&'
            main += pOf
        fP = nP/n   # Fréquence d'apparition des piles
        fF = nF/n   # Fréquence d'apparition des faces
        pP = n/2
    if (j + 1) % elPerLign != 0:
        for j in range((elPerLign - 1) - (n % elPerLign)):
            main += r'&'
        main += r'''\\
'''
    main += r'''
\hline%
'''
    main += r'''\end{tabular}
\end{center}
\{nomA} affirme que le fréquence statistique d'apparition des piles est plus importantes que la probabilité 
théorique. Est-ce vrai ?
'''
    eq = '='
    if fP != round(fP, 3):
        fP = round(fP, 3)
        eq = '\simeq'
    mainC = r'''\cor{Pile ou Face ?}%
\{nomA} a effectué \{n} lancés. Comme pour chaque lancé il y a une chance sur deux que ce soit un pile, le 
nombre de piles théorique est de 0.5. Cependant, la fréquence statististique d'apparition est  
de $\dfrac{\{nP}}{\{n}} \{eq} \{fP}$.\\
'''
    if fP > 0.5:
        mainC += r'''$\{fP} > 0.5$, on a donc bien une fréquence statistique supérieure à la probabilité théorique.\\
\{nomA} a bien raison.
'''
    else:
        mainC += r'''$\{fP} \leq 0.5$, on a donc une fréquence statistique inférieure ou égale à la probabilité théorique.\\
\{nomA} a tord.
'''

    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def statsClasse(fileExercices, fileCorrections):
    """Exercice type de statistique/probabilité en comparant 2 classes"""

    elPerLign = 10
    n = random.randint(20, 30)
    nLign = (n - 1) // elPerLign + 1
    fP = 0
    nP = 0
    nF = 0
    compteur = 0

    main = r'''\exo{Homogénéité des classes.}%
Deux classes, A et B, composées chacune de \{n} élèves ont effectué un devoir de Mathématiques. Les notes obtenues 
sont les suivantes.\\%

\begin{minipage}{0.45\textwidth}
\begin{center}
Classe A :\\
\medskip
\begin{tabular}{|*{\{elPerLign}}{c|}}
'''
    notes1 = []
    for i in range(nLign):
        main += r'''\hline
'''
        for j in range(i*elPerLign, min((i+1)*elPerLign, n)):
            note = random.randint(0, 10)
            notes1.append(note)
            note = str(note)
            if (j+1) % elPerLign == 0:
                note += r'''\\%
'''
            else:
                note += r'&'
            main += note
        moyenne1 = np.mean(notes1)   # Fréquence d'apparition des piles
        mediane1 = np.median(notes1)   # Fréquence d'apparition des faces
        etendue1 = np.max(notes1) - np.min(notes1)
    if (j + 1) % elPerLign != 0:
        for j in range((elPerLign - 1) - (n % elPerLign)):
            main += r'&'
        main += r'''\\
'''
    main += r'''
\hline%
'''
    main += r'''\end{tabular}
\end{center}
\end{minipage}%
\begin{minipage}{0.45\textwidth}
\begin{center}
Classe B :\\
\medskip
\begin{tabular}{|*{\{elPerLign}}{c|}}
'''
    notes2 = []
    for i in range(nLign):
        main += r'''\hline
'''
        for j in range(i*elPerLign, min((i+1)*elPerLign, n)):
            note = random.randint(0, 10)
            notes2.append(note)
            note = str(note)
            if (j+1) % elPerLign == 0:
                note += r'''\\%
'''
            else:
                note += r'&'
            main += note
        moyenne2 = np.mean(notes2)   # Fréquence d'apparition des piles
        mediane2 = np.median(notes2)   # Fréquence d'apparition des faces
        etendue2 = np.max(notes2) - np.min(notes2)
    if (j + 1) % elPerLign != 0:
        for j in range((elPerLign - 1) - (n % elPerLign)):
            main += r'&'
        main += r'''\\
'''
    main += r'''
\hline%
'''
    main += r'''\end{tabular}
\end{center}
\end{minipage}%
\medskip
\begin{enumerate}
\item Calculer la moyenne, médiane et étendue de la classe A.
\item Calculer la moyenne, médiane et étendue de la classe B.
\item Comparez, si possible, les classes A et B.
\end{enumerate}
'''
    moy1, med1, et1, moy2, med2, et2 = moyenne1, mediane1, etendue1, moyenne2, mediane2, etendue2
    if moy1 == round(moy1, 3):
        moy1 = ' = ' + str(moy1)
    else:
        moy1 = ' \simeq ' + str(round(moy1, 3))
    if moy2 == round(moy2, 3):
        moy2 = ' = ' + str(moy2)
    else:
        moy2 = ' \simeq ' + str(round(moy2, 3))
    if med1 == round(med1, 3):
        med1 = ' = ' + str(med1)
    else:
        med1 = ' \simeq ' + str(round(med1, 3))
    if med2 == round(med2, 3):
        med2 = ' = ' + str(med2)
    else:
        med2 = ' \simeq ' + str(round(med2, 3))
    if et1 == round(et1, 3):
        et1 = ' = ' + str(et1)
    else:
        et1 = ' \simeq ' + str(round(et1, 3))
    if et2 == round(et2, 3):
        et2 = ' = ' + str(et2)
    else:
        et2 = ' \simeq ' + str(round(et2, 3))
    moyenne1, moyenne2 = round(moyenne1, 3), round(moyenne2, 3)
    mediane1, mediane2 = round(mediane1, 3), round(mediane2, 3)
    etendue1, etendue2 = round(etendue1, 3), round(etendue2, 3)

    mainC = r'''\cor{Homogénéité des classes.}%
\begin{enumerate}
\item Pour la classe A, la moyenne vaut $m_A \{moy1}$, la médiane $med_A \{med1}$ et l'étendue $E_A \{et1}$.\\ 
L'écart entre la moyenne et la médiane est \{abs(round(moyenne1 - mediane1, 3))}.
\item Pour la classe B, la moyenne vaut $m_B \{moy2}$, la médiane $med_B \{med2}$ et l'étendue $E_B \{et2}$.\\
L'écart entre la moyenne et la médiane est \{abs(round(moyenne2 - mediane2, 3))}.
'''
    if abs(moyenne1 - mediane1) < abs(moyenne2 - mediane2):
        if etendue1 < etendue2:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est inférieur à celui de la classe B et 
l'étendue de la classe A est inférieure à celle de la classe B donc la classe A est plus homogène que la classe B.
'''
        elif etendue1 > etendue2:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est inférieur à celui de la classe B mais 
l'étendue de la classe A est supérieure à celle de la classe B donc on ne peut pas comparer les classes.
'''
        else:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est inférieur à celui de la classe B et 
l'étendue de la classe A est égale à celle de la classe B donc la classe A est plus homogène que la B.
'''
    elif abs(moyenne1 - mediane1) > abs(moyenne2 - mediane2):
        if etendue1 > etendue2:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est supérieur à celui de la classe B et 
l'étendue de la classe A est supérieure à celle de la classe B donc la classe A est moins homogène que 
la classe B.
'''
        elif etendue1 < etendue2:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est supérieur à celui de la classe B mais 
l'étendue de la classe A est inférieure à celle de la classe B donc on ne peut pas comparer les classes.
'''
        else:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est supérieur à celui de la classe B et 
l'étendue de la classe A est égale à celle de la classe B donc la classe B est plus homogène que la A.
'''
    else :
        if etendue1 > etendue2:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est égal à celui de la classe B et 
l'étendue de la classe A est supérieure à celle de la classe B donc la classe A est moins homogène que 
la classe B.
'''
        elif etendue1 < etendue2:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est égal à celui de la classe B mais 
l'étendue de la classe A est inférieure à celle de la classe B donc la classe A est plus homogène 
que la classe B.
'''
        else:
            mainC += r'''\item L'écart moyenne/médiane de la classe A est égal à celui de la classe B et 
l'étendue de la classe A est égale à celle de la classe B donc les classes ne sont pas comparables.
'''
    mainC += r'''
\end{enumerate}
'''

    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def probasRoueSac(fileExercices, fileCorrections):
    """Exercice sur les probabilités nécessitants un arbre. Basé sur une roue et un sac."""

    pA = round(pApercent / 100, 2)
    pB = round(pBpercent / 100, 2)
    pDa = round(pDaPercent / 100, 2)
    pDb = round(pDbPercent / 100, 2)
    pDaBar = round(1 - pDa, 2)
    pDbBar = round(1 - pDb, 2)
    pAandD = round(pA * pDa, 4)
    pAandDbar = round(pA * (1 - pDa), 4)
    pBandD = round(pB * pDb, 4)
    pBandDbar = round(pB * (1 - pDb), 4)
    pD = round(pAandD + pBandD, 4)
    # Fin des variables.

    # Enoncé de l'exercice.
    main = r'''\exo{Un gâchis monstre...}%
Une grande entreprise produit deux types de viennoiseries : des \{vienA} et des \{vienB}.\\%
Les employés travaillants à l'empaquetage de ces viennoiseries sont chargés de contrôler la perfection
de ces dernières. Si elles ne le sont pas, elles devront alors être jetées. (Malgré le gâchis que cela implique).\\%
On sait que \{pApercent}\% de la production vient d'une partie rénovée de l'usine,
le reste vient de la vieille partie de l'usine (avec son lot de défauts !)\\%
On sait que, statistiquement, seulement \{pDaPercent}\% des gâteaux venant de la partie rénovée de l'usine
ont un défaut, alors qu'il y en a \{pDbPercent}\% en provenance de la vielle partie de l'usine.\\%
On choisit un gâteau au hasard dans la production.\\%
On considère les événements :\\%
A : "la viennoiserie vient de la partie rénovée de l'usine"\\%
B : "la viennoiserie vient de la vieille partie de l'usine"\\%
D : "la viennoiserie a un défaut".\\%

\begin{enumerate}[label=\alph*)]%
    \item Faire un arbre de choix modélisant la situation de l'énoncé.%
    \item Déterminer la probabilité pour que la viennoiserie vienne de la partie rénovée de l'usine et ait un défaut.%
    \item Quelle est la probabilité pour la viennoiserie soit rejetée ?%
\end{enumerate}%
'''
    # Fin de l'énoncé.

    # Fichier texte de la correction.
    mainC = r'''\cor{Un gâchis monstre...}%
\begin{center}
\begin{tikzpicture}
    \tikzstyle{level 1}=[level distance=6cm, sibling distance=5cm]
    \tikzstyle{level 2}=[level distance=6cm, sibling distance=3.5cm]
    \node{}[grow=right]
    child{node{$B$}
      child{node{$B\cap \overline D$} edge from parent node[below]{\textcolor{red}{$\{pDbBar}$}}}
      child{node{\textcolor{blue}{$B\cap D$}}           edge from parent node[above]{\textcolor{red}{$\{pDb}$}}}
      edge from parent node[below]{\textcolor{red}{\textcolor{red}{$\{pB}$}}}}
    child{node{$A$}
      child{node{$A\cap \overline D$} edge from parent node[below]{\textcolor{red}{$\{pDaBar}$}}}
      child{node{\textcolor{blue}{$A\cap D$}} edge from parent node[above]{\textcolor{red}{$\{pDa}$}}}
      edge from parent node[above]{\textcolor{red}{$\{pA}$}}};
\end{tikzpicture}
\end{center}
\begin{enumerate}[label=\alph*)]%
\item Le problème peut être modélisé par l'arbre ci-dessus.
\item La probabilité que la viennoiserie vienne de la partie rénovée de l'usine et ait un défaut est la
probabilité de l'événement \textcolor{blue}{$A \cap D$} qui vaut : p(\textcolor{blue}{$A \cap D$}) =
$\{pA} \times \{pDa}$ = \{pAandD}.\\%
La probabilité que la partie rénovée vienne de la partie rénovée de l'usine et ait un défaut est de \{pAandD}.\\%
\item  La probabilité pour la viennoiserie d'être rejetée correspond à la première et troisième branche de l'arbre.
C'est à dire aux évènements \textcolor{blue}{$A \cap D$} et \textcolor{blue}{$B \cap D$}.
La probabilité de l'événement \textcolor{blue}{$A \cap D$} a déjà été calculé. La probabilité de l'événement
\textcolor{blue}{$B \cap D$} vaut quant à elle p(\textcolor{blue}{$B \cap D$}) = $\{pB} \times \{pDb}$ = \{pBandD}.\\%
On a donc, finalement, p(D) = p(\textcolor{blue}{$A \cap D$})
+ p(\textcolor{blue}{$B \cap D$}) = \{pAandD} + \{pBandD} = \{pD}.\\%
La probabilité que la viennoiserie soit rejetée est donc de \{pD}.\\%
\end{enumerate}
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
