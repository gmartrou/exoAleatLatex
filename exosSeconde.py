from random import *
import numpy as np
from fonctionsSimplifiantes import *


def fonctionAffine1(fileExercices, fileCorrections):
    main = ''
    mainC = ''
    main += r'\exo{Intersection de fonctions affines}'
    a, b, c, d = 0, 0, 0, 0
    while b == d or a == c:
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        c1 = randint(1, 6)
        c2 = randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = randint(2, 6)
        d2 = randint(-6, -1)
        d = np.random.choice([d1, d2])
    if b > 0:
        signB = r' + '
        bA = b
    else:
        signB = r' - '
        bA = abs(b)
    if d > 0:
        signD = r' + '
        dA = d
    else:
        signD = r' - '
        dA = abs(d)
    main += r'Soit $f$ et $g$ les fonctions définies sur $\R$ par $f(x) = ' + \
            str(a) + r'x' + signB + str(bA) + r'$ et $g(x) = ' + \
            str(c) + r'x' + signD + str(dA) + r'$'
    main += r'\medskip%' + '\n'
    main += r'\begin{enumerate}%' + '\n'
    main += r"\item Tracer les courbes représentatives des fonctions $f$ et $g$ dans le plan muni d'un repère.%" + '\n'
    main += r"\item Calculer les coordonnées du point d'intersection des deux courbes.%" + '\n'
    main += r'\end{enumerate}%' + '\n'
    if correction:
        xmin = -10
        ymin = -10
        xmax = 10
        ymax = 10
        xA = (d - b) / (a - c)
        if xA == int(xA):
            xA = int(xA)
        elif xA != round(xA, 2):
            xA = round(xA, 2)
        yA = a * xA + b
        if yA == int(yA):
            yA = int(yA)
        elif yA != round(yA, 2):
            yA = round(yA, 2)
        mainC += r'\cor{Intersection de fonctions affines}'
        mainC += r'''\medskip
        \begin{enumerate}
        \item Les courbes représentantes des fonctions $f$ et $g$ sont sur le graphique ci-après :
        \end{enumerate}'''
        mainC = repereDebut(mainC, xmin, ymin, xmax, ymax)
        mainC += r'\addplot[color=red,domain=-10:10, samples=300]{' + str(a) + r'*x+' + str(b) + r'};\\'
        mainC += r'\addplot[color=blue,domain=-10:10, samples=300]{' + str(c) + r'*x+' + str(d) + r'};\\'
        mainC += r'\node[text=red] at (7, 9) {$f(x)$};\\'
        mainC += r'\node[text=blue] at (7, 7) {$g(x)$};\\'
        mainC += r'\node[text=black, cross=3pt] at (' + str(xA) + r', ' + str(yA) + r') {};\\'
        mainC += r'\node[text=black, right] at (' + str(xA) + r', ' + str(yA) + r') {A};\\'
        mainC = repereFin(mainC)
        mainC += r'''
        \begin{enumerate}[resume]
        \item À l'intersection des deux droites, on a $f(x)=g(x)$. Soit, $''' + str(a) + r'x' + signB + str(bA) + \
                 r' = ' + str(c) + r'x' + signD + str(dA) + r'$\\'
        if xA == round(xA):
            mainC += r'''C'est à dire $x=\dfrac{''' + str(d - b) + r'}{' + str(a - c) + r'} = ' + str(xA) + r'$\\'
        else:
            mainC += r'''C'est à dire $x=\dfrac{''' + str(d - b) + r'}{' + str(a - c) + r'} \simeq ' + str(xA) + r'$\\'
        mainC += r'''Et donc $y=f(''' + str(xA) + r''')=''' + str(yA) + r'''$ ou $y = g(''' + str(xA) + r''')=''' + str(
            yA) + r'''$\\
        Le point d'intersection est donc le point A(''' + str(xA) + r''',''' + str(yA) + r''').
        \end{enumerate}'''
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Tableau de signe simple avec une seule expression du premier degré
def tableauDeSigneUn1(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul = 1 / 3
    a, b = 0, 0
    while VAnnul != round(VAnnul, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul = -b / a
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = ' + str(
        a) + r'x' + signB + str(abs(b)) + r'$%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) \leq 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $f(x)=0$ est ' + str(VAnnul) + r'.\\%' + '\n'
        if b > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc la fonction sera positive après ' \
                     + str(VAnnul) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc la fonction sera négative après ' \
                     + str(VAnnul) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if a > 0:
            signA = ' + '
            signMA = ' - '
        else:
            signA = ' - '
            signMA = ' + '
        mainC += r'\begin{tikzpicture}%' + '\n'
        mainC += r'\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $' + str(-b / a) + r'$, $+\infty$}%' + '\n'
        mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', }%' + '\n'
        mainC += r'\end{tikzpicture}%' + '\n'
        mainC += r'\end{center}%' + '\n'
        if a > 0:
            mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open  left]{-\infty}{' + str(
                VAnnul) + r'}$%' + '\n'
        else:
            mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open right]{' + str(
                VAnnul) + r'}{+\infty}$  %' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def tableauDeSigneUn2(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul = 1 / 3
    a, b = 0, 0
    while VAnnul != round(VAnnul, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul = -b / a
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = ' + str(
        a) + r'x' + signB + str(abs(b)) + r'$%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) \geq 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $f(x)=0$ est ' + str(VAnnul) + r'.\\%' + '\n'
        if b > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc la fonction sera positive après ' \
                     + str(VAnnul) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc la fonction sera négative après ' \
                     + str(VAnnul) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if a > 0:
            signA = ' + '
            signMA = ' - '
        else:
            signA = ' - '
            signMA = ' + '
        mainC += r'\begin{tikzpicture}%' + '\n'
        mainC += r'\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $' + str(-b / a) + r'$, $+\infty$}%' + '\n'
        mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', }%' + '\n'
        mainC += r'\end{tikzpicture}%' + '\n'
        mainC += r'\end{center}%' + '\n'
        if a < 0:
            mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open  left]{-\infty}{' + str(
                VAnnul) + r'}$%' + '\n'
        else:
            mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open right]{' + str(
                VAnnul) + r'}{+\infty}$  %' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Tableau de signe simple avec une seule expression du premier degré
