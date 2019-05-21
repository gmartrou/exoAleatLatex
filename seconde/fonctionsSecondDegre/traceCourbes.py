#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
import fonctionsSimplifiantes
from math import sqrt
from fonctionsSimplifiantes import signOpT, signT, signE, signOpE


def fonctionsSecondDegreTrace(fileExercices, fileCorrections):
    """Tracé d'une fonction du second degré en utilisant les formes canoniques, factorisées et développées."""
    
    a, al, beSa = 0, 0, 0
    
    while -2 * a * al == 0 or a*beSa + a * al**2 == 0 or abs(a*beSa) > 30:
        a1 = random.randint(2, 6)
        a2 = random.randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = random.randint(1, 6)
        b2 = random.randint(-6, -1)
        al = np.random.choice([b1, b2])
        beSa = np.random.choice([-1, -4, -9, -16, -25, -36])
    
    sBeSa = int(sqrt(-beSa))
    be = int(a*beSa)
    b = int(-2 * a * al)
    c = int(be + a * al**2)
    de = int(al + sqrt(-beSa))
    ga = int(al - sqrt(-beSa))
    
    xmin = -10
    ymin = -10
    xmax = 10
    ymax = 10

    signB, signC = ' + ', ' + '
    absB, absC = b, c
    if b < 0:
        signB = r' - '
        absB = abs(b)
    if c < 0:
        signC = r' - '
        absC = abs(c)
    signBe = ' + '
    signMAl, signAl = ' - ', ' + ',
    signMDe, signDe = ' - ', ' + ',
    signMGa, signGa = ' - ', ' + ',
    absAl, absBe, absDe, absGa = al, be, de, ga
    if al < 0:
        signAl = r' - '
        signMAl = r' + '
        absAl = abs(al)
    if de < 0:
        signDe = r' - '
        signMDe = r' + '
        absDe = abs(de)
    if ga < 0:
        signGa = r' - '
        signMGa = r' + '
        absGa = abs(ga)
    if be < 0:
        signBe = r' - '
        absBe = abs(be)

    main = r'''\exo{Tracé d'une fonction de degré 2}%
Soit $f$ la fonction définie sur $\R$ par $f(x) = \{a}x^2 \{signB} \{absB}x \{signC} \{absC}$.
\medskip%
\begin{enumerate}%
\item Tracer la courbe représentative de $f$ dans le plan muni d'un repère.%
\end{enumerate}%
'''
    mainC = r'''\cor{Tracé d'une fonction de degré 2}
\medskip%
\begin{enumerate}%
\item $f(x) = \{a}x^2 \{signE(b)}x \{signE(c)}$.\\
On factorise par \{a} : $f(x) = \{a}[x^2 \{signE(b/a)} x \{signE(c/a)}]$\\
'''
    if b/a > 0:
        mainC += r'''On remarque que $\{int(b/a)} = 2 \times \{int(b/(2*a))}$.
'''
    else:
        mainC += r'''On remarque que $\{int(b/a)} = 2 \times (\{int(b/(2*a))})$.
'''
    mainC += r'''Donc $x^2 \{signE(b/a)} x \{signE(c/a)}$ est une expression proche de $(x \{signOpE(al)})^2$.\\
En développant, on remarque que $(x \{signOpE(al)})^2 = x^2 \{signOpE(2*al)}x \{signE(al**2)}$.\\
Donc $(x \{signOpE(al)})^2 \{signE(c/a - al**2)} = x^2 \{signE(b/a)} x \{signE(c/a)}$.\\
Ainsi, $f(x) = \{a}[(x \{signOpE(al)})^2 \{signE(c/a - al**2)}] = \{a}(x \{signMAl} \{absAl})^2 \{signBe} \{absBe}$.\\
'''
    if al > 0:
        mainC += r'''La forme canonique de $f(x)$ est donc $f(x) = \{a}(x \{signMAl} \textcolor{red}{\{absAl}})^2
\textcolor{red}{\{signBe} \{absBe}}$.\\'''
    else:
        mainC += r'''La forme canonique de $f(x)$ est donc $f(x) = \{a}(x \{signMAl} \{absAl})^2 \{signBe} \{absBe} =
\{a}(x - (\textcolor{red}{- \{absAl}}))^2 \textcolor{red}{\{signBe} \{absBe}}$.\\
'''
    mainC += r'''Le sommet de la parabole est donc le point S(\textcolor{red}{\{al}}; \textcolor{red}{\{be}}).\\

On remarque que $\{-beSa} = \{sBeSa}^2$, on peut donc utiliser l'identité remarquable $a^2 - b^2 = (a-b)(a+b)$.\\
Soit, $f(x) = \{a}[(x \{signOpE(al)})^2 \{signE(beSa)}] = \{a}[(x \{signOpE(al)})^2 - \{sBeSa}^2] =
\{a}(x \{signOpE(al)} \{signOpE(sBeSa)})(x \{signOpE(al)} \{signE(sBeSa)}) =
\{a}(x \{signOpE(al+sBeSa)})(x \{signOpE(al-sBeSa)})$.\\
La forme factorisée de f(x) est donc $f(x) = \{a}(x \{signMDe} \{absDe})(x \{signMGa} \{absGa})$.\\
La fonction f \textcolor{red}{s'annule} donc en $x = \textcolor{blue}{\{de}}$ et en $x = \textcolor{blue}{\{ga}}$.\\
La parabole passe donc par les points A(\textcolor{blue}{\{de}}; \textcolor{red}{0})
 et B(\textcolor{blue}{\{ga}}; \textcolor{red}{0}).\\
'''
    if a>0:
        mainC += r'''Comme $\{a}>0$, la parabole est "contente", elle sera décroissante puis croissante.\\
'''
    else:
        mainC += r'''Comme $\{a}<0$, la parabole est "triste", elle sera croissante puis décroissante.\\
'''
    mainC += r'''La fonction f peut donc être représentée par la courbe suivante :
\end{enumerate}
'''
    mi = min(de, ga)
    ma = max(de, ga)
    if a < 0:
        mainC = fonctionsSimplifiantes.repereDebut(mainC, min(mi - 2, -10), -10, max(ma + 2, 10), max(be + 2, 10))
    else:
        mainC = fonctionsSimplifiantes.repereDebut(mainC, min(mi - 2, -10), min(be - 2, -10), max(ma + 2, 10), 10)
    # mainC = fonctionsSimplifiantes.repereDebut(mainC, xmin, ymin, xmax, ymax)
    mainC += r'''\addplot[color=red,domain=\{mi - 2}:\{ma + 2}, samples=300]{\{a}*x*x \{signE(b)}*x \{signE(c)}};
\node[blue, cross=3pt] at (\{de}, 0) {};\\
\node[blue, cross=3pt] at (\{ga}, 0) {};\\
\node[blue, cross=3pt] at (\{al}, \{be}) {};\\
\node[text=blue, right] at (\{de}, 0) {A};\\
\node[text=blue, right] at (\{ga}, 0) {B};\\
\node[text=blue, right] at (\{al}, \{be}) {S};\\
'''
    mainC = fonctionsSimplifiantes.repereFin(mainC)
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def fonctionsHomographiqueTrace(fileExercices, fileCorrections):
    """Tracé d'une fonction homographique."""
    
    a, b, c, d = 0, 0, 0, 0
    
    while a*d - b*c == 0 or round(d/c, 3) != d/c or round(a/c, 3) != a/c:
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
    
    main = r'''\exo{Tracé d'une fonction homographique}%
Soit $f$ la fonction définie sur $\R$ par $f(x) = \dfrac{\{a}x \{signE(b)}}{\{c}x \{signE(d)}}$.
\medskip%
\begin{enumerate}%
\item Justifier que $f$ est une fonction homographique.%
\item Quel est l'ensemble de définition de $f$ ?%
\item Tracer la courbe représentative de $f$ dans le plan muni d'un repère.%
\end{enumerate}%
'''
    mainC = r'''\cor{Tracé d'une fonction homographique}
\medskip%
\begin{enumerate}%
\item $f(x) = \dfrac{\{a}x \{signE(b)}}{\{c}x \{signE(d)}}$.
La fonction $f$ est une fonction du type $f(x) = \dfrac{a x + b}{c x + d}$ avec a = \{a}, b = \{b}, c = \{c} et
d = \{d} et $ad - bc = \{a*d - b*c} \neq 0$ donc $f$ est bien une fonction homographique.%
\item La fonction n'est pas définie lorsque le dénominateur s'annule car il est interdit de diviser par 0.\\
Or, $\{c} x \{signE(d)} = 0 => x = \{-d/c}$. $f$ est donc définie sur $\R \setminus \lbrace{\{-d/c}}\rbrace$.
\item $f$ est donc définie sur $\R \setminus \lbrace{\{-d/c}}\rbrace$, on sait donc que la fonction aura pour
tangente verticale la droite d'équation $x = \{-d/c}$.\\
Pour des valeurs "très grandes" ou "très petites" de $x$, les coefficients "b" et "d" n'auront pas d'impact
sur la valeur de la fonction et celle-ci tendra vers une valeur constante, $\dfrac{a}{c} = \dfrac{\{a}}{\{c}} = \{a/c}$.\\
La fonction aura donc pour tangente horizontale la droite d'équation $y = \{a/c}$.\\
'''
    if a*d - b*c > 0:
        mainC += r'''Comme $ad - bc = \{a*d - b*c} > 0$, la fonction est croissante.\\
'''
    else:
        mainC += r'''Comme $ad - bc = \{a*d - b*c} < 0$, la fonction est décroissante.\\
'''
    mainC += r'''La fonction $f$ peut donc être représentée par la courbe suivante :
\end{enumerate}
'''
    ymin = int(a / c) - 6
    ymax = int(a / c) + 6
    xmin = int(-d / c) - 6
    xmax = int(-d / c) + 6
    mainC = fonctionsSimplifiantes.repereDebut(mainC, xmin, ymin, xmax, ymax)
    mainC += r'''\addplot[color=red,domain=\{-10}:\{10}, samples=300]{(\{a}*x \{signE(b)})/(\{c}*x \{signE(d)})};
\addplot[dashed, color=blue,domain=\{-10}:\{10}] coordinates {(\{-d/c}, \{ymin})(\{-d/c}, \{ymax})};
\addplot[dashed, color=blue,domain=\{-10}:\{10}, samples=300]{\{a/c}};
'''
    mainC = fonctionsSimplifiantes.repereFin(mainC)
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


