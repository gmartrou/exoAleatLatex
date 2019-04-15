#!/usr/bin/python
# -*- coding: utf-8 -*-

from fonctionsSimplifiantes import signT
import fonctionsSimplifiantes


def tableauSigneAffine(a, b):
    main = r'''\begin{center}%
\begin{tikzpicture}%
\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $ \{-b/a} $, $+\infty$}%
\tkzTabLine{, \{signT(-a)}, z, \{signT(a)}, }%' + '\n'
\end{tikzpicture}%
\end{center}%
'''
    return main


a = 1
coeffs = [(1, 1), (-2, 3), (1, -1)]


def tableauSigne(a,coeffs):
    prec = 0.01
    zeros = set()
    aTotal = a
    for l in coeffs:
        aTotal *= l[0]
    for l in coeffs:
        if l[0] == 0:
            print("IL DOIT S'AGIT D'UN PRODUIT DE FONCTIONS AFFINES !!!")
        else:
            zeros.add(-l[1]/l[0])
    zeros = sorted(zeros)
    main = r'''\begin{center}%
\begin{tikzpicture}%
\tkzTabInit[espcl = \textwidth/''' + str(35*(len(zeros) + 1)) + r''']{$x$ / 1 ,'''
    for l in coeffs:
        if l[0] == 1:
            main += r'$x' + str(signT(l[1])) + str(abs(l[1])) + r'$ / 1, '
        elif l[0] == -1:
            main += r'$-x' + str(signT(l[1])) + str(abs(l[1])) + r'$ / 1, '
        else:
            main += r'$' + str(l[0]) + r'x' + str(signT(l[1])) + str(abs(l[1])) + r'$ / 1, '
    main += r''' $f(x)$ / 1}{$-\infty$, '''
    for z in zeros:
        main += r'$' + str(round(z, 2)) + r'$, '
    main += r'$+\infty$}%' + '\n'
    signF = [' + '] * (len(coeffs) + 5)
    for l in coeffs:
        i = 0
        main += r'\tkzTabLine{, '
        for z in zeros:
            sign = signT(l[0]*(z - prec) + l[1])
            main += str(sign) + r', '
            if str(sign) == signF[i]:
                signF[i] = ' + '
            else:
                signF[i] = ' - '
            i += 1
            if -l[1]/l[0] == z:
                main += r'z, '
            else:
                main += r't, '
        sign = signT(l[0]*(zeros[len(zeros) - 1] + prec) + l[1])
        main += str(sign) + r', '
        if str(sign) == signF[i]:
            signF[i] = ' + '
        else:
            signF[i] = ' - '
        main += r' }%' + '\n'
    main += r'\tkzTabLine{, '
    for j in range(len(zeros) + 1):
        if j != (len(zeros)):
            main += signF[j] + r', z, '
        else:
            main += signF[j] + r', '
    main += r' }%' + '\n'
    main += r'''\end{tikzpicture}%
\end{center}%
'''
    # return main
    return main
