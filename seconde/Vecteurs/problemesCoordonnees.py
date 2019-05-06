#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
import fonctionsSimplifiantes


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
    mainC = fonctionsSimplifiantes.repereDebut(mainC, -6, -8, 9, 6)
    mainC += r'''\path[draw, red] (\{xA}, \{yA})  coordinate [label= left:$A$] (A) --
(\{xB}, \{yB})  coordinate [label=above:$B$] (B) -- (\{xC}, \{yC})  coordinate [label=right:$C$] (C) --
(\{xD}, \{yD})  coordinate [label=right:$D$] (D) -- cycle;%
'''
    mainC = fonctionsSimplifiantes.repereFin(mainC)
    mainC += r'''$\coordv{BA}{x_A - x_B}{y_A - y_B}$. Donc, $\coordv{BA}{\{xA} - (\{xB})}{\{yA} - \{yB}}$.
Ainsi, $\coordv{BA}{\{xBA}}{\{yBA}}$\\%

$\coordv{CD}{x_D - x_C}{y_D - y_C}$. Donc, $\coordv{CD}{\{xD} - \{xC}}{\{yD} - \{yC}}$.
Ainsi, $\coordv{CD}{\{xCD}}{\{yCD}}$\\%

$\vv{BA}=\vv{CD}$, donc, ABCD est un parallèlogramme.
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    mainC = fonctionsSimplifiantes.repereDebut(mainC, -6, -8, 9, 6)
    mainC += r'''\path[draw, red] (\{xA}, \{yA})  coordinate [label= left:$A$] (A) --
(\{xB}, \{yB})  coordinate [label=above:$B$] (B) -- (\{xC}, \{yC})  coordinate [label=right:$C$] (C) --
(\{xD}, \{yD})  coordinate [label=right:$D$] (D) -- cycle;%
'''
    mainC = fonctionsSimplifiantes.repereFin(mainC)
    mainC += r'''$\coordv{BA}{x_A - x_B}{y_A - y_B}$. Donc, $\coordv{BA}{\{xA} - (\{xB})}{\{yA} - \{yB}}$.
Ainsi, $\coordv{BA}{\{xBA}}{\{yBA}}$\\%

$\coordv{CD}{x_D - x_C}{y_D - y_C}$. Donc, $\coordv{CD}{\{xD} - \{xC}}{\{yD} - \{yC}}$.
Ainsi, $\coordv{CD}{\{xCD}}{\{yCD}}$\\%

$\vv{BA} \neq \vv{CD}$, donc, ABCD n'est pas un parallèlogramme.%
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


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
    mainC = fonctionsSimplifiantes.repereDebut(mainC, xA - 1, yA - 1, max(xC + 1, 1), max(yC + 1, 1))
    mainC += r'''\node[text=red, cross=3pt, label=right:\textcolor{red}{A}] at (\{xA}, \{yA}) {};\\
\node[text=red, cross=3pt, label=right:\textcolor{red}{B}] at (\{xB}, \{yB}) {};\\
\node[text=red, cross=3pt, label=right:\textcolor{red}{C}] at (\{xC}, \{yC}) {};\\
'''
    mainC = fonctionsSimplifiantes.repereFin(mainC)
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
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