def tableauDeSigneUn3(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul = 1 / 3
    a, b = 0, 0
    while VAnnul != round(VAnnul, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul = -b / a
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = ' + str(
        a) + r'x' + signB + str(abs(b)) + r'$%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) < 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $f(x)=0$ est ' + str(VAnnul) + r'.\\%' + '\n'
        if b > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc la fonction sera positive après ' \
                     + str(VAnnul) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc la fonction sera négative après ' \
                     + str(VAnnul) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if a > 0:
            signA = ' + '
            signMA = ' - '
        else:
            signA = ' - '
            signMA = ' + '
        mainC += r'\begin{tikzpicture}%' + '\n'
        mainC += r'\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $' + str(-b / a) + r'$, $+\infty$}%' + '\n'
        mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', }%' + '\n'
        mainC += r'\end{tikzpicture}%' + '\n'
        mainC += r'\end{center}%' + '\n'
        if a > 0:
            mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{-\infty}{' + str(
                VAnnul) + r'}$%' + '\n'
        else:
            mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{' + str(
                VAnnul) + r'}{+\infty}$  %' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


def tableauDeSigneUn4(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul = 1 / 3
    a, b = 0, 0
    while VAnnul != round(VAnnul, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul = -b / a
    if b > 0:
        signB = ' + '
    else:
        signB = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = ' + str(
        a) + r'x' + signB + str(abs(b)) + r'$%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) > 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $f(x)=0$ est ' + str(VAnnul) + r'.\\%' + '\n'
        if b > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc la fonction sera positive après ' \
                     + str(VAnnul) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc la fonction sera négative après ' \
                     + str(VAnnul) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
        if a > 0:
            signA = ' + '
            signMA = ' - '
        else:
            signA = ' - '
            signMA = ' + '
        mainC += r'\begin{tikzpicture}%' + '\n'
        mainC += r'\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $' + str(-b / a) + r'$, $+\infty$}%' + '\n'
        mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', }%' + '\n'
        mainC += r'\end{tikzpicture}%' + '\n'
        mainC += r'\end{center}%' + '\n'
        if a < 0:
            mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{-\infty}{' + str(
                VAnnul) + r'}$%' + '\n'
        else:
            mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{' + str(
                VAnnul) + r'}{+\infty}$  %' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Tableau de signe pour une expression du second degré (produit de deux expressions du premier degré). f(x)<=0
def tableauDeSigne2(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = 0, 0
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = randint(2, 6)
        c2 = randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = randint(1, 6)
        d2 = randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
        if b > 0:
            signB = ' + '
        else:
            signB = ' - '
        if d > 0:
            signD = ' + '
        else:
            signD = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = (' + \
            str(a) + r'x' + signB + str(abs(b)) + r')(' + str(c) + r'x' + signD + str(abs(d)) + r'$)%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) \leq 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $' + str(a) + r'x' + signB + str(abs(b)) + r' = 0$ est ' + str(
            VAnnul1) + r'.\\%' + '\n'
        if a > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera positive après ' \
                     + str(VAnnul1) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera négative après ' \
                     + str(VAnnul1) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'La valeur de $x$ pour laquelle $' + str(c) + r'x' + signD + str(abs(d)) + r' = 0$ est ' + str(
            VAnnul2) + r'.\\%' + '\n'
        if c > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera positive après ' \
                     + str(VAnnul2) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera négative après ' \
                     + str(VAnnul2) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
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
        mainC += r'\begin{tikzpicture}%' + '\n'
        if VAnnul1 < VAnnul2:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul1) + r'$, $' + str(
                VAnnul2) + \
                     r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', t,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', t, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' - ':
                mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open  left]{-\infty}{' + str(
                    VAnnul1) + r'} \cup \interval[open  right]{' + str(VAnnul2) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval{' + str(
                    VAnnul1) + r'}{' + str(VAnnul2) + r'}$  %' + '\n'
        elif VAnnul2 < VAnnul1:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul2) + r'$, $' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', t, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z, ' + signC + r', t,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' - ':
                mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval[open  left]{-\infty}{' + str(
                    VAnnul2) + r'} \cup \interval[open  right]{' + str(VAnnul1) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in\interval{' + str(
                    VAnnul2) + r'}{' + str(VAnnul1) + r'}$  %' + '\n'
        else:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $''' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' - ':
                mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x\in \R$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) \leq 0$ pour $x=' + str(VAnnul1) + r'$%' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Tableau de signe pour une expression du second degré (produit de deux expressions du premier degré). f(x)>=0
def tableauDeSigne3(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = '', ''
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = randint(2, 6)
        c2 = randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = randint(1, 6)
        d2 = randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
        if b > 0:
            signB = ' + '
        else:
            signB = ' - '
        if d > 0:
            signD = ' + '
        else:
            signD = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = (' + \
            str(a) + r'x' + signB + str(abs(b)) + r')(' + str(c) + r'x' + signD + str(abs(d)) + r'$)%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) \geq 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $' + str(a) + r'x' + signB + str(abs(b)) + r' = 0$ est ' + str(
            VAnnul1) + r'.\\%' + '\n'
        if a > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera positive après ' \
                     + str(VAnnul1) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera négative après ' \
                     + str(VAnnul1) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'La valeur de $x$ pour laquelle $' + str(c) + r'x' + signD + str(abs(d)) + r' = 0$ est ' + str(
            VAnnul2) + r'.\\%' + '\n'
        if c > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera positive après ' \
                     + str(VAnnul2) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera négative après ' \
                     + str(VAnnul2) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
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
        mainC += r'\begin{tikzpicture}%' + '\n'
        if VAnnul1 < VAnnul2:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul1) + r'$, $' + str(
                VAnnul2) + \
                     r'$, $ + \infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', t,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', t, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' + ':
                mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open  left]{-\infty}{' + \
                         str(VAnnul1) + r'} \cup \interval[open  right]{' + str(VAnnul2) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval{' + \
                         str(VAnnul1) + r'}{' + str(VAnnul2) + r'}$  %' + '\n'
        elif VAnnul2 < VAnnul1:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul2) + r'$, $' + str(
                VAnnul1) + \
                     r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', t, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z, ' + signC + r', t,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' + ':
                mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval[open  left]{-\infty}{' + \
                         str(VAnnul2) + r'} \cup \interval[open  right]{' + str(VAnnul1) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in\interval{' + \
                         str(VAnnul2) + r'}{' + str(VAnnul1) + r'}$  %' + '\n'
        else:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $''' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' + ':
                mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x\in \R$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) \geq 0$ pour $x=' + str(VAnnul1) + r'$%' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Tableau de signe pour une expression du second degré (produit de deux expressions du premier degré). f(x)<0
