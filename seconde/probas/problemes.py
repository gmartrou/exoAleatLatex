#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
import fonctionsSimplifiantes


def probasMaladies(fileExercices, fileCorrections):
    """Exercice de probabilité utilisant un schéma de probabilité afin de résoudre le problème."""
    
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
    pA = round(pApercent / 100, 2)
    pB = round(pBpercent / 100, 2)
    pAinterB = round(pTpercent / 100, 2)
    pAinterBBar = round(1 - pAinterB, 2)
    pAunionB = round(pA + pB - pAinterB, 2)
    pAunionBBar = round(1 - pAunionB, 2)
    pAonly = round(pA - pAinterB, 2)
    pAonlyBar = round(1 - pAonly, 2)
    pBonly = round(pB - pAinterB, 2)
    pAxorB = round(pAunionB - pAinterB, 2)
    # Fin des variables.
    
    # Enoncé de l'exercice.
    main = r'''\exo{Des maladies dangereuses}%
En \{annee}, les habitants de \{ville} subissent une épidémie. Les deux maladies décimants la ville sont
\{malA} et \{malB}.\\%

On estime que \{pApercent}\% des habitants sont atteints de la \{malA}, \{pBpercent}\%
des habitants sont atteints de la \{malB}
et \{pTpercent}\% des habitants sont atteints des deux maladies à la fois.\\%

On prend un habitant au hasard dans la ville.\\%

\begin{enumerate}[label=\alph*)]%
    \item Calculer la probabilité qu'il soit atteint seulement de \{malA}.%
    \item Calculer la probabilité qu'il ne soit pas malade.%
    \item Calculer la probabilité qu'il soit malade mais seulement atteint d'une des deux maladies%
\end{enumerate}%
'''
    # Fin de l'énoncé.
    
    # Fichier texte de la correction.
    mainC = r'''\cor{Des maladies dangereuses}%
Notons A : "L'habitant de \{ville} est atteint de \{malA}"\\%
Notons B : "L'habitant de \{ville} est atteint de \{malB}"\\%

Les données de l'énoncé nous disent que :\\%
p(A) = \{pA}\\%
p(B) = \{pB}\\%
p(A $\cap$ B) = \{pAinterB}\\%
Afin de bien se représenter le problème, on peut faire les schémas suivants :\\%
\begin{center}
\begin{minipage}{0.3\textwidth}%
\includegraphics[width = \textwidth]{images/proba13.png}%
\end{minipage}%
\begin{minipage}{0.32\textwidth}%
\includegraphics[width = \textwidth]{images/proba23.png}%
\end{minipage}%
\begin{minipage}{0.32\textwidth}%
\includegraphics[width = \textwidth]{images/proba3.png}%
\end{minipage}%
\end{center}
\begin{enumerate}[label=\alph*)]%
\item La probabilité que l'on cherche est la probabilité qu'il soit atteint de \{malA} ET pas de \{malB}.\\%
On cherche donc p($A \cap \bar{B}$).\\%
En observant les schémas on observe que p(A $\cap$ $\bar{B}$) = p(A) - p(A $\cap$ B) =
\{pA} - \{pAinterB} = \{pAonly}.\\%
\item La probabilité cherchée est p($\overline{A \cup B}$) = 1 - p($A \cup B$).\\%
Or, p($A \cup B$) = p(A) + p(B) - p($A \cap B$) = \{pA} + \{pB} - \{pAinterB} = \{pAunionB}.\\%
Donc, p($\overline{A \cup B}$) = 1 - \{pAunionB} = \{pAunionBBar}.\\%
\item La probabilité recherchée est la probabilité qu'il soit malade moins la probabilité qu'il soit atteint
des deux à la fois soit p($A \cup B$) - p($A \cap B$) =
\{pAunionB} - \{pAinterB} = \{pAxorB}.\\%
\end{enumerate}
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def probasViennoiseriesTest(fileExercices, fileCorrections):
    """Exercice sur les probabilités nécessitants un arbre. Basé sur une usine de viennoiseries."""
    
    # Définition des variables.
    listeViennoiseries = ['pains au chocolat',
                          'chocolatines',
                          'pains aux raisins',
                          'croissants',
                          'chouquettes',
                          'chaussons aux pommes',
                          'brioches au chocolat',
                          'brioches tressées',
                          'croissants aux amandes',
                          'fougasses',
                          'muffins',
                          'pains aux céréales',
                          ]
    
    vienA = np.random.choice(listeViennoiseries)
    listeViennoiseries.remove(vienA)
    vienB = np.random.choice(listeViennoiseries)
    pApercent = random.randint(61, 90)
    pBpercent = 100 - pApercent
    pDaPercent = random.randint(2, 4)
    pDbPercent = random.randint(pDaPercent + 1, 8)
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