#!/usr/bin/python
# -*- coding: utf-8 -*-

from fonctionsSimplifiantes import signT


def tableauSigneAffine(a, b):
    main = r'''\begin{center}%
\begin{tikzpicture}%
\tkzTabInit{$x$ / 1 , $f(x)$ / 1}{$-\infty$, $ \{-b/a} $, $+\infty$}%
\tkzTabLine{, \{signT(-a)}, z, \{signT(a)}, }%' + '\n'
\end{tikzpicture}%
\end{center}%
'''
    return main


# def tableauSigneSecondDegreFactorise()