def tableauDeSigne4(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = '', ''
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = randint(2, 6)
        c2 = randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = randint(1, 6)
        d2 = randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
        if b > 0:
            signB = ' + '
        else:
            signB = ' - '
        if d > 0:
            signD = ' + '
        else:
            signD = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = (' + str(
        a) + r'x' + signB + str(abs(b)) + r')(' + str(c) + r'x' + signD + str(abs(d)) + r'$)%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) < 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $' + str(a) + r'x' + signB + str(abs(b)) + r' = 0$ est ' + str(
            VAnnul1) + r'.\\%' + '\n'
        if a > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera positive après ' \
                     + str(VAnnul1) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera négative après ' \
                     + str(VAnnul1) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'La valeur de $x$ pour laquelle $' + str(c) + r'x' + signD + str(abs(d)) + r' = 0$ est ' + str(
            VAnnul2) + r'.\\%' + '\n'
        if c > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera positive après ' \
                     + str(VAnnul2) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera négative après ' \
                     + str(VAnnul2) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
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
        mainC += r'\begin{tikzpicture}%' + '\n'
        if VAnnul1 < VAnnul2:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul1) + r'$, $' + str(
                VAnnul2) + \
                     r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', t,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', t, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' - ':
                mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{-\infty}{' + str(
                    VAnnul1) + r'} \cup \interval[open]{' + str(VAnnul2) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in\interval{' + str(VAnnul1) + r'}{' + str(
                    VAnnul2) + r'}$  %' + '\n'
        elif VAnnul2 < VAnnul1:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul2) + r'$, $' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', t, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z, ' + signC + r', t,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' - ':
                mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in\interval[open]{-\infty}{' + str(
                    VAnnul2) + r'} \cup \interval[open]{' + str(VAnnul1) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in\interval{' + str(VAnnul2) + r'}{' + str(
                    VAnnul1) + r'}$  %' + '\n'
        else:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $''' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' - ':
                mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in \R \backslash \{' + str(
                    VAnnul1) + r'\}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) < 0$ pour $x\in \emptyset $%' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Tableau de signe pour une expression du second degré (produit de deux expressions du premier degré). f(x)>0
def tableauDeSigne5(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r'\exo{Tableau de Signe}%' + '\n'
    VAnnul1 = 1 / 3
    VAnnul2 = 1 / 3
    a, b, c, d = 0, 0, 0, 0
    signB, signD = '', ''
    while VAnnul1 != round(VAnnul1, 3) or VAnnul2 != round(VAnnul2, 3):
        a1 = randint(2, 6)
        a2 = randint(-6, -2)
        a = np.random.choice([a1, a2])
        b1 = randint(1, 6)
        b2 = randint(-6, -1)
        b = np.random.choice([b1, b2])
        VAnnul1 = -b / a
        c1 = randint(2, 6)
        c2 = randint(-6, -2)
        c = np.random.choice([c1, c2])
        d1 = randint(1, 6)
        d2 = randint(-6, -1)
        d = np.random.choice([d1, d2])
        VAnnul2 = -d / c
        if b > 0:
            signB = ' + '
        else:
            signB = ' - '
        if d > 0:
            signD = ' + '
        else:
            signD = ' - '
    main += r'\begin{enumerate}%' + '\n'
    main += r'\item Tracez le tableau de variation de la fonction $f$ définie par : $f(x) = (' + str(
        a) + r'x' + signB + str(abs(b)) + r')(' + str(c) + r'x' + signD + str(abs(d)) + r'$)%' + '\n'
    main += r'\item En déduire les valeurs pour lesquelles $f(x) > 0$%' + '\n'
    main += r'\end{enumerate}%' + '\n'
    main += '\n'
    if correction:
        mainC += r'\cor{Tableau de Signe}%' + '\n'
        mainC += r'\begin{enumerate}%' + '\n'
        mainC += r'\item La valeur de $x$ pour laquelle $' + str(a) + r'x' + signB + str(abs(b)) + r' = 0$ est ' + str(
            VAnnul1) + r'.\\%' + '\n'
        if a > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera positive après ' \
                     + str(VAnnul1) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(a) + r'$x$' + signB + str(
                abs(b)) + r' sera négative après ' \
                     + str(VAnnul1) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'La valeur de $x$ pour laquelle $' + str(c) + r'x' + signD + str(abs(d)) + r' = 0$ est ' + str(
            VAnnul2) + r'.\\%' + '\n'
        if c > 0:
            mainC += r'Le coefficient devant $x$ est positif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera positive après ' \
                     + str(VAnnul2) + r' et négative avant.\\%' + '\n' + '\n'
        else:
            mainC += r'Le coefficient devant $x$ est négatif, donc ' + str(c) + r'$x$' + signB + str(
                abs(d)) + r' sera négative après ' \
                     + str(VAnnul2) + r' et positive avant.\\%' + '\n' + '\n'
        mainC += r'On a donc le tableau de signes suivant :\\%' + '\n'
        mainC += r'\begin{center}%' + '\n'
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
        mainC += r'\begin{tikzpicture}%' + '\n'
        if VAnnul1 < VAnnul2:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul1) + r'$, $' + str(
                VAnnul2) + \
                     r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z, ' + signA + r', t,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', t, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' + ':
                mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{-\infty}{' + str(
                    VAnnul1) + r'} \cup \interval[open]{' + str(VAnnul2) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in\interval{' + str(VAnnul1) + r'}{' + str(
                    VAnnul2) + r'}$  %' + '\n'
        elif VAnnul2 < VAnnul1:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $' + str(VAnnul2) + r'$, $' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', t, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z, ' + signC + r', t,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z, ' + signFM + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' + ':
                mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in\interval[open]{-\infty}{' + str(
                    VAnnul2) + r'} \cup \interval[open]{' + str(VAnnul1) + r'}{+\infty}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in\interval{' + str(VAnnul2) + r'}{' + str(
                    VAnnul1) + r'}$  %' + '\n'
        else:
            mainC += r'\tkzTabInit{$x$ / 1 , ' + str(a) + r'$x$' + signB + str(abs(b)) + r' /1, ' + str(c) + \
                     r'$x$' + signD + str(abs(d)) + r' /1, $f(x)$ / 1}{$-\infty$, $''' + str(
                VAnnul1) + r'$, $+\infty$}%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMA + r', z,' + signA + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signMC + r', z,' + signC + r' }%' + '\n'
            mainC += r'\tkzTabLine{, ' + signFD + r', z,' + signFD + r' }%' + '\n'
            mainC += r'\end{tikzpicture}%' + '\n'
            mainC += r'\end{center}%' + '\n'
            if signFD == ' + ':
                mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in \R \backslash \{' + str(
                    VAnnul1) + r'\}$  %' + '\n'
            else:
                mainC += r'\item On peut en déduire que $f(x) > 0$ pour $x\in \emptyset $%' + '\n'
        mainC += r'\end{enumerate}%' + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Exo vecteur (prouver qu'il s'agit d'un parallèlogramme)
def vecteurs1(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r"\exo{Vecteurs et parallèlogrammes.}%" + '\n'
    xA = randint(-5, -1)
    yA = randint(-5, -1)
    xB = randint(-5, -1)
    yB = randint(1, 5)
    xC = randint(1, 5)
    yC = randint(1, 5)
    xD = xA + xC - xB
    yD = yA + yC - yB
    main += r'''Dans le plan muni d'un repère $\left( {{\mathrm{O}};\vec{\imath},
    \vec{\jmath}} \right)$, on considère les points $A\left(''' + \
            str(xA) + r";" + str(yA) + r"\right)$, $B\left(" + \
            str(xB) + r";" + str(yB) + r"\right)$, $C\left(" + \
            str(xC) + r";" + str(yC) + r"\right)$ et $D\left(" + \
            str(xD) + r";" + str(yD) + r"\right)$.\\%" + '\n'
    main += r'Le quadrilatère ABCD est-il un parallèlogramme ?%' + '\n'
    main += '\n'
    if correction:
        mainC += r"\cor{Vecteurs et parallèlogrammes.}%" + '\n'
        mainC = repereDebut(mainC, -6, -8, 9, 6)
        mainC += r"\path[draw, red] (" + str(xA) + r"," + str(yA) + r")  coordinate [label= left:$A$] (A) -- (" + \
                 str(xB) + r"," + str(yB) + r")  coordinate [label=above:$B$] (B)" + \
                 r"-- ( " + str(xC) + r"," + str(yC) + r")  coordinate [label=right:$C$] (C)" + \
                 r"-- ( " + str(xD) + r"," + str(yD) + r")  coordinate [label=right:$D$] (D)" + \
                 r"-- cycle;%" + '\n'
        mainC = repereFin(mainC)
        mainC += r"$\coordv{BA}{x_A - x_B}{y_A - y_B}$. "
        mainC += r"Donc, $\coordv{BA}{" + str(xA) + r" - (" + str(xB) + r")}{" + str(yA) + r" - " + str(yB) + r"}$. "
        mainC += r"Ainsi, $\coordv{BA}{" + str(xA - xB) + r"}{" + str(yA - yB) + r"}$\\%"
        mainC += '\n'
        mainC += r"$\coordv{CD}{x_D - x_C}{y_D - y_C}$. "
        mainC += r"Donc, $\coordv{CD}{" + str(xD) + r" - " + str(xC) + r"}{" + str(yD) + r" - " + str(yC) + r"}$. "
        mainC += r"Ainsi, $\coordv{CD}{" + str(xD - xC) + r"}{" + str(yD - yC) + r"}$\\%"
        mainC += '\n'
        mainC += r"$\vv{BA}=\vv{CD}$, donc, ABCD est un parallèlogramme.%" + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Exo vecteur (prouver qu'il ne s'agit pas d'un parallèlogramme)
def vecteurs2(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r"\exo{Vecteurs et parallèlogrammes.}%" + '\n'
    xA = randint(-5, -1)
    yA = randint(-5, -1)
    xB = randint(-5, -1)
    yB = randint(1, 5)
    xC = randint(1, 5)
    yC = randint(1, 5)
    xD = xA + xC - xB
    yD = yA + yC - yB
    perturbation = [-2, -1, 1, 2]
    xD += np.random.choice(perturbation)
    yD += np.random.choice(perturbation)
    main += r'''Dans le plan muni d'un repère $\left( {{\mathrm{O}};
    \vec{\imath},\vec{\jmath}} \right)$, on considère les points $A\left(''' + \
            str(xA) + r";" + str(yA) + r"\right)$, $B\left(" + \
            str(xB) + r";" + str(yB) + r"\right)$, $C\left(" + \
            str(xC) + r";" + str(yC) + r"\right)$ et $D\left(" + \
            str(xD) + r";" + str(yD) + r"\right)$.\\%" + '\n'
    main += r'Le quadrilatère ABCD est-il un parallèlogramme ?%' + '\n'
    main += '\n'
    if correction:
        mainC += r"\cor{Vecteurs et parallèlogrammes.}%" + '\n'
        mainC = repereDebut(mainC, -6, -8, 9, 6)
        mainC += r"\path[draw, red] (" + str(xA) + r"," + str(yA) + r")  coordinate [label= left:$A$] (A) -- (" + \
                 str(xB) + r"," + str(yB) + r")  coordinate [label=above:$B$] (B)" + \
                 r"-- ( " + str(xC) + r"," + str(yC) + r")  coordinate [label=right:$C$] (C)" + \
                 r"-- ( " + str(xD) + r"," + str(yD) + r")  coordinate [label=right:$D$] (D)" + \
                 r"-- cycle;%" + '\n'
        mainC = repereFin(mainC)
        mainC += r"$\coordv{BA}{x_A - x_B}{y_A - y_B}$. "
        mainC += r"Donc, $\coordv{BA}{" + str(xA) + r" - (" + str(xB) + r")}{" + str(yA) + r" - " + str(yB) + r"}$. "
        mainC += r"Ainsi, $\coordv{BA}{" + str(xA - xB) + r"}{" + str(yA - yB) + r"}$\\%"
        mainC += '\n'
        mainC += r"$\coordv{CD}{x_D - x_C}{y_D - y_C}$. "
        mainC += r"Donc, $\coordv{CD}{" + str(xD) + r" - " + str(xC) + r"}{" + str(yD) + r" - " + str(yC) + r"}$. "
        mainC += r"Ainsi, $\coordv{CD}{" + str(xD - xC) + r"}{" + str(yD - yC) + r"}$\\%"
        mainC += '\n'
        mainC += r"$\vv{BA} \neq \vv{CD}$, donc, ABCD n'est pas un parallèlogramme.%" + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Exo vecteur (Calculer les coordonnées d'un point à partir d'une expression vectorielle)
def vecteurs3(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r"\exo{Vecteurs et coordonnées.}%" + '\n'
    xA = randint(-5, -1)
    yA = randint(-5, -1)
    xB = randint(-5, -1)
    yB = randint(1, 5)
    xC = randint(1, 5)
    yC = randint(1, 5)
    coeff1, coeff2 = 0, 0
    signC2 = ''
    while coeff1 in [-1, 0, 1] or coeff2 in [-1, 0, 1]:
        coeff1 = randint(-5, 5)
        coeff2 = randint(-5, 5)
        if coeff2 >= 0:
            signC2 = ' + '
        else:
            signC2 = ' - '
    main += r'''Dans le plan muni d'un repère $\left( {{\mathrm{O}};\vec{\imath},
    \vec{\jmath}} \right)$, on considère les points $A\left(''' + \
            str(xA) + r";" + str(yA) + r"\right)$, $B\left(" + \
            str(xB) + r";" + str(yB) + r"\right)$ et $C\left(" + \
            str(xC) + r";" + str(yC) + r"\right)$.\\%" + '\n'
    main += r'Calculez les coordonnées du point D tel que :%' + '\n'
    main += r'\begin{center}%' + '\n'
    main += r'$\vv{BD}=' + str(coeff1) + r'\vv{AB}' + signC2 + str(abs(coeff2)) + r'\vv{CA}$%' + '\n'
    main += r'\end{center}%' + '\n'
    main += '\n'
    if correction:
        mainC += r"\cor{Vecteurs et coordonnées.}%" + '\n'
        mainC += r"\begin{enumerate}%" + '\n'
        mainC += r"\item On calcule les coordonnées des vecteurs $\vv{AB}$ et $\vv{CA}$\\%" + '\n'
        mainC += r"$\coordv{AB}{x_B - x_A}{y_B - y_A}$. "
        mainC += r"Donc, $\coordv{AB}{" + str(xB) + r" - (" + str(xA) + r")}{" + str(yB) + r" - " + str(yA) + r"}$. "
        mainC += r"Ainsi, $\coordv{AB}{" + str(xB - xA) + r"}{" + str(yB - yA) + r"}$\\%"
        mainC += '\n' + '\n'
        mainC += r"$\coordv{CA}{x_A - x_C}{y_A - y_C}$. "
        mainC += r"Donc, $\coordv{CA}{" + str(xA) + r" - " + str(xC) + r"}{" + str(yA) + r" - " + str(yC) + r"}$. "
        mainC += r"Ainsi, $\coordv{CA}{" + str(xA - xC) + r"}{" + str(yA - yC) + r"}$\\%"
        mainC += '\n' + '\n'
        mainC += r"\item On calcule maintenant, grâce à ces vecteurs, les coordonnées du vecteurs $\vv{BD}$\\%" + '\n'
        mainC += r'$\vv{BD}=' + str(coeff1) + r'\vv{AB}' + signC2 + str(abs(coeff2)) + r'\vv{CA}$. '
        if xB > xA:
            mainC += r"Donc, $\coordv{BD}{" + str(coeff1) + r"\times" + str(xB - xA) + \
                     signC2 + str(abs(coeff2)) + r"\times(" + str(xA - xC) + r")}{" + str(coeff1) + r"\times" + str(
                yB - yA) + \
                     signC2 + str(abs(coeff2)) + r"\times(" + str(yA - yC) + r")}$. "
        else:
            mainC += r"Donc, $\coordv{BD}{" + str(coeff1) + r"\times(" + str(xB - xA) + \
                     ")" + signC2 + str(abs(coeff2)) + r"\times(" + str(xA - xC) + r")}{" + str(coeff1) + r"\times" + \
                     str(yB - yA) + signC2 + str(abs(coeff2)) + r"\times(" + str(yA - yC) + r")}$. "
        mainC += r"Soit, $\coordv{BD}{" + str(coeff1 * (xB - xA) + coeff2 * (xA - xC)) + \
                 r"}{" + str(coeff1 * (yB - yA) + coeff2 * (yA - yC)) + r"}$.\\%" + '\n' + '\n'
        mainC += r"\item À partir des coordonnées de B et $\vv{BD}$, on calcule ceux du point D.\\%" + '\n'
        mainC += r"On a $\coord{B}{" + str(xB) + r"}{" + str(yB) + r"}$ et $\coordv{BD}{" + \
                 str(coeff1 * (xB - xA) + coeff2 * (xA - xC)) + \
                 r"}{" + str(coeff1 * (yB - yA) + coeff2 * (yA - yC)) + r"}$. "
        bdx = coeff1 * (xB - xA) + coeff2 * (xA - xC)
        bdy = coeff1 * (yB - yA) + coeff2 * (yA - yC)
        if bdx >= 0:
            signbdx = ' + '
        else:
            signbdx = ' - '
        if bdy >= 0:
            signbdy = ' + '
        else:
            signbdy = ' - '
        mainC += r"Donc $\coord{D}{" + str(xB) + signbdx + str(abs(bdx)) + r"}{" + str(yB) + signbdy + str(
            abs(bdy)) + r"}$\\%" + '\n'
        mainC += r"Et, finalement, $\coord{D}{" + str(xB + bdx) + r"}{" + str(yB + bdy) + r"}$%" + '\n'
        mainC += r"\end{enumerate}%" + '\n'
        mainC += '\n'
        fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Exo vecteur (vérifier que 2 droites sont, ou non, colinéaires).
def vecteurs4(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r"\exo{Vecteurs et colinéarité.}%" + '\n'
    xA, yA, xB, yB, xC, yC, xAB, yAB = 0, 0, 0, 0, 100, 100, 0, 0
    while xC > 8 or yC > 8:
        xA = randint(-5, -1)
        yA = randint(-5, -1)
        xB = randint(xA + 1, 1)
        yB = randint(yA + 1, 1)
        xAB = xB - xA
        yAB = yB - yA
        coeff = randint(2, 3)
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
    
    main += r'''Dans le plan muni d'un repère $\left( {{\mathrm{O}};
    \vec{\imath},\vec{\jmath}} \right)$, on considère les points $A\left(''' + \
            str(xA) + r";" + str(yA) + r"\right)$, $B\left(" + \
            str(xB) + r";" + str(yB) + r"\right)$ et $C\left(" + \
            str(xC) + r";" + str(yC) + r"\right)$.\\%" + '\n'
    main += r'Les points A, B et C sont-ils alignés ?%' + '\n'
    main += '\n'
    if correction:
        mainC += r"\cor{Vecteurs et colinéarité.}%" + '\n'
        mainC = repereDebut(mainC, xA-1, yA-1, max(xC+1, 1), max(yC+1, 1))
        mainC += r'\node[text=red, cross=3pt, label=right:\textcolor{red}{A}] at (' +\
                 str(xA) + r', ' + str(yA) + r') {};\\'
        mainC += r'\node[text=red, cross=3pt, label=right:\textcolor{red}{B}] at (' +\
                 str(xB) + r', ' + str(yB) + r') {};\\'
        mainC += r'\node[text=red, cross=3pt, label=right:\textcolor{red}{C}] at (' +\
                 str(xC) + r', ' + str(yC) + r') {};\\'
        mainC = repereFin(mainC)
        mainC += r"\begin{enumerate}%" + '\n'
        mainC += r"\item On calcule les coordonnées des vecteurs $\vv{AB}$ et $\vv{CB}$\\%" + '\n'
        mainC += r"$\coordv{AB}{x_B - x_A}{y_B - y_A}$. "
        mainC += r"Donc, $\coordv{AB}{" + str(xB) + r" - " + xAtext + r"}{" + str(yB) + r" - " + yAtext + r"}$. "
        mainC += r"Ainsi, $\coordv{AB}{" + str(xB - xA) + r"}{" + str(yB - yA) + r"}$\\%"
        mainC += '\n' + '\n'
        mainC += r"$\coordv{CB}{x_B - x_C}{y_B - y_C}$. "
        mainC += r"Donc, $\coordv{CB}{" + str(xB) + r" - " + xCtext + r"}{" + str(yB) + r" - " + yCtext + r"}$. "
        mainC += r"Ainsi, $\coordv{CB}{" + str(xB - xC) + r"}{" + str(yB - yC) + r"}$\\%"
        mainC += '\n' + '\n'
        mainC += r"\item On calcule maintenant le déterminant de ces vecteurs.\\%" + '\n'
        if yCB < 0:
            yCBtext = "("+str(yCB)+")"
        else:
            yCBtext = str(yCB)
        if xCB < 0:
            xCBtext = "("+str(xCB)+")"
        else:
            xCBtext = str(xCB)
        if yAB < 0:
            yABtext = "("+str(yAB)+")"
        else:
            yABtext = str(yAB)
        mainC += r"det($\vv{AB}$, $\vv{CB}$)=$x_{AB} \times y_{CB} - y_{AB} \times x_{CB}$=" \
                 + str(xAB) + r"$\times$" + yCBtext + r" - " + yABtext + r"$\times$" + xCBtext + r" = " +\
                 str(xAB * yCB - yAB * xCB) + r"\\%" + '\n'
        mainC += r"Le déterminant de ces deux vecteurs étant nul, ils sont colinéaires.%" + '\n'
        mainC += r"\end{enumerate}%" + '\n'
        mainC += '\n'
        fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections

def test(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r"\exo{Développement}%" + '\n'
    a = 4
    b = 5
    main += fr'La somme de {a} et {b} est {a+b}'
    if correction:
        mainC += r"\cor{Développement}%" + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections


# Exercice (base)
def exercice(fileExercices, fileCorrections, correction=False, separes=False):
    main = ''
    mainC = ''
    main += r"\exo{Nom de l'exercice}%" + '\n'
    if correction:
        mainC += r"\cor{Nom de l'exercice}%" + '\n'
        mainC += '\n'
    fileExercices += main
    if separes:
        fileCorrections += mainC
    else:
        fileExercices += mainC
    return fileExercices, fileCorrections
