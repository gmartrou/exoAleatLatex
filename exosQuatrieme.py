from random import *
import numpy as np
from math import *
from fonctionsSupplementaires import *
from fonctionsSimplifiantes import *

def pythagore1(fileExercices, fileCorrections):
    a = randint(1, 10)
    b = randint(a + 1, 15)
    ac = a ** 2
    bc = b ** 2
    di = sqrt(bc - ac)
    ro = round(sqrt(di), 2)

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
    localV = locals()
    return endExercice(main, mainC, fileExercices, fileCorrections, localV)


def pythagore2(fileExercices, fileCorrections):
    a = randint(1, 15)
    b = randint(1, 15)
    ac = a**2
    bc = b**2
    sum = ac + bc
    sqSum = sqrt(sum)
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
BC$^2$ = \{sum}\\%
BC = $\sqrt{\{sum}}$ cm\\%
'''
    if sum == ro:
        mainC += r'''BC = \{sqSum} cm\\%
'''
    else:
        mainC += r'''BC $\simeq$ \{sqSum} cm\\%
'''
    localV = locals()
    return endExercice(main, mainC, fileExercices, fileCorrections, localV)


def pythagore3(fileExercices, fileCorrections):
    a = randint(1, 10)
    b = randint(a + 1, 15)
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
    localV = locals()
    return endExercice(main, mainC, fileExercices, fileCorrections, localV)


def pythagore4(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'\exo{Théorème de Pythagore}%' + '\n'
    main += r'ABC est un triangle.\\%' + '\n'
    a = randint(1, 15)
    b = randint(1, 15)
    c = sqrt(a ** 2 + b ** 2)
    c = round(c, 3)
    main += r'AB = ' + str(a) + r' cm.\\%' + '\n'
    main += r'AC = ' + str(b) + r' cm.\\%' + '\n'
    main += r'BC = ' + str(c) + r' cm.\\%' + '\n'
    main += r"ABC est-il rectangle ? (Si les valeurs sont juste à 1 chiffre après la virgule, c'est bon)\\%" + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Théorème de Pythagore}%' + '\n'
        mainC += r'BC est le plus grand côté.\\%' + '\n'
        mainC += r'BC$^2$ = ' + str(c) + r'$^2$\\%' + '\n'
        mainC += r'BC$^2$ = ' + str(c ** 2) + r'\\%' + '\n'
        mainC += r'AB$^2$ + AC$^2 = $' + str(a ** 2) + r' + ' + str(b ** 2) + r'\\%' + '\n'
        mainC += r'AB$^2$ + AC$^2 = $' + str(a ** 2 + b ** 2) + r'\\%' + '\n'
        if (a ** 2 + b ** 2) == c ** 2:
            mainC += r'BC$^2$ = AB$^2$ + AC$^2$\\%' + '\n'
        else:
            mainC += r'\`{A} 1 chiffre après la virgule près, on a :\\%' + '\n'
            mainC += r'BC$^2$ = AB$^2$ + AC$^2$\\%' + '\n'
        mainC += r"Donc, d'après la réciproque du théorème de Pythagore ABC est rectangle en B.\\%" + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def pythagore5(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'\exo{Théorème de Pythagore}%' + '\n'
    main += r'ABC est un triangle.\\%' + '\n'
    a = randint(1, 15)
    b = randint(1, 15)
    if random() > 0.5:
        c = sqrt(a ** 2 + b ** 2) + random()
    else:
        c = sqrt(a ** 2 + b ** 2) - random()
    c = round(c, 3)
    main += r'AB = ' + str(a) + r' cm.\\%' + '\n'
    main += r'AC = ' + str(b) + r' cm.\\%' + '\n'
    main += r'BC = ' + str(c) + r' cm.\\%' + '\n'
    main += r"ABC est-il rectangle ? (Si les valeurs sont juste \`{a} 1 chiffre après la virgule, c'est bon)\\%" + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Théorème de Pythagore}\\%' + '\n'
        mainC += r'BC est le plus grand côté.\\%' + '\n'
        mainC += r'BC$^2$ = ' + str(c) + r'$^2$\\%' + '\n'
        mainC += r'BC$^2$ = ' + str(c ** 2) + r'\\%' + '\n'
        mainC += r'AB$^2$ + AC$^2 = $ ' + str(a ** 2) + r' + ' + str(b ** 2) + r'\\%' + '\n'
        mainC += r'AB$^2$ + AC$^2 = $ ' + str(a ** 2 + b ** 2) + r'\\%' + '\n'
        if (a ** 2 + b ** 2) == c ** 2:
            mainC += r'\`{A} 1 chiffre après la virgule près, on a :\\%' + '\n'
            mainC += r'BC$^2$ = AB$^2$ + AC$^2$\\%' + '\n'
            mainC += r"Donc, d'après la réciproque du théorème de Pythagore ABC est rectangle en B.\\%" + '\n'
        else:
            mainC += r'On a :\\%' + '\n'
            mainC += r'BC$^2$ $\neq$ AB$^2$ + AC$^2$\\%' + '\n'
        mainC += r"Donc, d'après la contraposée du théorème de Pythagore ABC n'est pas rectangle.\\%" + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def equation1(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'''\exo{Résolution d'équation}'''
    a = randint(2, 15)
    b = randint(1, 15)
    c = randint(2, 15)
    d = randint(1, 15)
    main += r'Trouver la valeur de $x$ vérifiant :\\%' + '\n'
    main += str(a) + r'$x$ + ' + str(b) + ' $=$ ' + str(c) + r'$x$ + ' + str(d) + r'\\%' + '\n'
    main += '\n'
    if correction:
        mainC += r'''\cor{Résolution d'équation}'''
        mainC += str(a) + r'$x$ + ' + str(b) + ' $=$ ' + str(c) + r'$x$ + ' + str(d) + r'\\%' + '\n'
        if a < c:
            mainC += r'On retire ' + str(a) + r'$x$ de chaque côté : %'
            if a == c:
                mainC += str(b) + ' $=$ ' + str(d) + r'\\%' + '\n'
                if b == d:
                    mainC += r'Cela est vrai pour toutes les valeurs de $x$\\%' + '\n'
                else:
                    mainC += r"Cela n'est vrai pour aucune valeur de $x$\\%" + '\n'
            else:
                mainC += str(b) + ' $=$ ' + str(c - a) + r'$x$ + ' + str(d) + r'\\%' + '\n'
                mainC += r'On retire ' + str(d) + r' de chaque côté : '
                mainC += str(b - d) + ' $=$ ' + str(c - a) + r'$x$\\%' + '\n'
                mainC += r'On divise par ' + str(c - a) + r' de chaque côté : '
                mainC += r'$\dfrac{' + str(b - d) + r'}{' + str(c - a) + r'}=x$\\%' + '\n'
                if round((b - d) / (c - a), 2) == ((b - d) / (c - a)):
                    if b == d:
                        mainC += r'$x = 0$\\%' + '\n'
                    else:
                        mainC += r'$x = $ ' + str((b - d) / (c - a)) + r'\\%' + '\n'
                else:
                    mainC += r'$x \simeq$ ' + str(round((b - d) / (c - a), 2)) + r'\\%' + '\n'
        else:
            mainC += r'On retire ' + str(c) + r'$x$ de chaque côté : '
            if a == c:
                mainC += str(b) + ' $=$ ' + str(d) + r'\\%' + '\n'
                if b == d:
                    mainC += r'Cela est vrai pour toutes les valeurs de $x$\\%' + '\n'
                else:
                    mainC += r"Cela n'est vrai pour aucune valeur de $x$\\%" + '\n'
            else:
                mainC += str(a - c) + r'$x$ + ' + str(b) + ' $=$ ' + str(d) + r'\\%' + '\n'
                mainC += r'On retire ' + str(b) + r' de chaque côté : '
                mainC += str(a - c) + r'$x =$ ' + str(d - b) + r'\\%' + '\n'
                mainC += r'On divise par ' + str(a - c) + r' de chaque côté : '
                mainC += r'$x = \dfrac{' + str(d - b) + r'}{' + str(a - c) + r'}$\\%' + '\n'
                if round((b - d) / (c - a), 2) == ((b - d) / (c - a)):
                    if b == d:
                        mainC += r'$x = 0$\\%' + '\n'
                    else:
                        mainC += r'$x = $ ' + str((b - d) / (c - a)) + r'\\%' + '\n'
                else:
                    mainC += r'$x \simeq$ ' + str(round((b - d) / (c - a), 2)) + r'\\%' + '\n'
            mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def equation2(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'''\exo{Résolution d'équation}'''
    pasBon = True
    listePrenoms = ['Paul', 'Pierre', 'Marie', 'Margot', 'Fanny',
                    'Jean', 'Julie', 'Adrien', 'Thomas', 'Suzanne', 'Philippe']
    a, b, c, ans = 0, 0, 0, 0
    while pasBon:
        a = randint(1, 30)
        b = randint(31, 60)
        c = randint(2, 4)
        ans = (b - c * a) / (c - 1)
        if (ans == int(ans)) and ((b - a) > 1):
            ans = int(ans)
            pasBon = False
    nomA = np.random.choice(listePrenoms)
    listePrenoms.remove(nomA)
    nomB = np.random.choice(listePrenoms)
    main += nomA + r' a ' + str(b - a) + r' ans de plus que ' + nomB + r'.\\%' + '\n'
    if b / a > c:
        if ans == 1:
            main += r'Dans ' + str(ans) + ' an ' + nomA + r' aura ' + str(c) + \
                    r" fois l'âge de " + nomB + r'.\\%' + '\n'
        else:
            main += r'Dans ' + str(ans) + ' ans ' + nomA + r' aura ' + str(c) + \
                    r" fois l'âge de " + nomB + r'.\\%' + '\n'
    else:
        if ans == 1:
            main += r'Il y a ' + str(-ans) + ' an ' + nomA + r' avait ' + str(c) + \
                    r" fois l'âge de " + nomB + r'.\\%' + '\n'
        else:
            main += r'Il y a ' + str(-ans) + ' ans ' + nomA + r' avait ' + str(c) + \
                    r" fois l'âge de " + nomB + r'.\\%' + '\n'
    main += r'Quels sont leurs âges respectifs actuellement ?\\%' + '\n'
    main += '\n'
    if correction:
        mainC += r"\cor{Résolution d'équation}"
        mainC += r'''Notons $x$:"L'âge de ''' + nomA + r'"\\%' + '\n'
        mainC += r'''Notons $y$:"L'âge de ''' + nomB + r'"\\%' + '\n'
        mainC += r'On a les deux équations suivantes : \\%' + '\n'
        mainC += r'$x$ = $y$ + ' + str(b - a) + r'\\%' + '\n'
        if ans > 0:
            mainC += r'$x$ + ' + str(ans) + r' = ' + str(c) + r'($y + $' + str(ans) + r')\\%' + '\n'
            mainC += r'On remplace $x$ par $y$ + ' + str(b - a) + r'\\%' + '\n'
            mainC += r'$y$ + ' + str(b - a) + r' + ' + str(ans) + r' = ' + str(c) + r'($y$ + ' + \
                     str(ans) + r')\\%' + '\n'
            mainC += r'$y$ + ' + str(b - a + ans) + r' = ' + str(c) + r'($y$ + ' + str(ans) + r')\\%' + '\n'
            mainC += r'On développe : %' + '\n'
            mainC += r'$y$ + ' + str(b - a + ans) + r' = ' + str(c) + r'$y$ + ' + str(c) + r'$\times$' + \
                     str(ans) + r'\\%' + '\n'
            mainC += r'$y$ + ' + str(b - a + ans) + r' = ' + str(c) + r'$y$ + ' + str(c * ans) + r'\\%' + '\n'
            mainC += r'On retire $y$ de chaque côté : '
            mainC += str(b - a + ans) + r' = ' + str(c - 1) + r'$y$ + ' + str(c * ans) + r'\\%' + '\n'
            mainC += r'On retire ' + str(c * ans) + r' de chaque côté : '
            mainC += str(b - a + ans - c * ans) + r' = ' + str(c - 1) + r'$y$' + r'\\%' + '\n'
            mainC += r'On divise par ' + str(c - 1) + r' de chaque côté : '
            mainC += r'$y = \dfrac{' + str(b - a + ans - c * ans) + r'}{' + str(c - 1) + r'}$\\%' + '\n'
            mainC += r'$y =$ ' + str(int(a)) + r'\\%' + '\n'
            mainC += nomB + r' a ' + str(a) + r' ans.\\%' + '\n'
            mainC += r'Et donc, ' + nomA + r' a ' + str(b) + r' ans.\\%' + '\n'
        else:
            mainC += r'$x$ - ' + str(-ans) + r' = ' + str(c) + r'($y$ - ' + str(-ans) + r')\\%' + '\n'
            mainC += r'On remplace $x$ par $y$ + ' + str(b - a) + r'\\%' + '\n'
            mainC += r'$y$ + ' + str(b - a) + r' - ' + str(-ans) + r' = ' + str(c) + r'($y$ - ' + \
                     str(-ans) + r')\\%' + '\n'
            mainC += r'$y$ + ' + str(b - a + ans) + r' = ' + str(c) + r'($y$ - ' + str(-ans) + r')\\%' + '\n'
            mainC += r'On développe : '
            mainC += r'$y$ + ' + str(b - a + ans) + r' = ' + str(c) + r'$y$ + ' + str(c) + r'$\times$(-' + \
                     str(-ans) + r')\\%' + '\n'
            mainC += r'$y$ + ' + str(b - a + ans) + r' = ' + str(c) + r'$y$ - ' + str(c * (-ans)) + r'\\%' + '\n'
            mainC += r'On retire $y$ de chaque côté : '
            mainC += str(b - a + ans) + r' = ' + str(c - 1) + r'$y$ - ' + str(c * (-ans)) + r'\\%' + '\n'
            mainC += r'On ajoute ' + str(c * (-ans)) + r' de chaque côté : '
            mainC += str(b - a + ans - c * ans) + r' = ' + str(c - 1) + r'$y$' + r'\\%' + '\n'
            mainC += r'On divise par ' + str(c - 1) + r' de chaque côté : '
            mainC += r'$y = \dfrac{' + str(b - a + ans - c * ans) + r'}{' + str(c - 1) + r'}$\\%' + '\n'
            mainC += r'$y =$ ' + str(int(a)) + r'\\%' + '\n'
            mainC += nomB + r' a ' + str(a) + r' ans.\\%' + '\n'
            mainC += r'Et donc, ' + nomA + r' a ' + str(b) + r' ans.\\%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def equation3(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'''\exo{Résolution d'équation}%''' + '\n'
    nbrPersonnes = randint(100, 400)
    nbrAdultes = randint(1, nbrPersonnes)
    nbrEnfants = nbrPersonnes - nbrAdultes
    prxEnfant = randint(2, 7)
    prxAdulte = randint(8, 13)
    nbr = nbrAdultes + nbrEnfants
    tot = prxEnfant * nbrEnfants + prxAdulte * nbrAdultes
    main += str(nbrPersonnes) + r" personnes vont \`{a} un spectacle.\\%" + '\n'
    main += r'Les adultes payent ' + str(prxAdulte) + r'\euro~la place et les enfants ' + str(
        prxEnfant) + r'\euro.\\%' + '\n'
    main += r'La recette de la salle est de ' + str(tot) + r'\euro.\\%' + '\n'
    main += r"Combien d'enfants étaient présents ?\\%" + '\n'
    main += '\n'
    if correction:
        mainC += r"\cor{Résolution d'équation}"
        mainC += r'''Notons $x$:"Le nombre d'enfants"\\%''' + '\n'
        mainC += r'''Notons $y$:"Le nombre d'adultes"\\%''' + '\n'
        mainC += r'On a les deux équations suivantes : \\%' + '\n'
        mainC += r'$x$ + $y$ = ' + str(nbr) + r'\\%' + '\n'
        mainC += \
            str(prxEnfant) + r'$x$ + ' + \
            str(prxAdulte) + r'$y$ = ' + \
            str(tot) + r'\\%' + '\n'
        mainC += r'On remplace $y$ par ' + str(nbr) + \
                 r''' - $x$ (Cela permet de garder seulement l'inconnue que l'on cherche)\\'''
        mainC += \
            str(prxEnfant) + r'$x$ + ' + \
            str(prxAdulte) + r'(' + \
            str(nbr) + r' - $x$) = ' + \
            str(tot) + r'\\%' + '\n'
        mainC += r'On développe : '
        mainC += \
            str(prxEnfant) + r'$x$ + ' + \
            str(prxAdulte) + r'$\times$' + str(nbr) + r' - ' + \
            str(prxAdulte) + r'$x$ = ' + \
            str(tot) + r'\\%' + '\n'
        mainC += \
            str(prxEnfant - prxAdulte) + r'$x$ + ' + \
            str(prxAdulte * nbr) + ' = ' + \
            str(tot) + r'\\%' + '\n'
        mainC += r'On retire ' + str(prxAdulte * nbr) + ' de chaque côté : '
        mainC += \
            str(prxEnfant - prxAdulte) + r'$x$' + ' = ' + \
            str(tot - prxAdulte * nbr) + r'\\%' + '\n'
        mainC += r'On divise par ' + str(prxEnfant - prxAdulte) + r' de chaque côté : '
        mainC += r'$x = \dfrac{' + str(tot - prxAdulte * nbr) + r'}{' + str(prxEnfant - prxAdulte) + r'}$\\%' + '\n'
        mainC += r'$x =$ ' + str(int(nbrEnfants)) + r'\\%' + '\n'
        mainC += r'Il y avait, ' + str(nbrEnfants) + r' enfants présents.\\%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def puissance1(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'''\exo{Puissances}%''' + '\n'
    a = randint(-30, 30)
    b = randint(-30, 30)
    main += r"Faites le calcul suivant (le résultat doit être sous forme d'une puissance de 10).\\%" + '\n'
    main += r'\begin{center}%' + '\n'
    main += r'$10^{' + str(a) + r'}\times 10^{' + str(b) + r'}=$\\%' + '\n'
    main += r'\end{center}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Puissances}%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if b < 0:
            mainC += r'$10^{' + str(a) + r'}\times 10^{' + str(b) + r'}=' + \
                     r'10^{' + str(a) + r' + (' + str(b) + r')}=' + \
                     r'10^{' + str(a + b) + r'}$%' + '\n'
        else:
            mainC += r'$10^{' + str(a) + r'}\times 10^{' + str(b) + r'}=' + \
                     r'10^{' + str(a) + r' + ' + str(b) + r'}=' + \
                     r'10^{' + str(a + b) + r'}$%' + '\n'
        mainC += r'\end{center}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def puissance2(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'''\exo{Puissances}%''' + '\n'
    a = randint(-30, 30)
    b = randint(-30, 30)
    main += r"Faites le calcul suivant (le résultat doit être sous forme d'une puissance de 10).\\%" + '\n'
    main += r'\begin{center}%' + '\n'
    main += r'$\dfrac{10^{' + str(a) + r'}}{10^{' + str(b) + r'}}=$\\%' + '\n'
    main += r'\end{center}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Puissances}%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if b < 0:
            mainC += r'$\dfrac{10^{' + str(a) + r'}}{10^{' + str(b) + r'}}=' + \
                     r'10^{' + str(a) + r' - (' + str(b) + r')}=' + \
                     r'10^{' + str(a - b) + r'}$' + '\n'
        else:
            mainC += r'$\dfrac{10^{' + str(a) + r'}}{10^{' + str(b) + r'}}=' + \
                     r'10^{' + str(a) + r' - ' + str(b) + r'}=' + \
                     r'10^{' + str(a - b) + r'}$' + '\n'
        mainC += r'\end{center}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def puissance3(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'\exo{Puissances}%' + '\n'
    a = randint(-30, 30)
    b = randint(-30, 30)
    main += r"Faites le calcul suivant (le résultat doit être sous forme d'une puissance de 10).\\%" + '\n'
    main += r'\begin{center}%' + '\n'
    main += r'$(10^{' + str(a) + r'})^{' + str(b) + r'}=$\\%' + '\n'
    main += r'\end{center}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Puissances}%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if b < 0:
            mainC += r'$\dfrac{10^{' + str(a) + r'}}{10^{' + str(b) + r'}}=' + \
                     r'10^{' + str(a) + r' \times (' + str(b) + r')}=' + \
                     r'10^{' + str(a * b) + r'}$' + '\n'
        else:
            mainC += r'$\dfrac{10^{' + str(a) + r'}}{10^{' + str(b) + r'}}=' + \
                     r'10^{' + str(a) + r' \times ' + str(b) + r'}=' + \
                     r'10^{' + str(a * b) + r'}$' + '\n'
        mainC += r'\end{center}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def cosinus1(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    a = randint(5, 30)
    b = randint(10, 80)
    br = b * 2 * pi / 360
    main += r'\exo{Cosinus}%' + '\n'
    main += r'\begin{minipage}{0.6\textwidth}%' + '\n'
    main += r'ABC est le triangle ci-contre.\\%' + '\n'
    main += r'AB = ' + str(a) + r" cm et l'angle $\alpha$ mesure " + str(b) + r'\textdegree\\%' + '\n'
    main += r'Combien mesure AC ?\\%' + '\n'
    main += r'\end{minipage}%' + '\n'
    main += r'\begin{minipage}{0.3\textwidth}%' + '\n'
    main += r'\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%' + '\n'
    main += r'\end{minipage}\\%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Cosinus}%' + '\n'
        mainC += r'cos($\alpha$)=$\dfrac{AC}{AB}$\\%' + '\n'
        mainC += r'Donc, AC = AB $\times$ cos($\alpha$)\\%' + '\n'
        mainC += r'AC $\simeq$ ' + str(round(a * cos(br), 2)) + r' cm\\%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def cosinus2(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    a = randint(5, 30)
    b = randint(10, 80)
    br = b * 2 * pi / 360
    main += r'\exo{Cosinus}%' + '\n'
    main += r'\begin{minipage}{0.6\textwidth}%' + '\n'
    main += r'ABC est le triangle ci-contre.\\%' + '\n'
    main += r'AC = ' + str(a) + r" cm et l'angle $\alpha$ mesure " + str(b) + r'\textdegree\\%' + '\n'
    main += r'Combien mesure AB ?\\%' + '\n'
    main += r'\end{minipage}%' + '\n'
    main += r'\begin{minipage}{0.3\textwidth}%' + '\n'
    main += r'\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%' + '\n'
    main += r'\end{minipage}\\%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Cosinus}%' + '\n'
        mainC += r'cos($\alpha$)=$\dfrac{AC}{AB}$\\%' + '\n'
        mainC += r'Donc, AC = $\dfrac{AB}{cos(\alpha)}$\\%' + '\n'
        mainC += r'AC $\simeq$ ' + str(round(a / cos(br), 2)) + r' cm\\%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def cosinus3(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    a = randint(5, 30)
    b = randint(10, 80)
    br = b * 2 * pi / 360
    main += r'\exo{Cosinus}%' + '\n'
    main += r'\begin{minipage}{0.6\textwidth}%' + '\n'
    main += r'ABC est le triangle ci-contre.\\%' + '\n'
    main += r'AB = ' + str(a) + r" cm et l'angle $\beta$ mesure " + str(b) + r'\textdegree\\%' + '\n'
    main += r'Combien mesure BC ?\\%' + '\n'
    main += r'\end{minipage}%' + '\n'
    main += r'\begin{minipage}{0.3\textwidth}%' + '\n'
    main += r'\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%' + '\n'
    main += r'\end{minipage}\\%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Cosinus}%' + '\n'
        mainC += r'cos($\beta$)=$\dfrac{BC}{AB}$\\%' + '\n'
        mainC += r'Donc, BC = AB $\times$ cos($\beta$)\\%' + '\n'
        mainC += r'BC $\simeq$ ' + str(round(a * cos(br), 2)) + r' cm\\%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def cosinus4(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    a = randint(5, 30)
    b = randint(10, 80)
    br = b * 2 * pi / 360
    main += r'\exo{Cosinus}%' + '\n'
    main += r'\begin{minipage}{0.6\textwidth}%' + '\n'
    main += r'ABC est le triangle ci-contre.\\%' + '\n'
    main += r'BC = ' + str(a) + r" cm et l'angle $\beta$ mesure " + str(b) + r'\textdegree\\%' + '\n'
    main += r'Combien mesure AB ?\\%' + '\n'
    main += r'\end{minipage}%' + '\n'
    main += r'\begin{minipage}{0.3\textwidth}%' + '\n'
    main += r'\includegraphics[width = \textwidth]{imagesQuatrieme/triangleRectangle.png}%' + '\n'
    main += r'\end{minipage}\\%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Cosinus}%' + '\n'
        mainC += r'cos($\beta$)=$\dfrac{BC}{AB}$\\%' + '\n'
        mainC += r'Donc, AB = $\dfrac{BC}{cos(\beta)}$\\%' + '\n'
        mainC += r'AB $\simeq$ ' + str(round(a / cos(br), 2)) + r' cm\\%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Addition de fractions#
def fraction1(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'\exo{Addition de fractions}%' + '\n'

    nums = []
    dens = []
    signs = []

    main += r'Faites le calcul suivant (le résultat doit être sous forme de fraction).\\%' + '\n'
    main += r'\begin{center}%' + '\n'
    main += r'$A='

    nbrTerms = randint(3, 4)
    for i in range(nbrTerms):
        aa = randint(1, 30)
        ab = randint(-30, -1)
        nums.append(np.random.choice([aa, ab]))
        ba = randint(1, 30)
        bb = randint(-30, -1)
        dens.append(np.random.choice([ba, bb]))
        signs.append(np.random.choice([r' + ', r' - ']))

    for i in range(nbrTerms):
        if i == 0 and (signs[i] == r' + '):
            main += r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
        else:
            main += signs[i] + r'\dfrac{' + str(nums[i]) + r'}{' + str(dens[i]) + r'}'
    main += r'$%' + '\n'
    main += r'\end{center}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Addition de fractions}%' + '\n'
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
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections






