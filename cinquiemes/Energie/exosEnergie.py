import random
import numpy as np
from math import *
import fonctionsSupplementaires
import fonctionsSimplifiantes

def centraleElectrique(fileExercices, fileCorrections):
    """Exo sur la construction d'une chaîne d'énergie d'une centrale électrique classique."""
    energies = ["pétrole", "gaz naturel", "charbon"]
    energie = random.choice(energies)
    energies.remove(energie)

    main = r'''\titledquestion{Une centrale classique : }
Le schéma ci-dessous représente le fonctionnement d'une centrale électrique classique. Son combustible est le 
\textbf{\{energie}}. 

\begin{center}
\includegraphics[width = 0.4\textwidth]{cinquiemes/Energie/centraleThermique.png}
\end{center}

\tabComp{D4}
\begin{parts}
\part Construis une chaîne d'énergie en y plaçant les 4 formes d'énergie et les 3 convertisseurs appropriés 
correspondants au fonctionnement de la centrale électrique classique fonctionnant au \{energie}.
\begin{solutionorbox}[5cm]
Cela signifie que le \{energie} peut être trouvé tel quel dans la nature.
\end{solutionorbox}

\part Le \{energie} est une source d'énergie primaire. Qu'est-ce que cela signifie ?
\begin{solutionordottedlines}[2cm]
Cela signifie que le \{energie} peut être trouvé tel quel dans la nature.
\end{solutionordottedlines}

\part Citez deux sources d'énergie primaire renouvelables.
\begin{solutionordottedlines}[2cm]
Soleil et vent.
\end{solutionordottedlines}

\part Citez deux sources d'énergie primaire non renouvelables (autre que le \{energie}).
\begin{solutionordottedlines}[2cm]
Le \{energies[0]} et le \{energies[1]} sont des sources d'énergie primaire renouvelables.
\end{solutionordottedlines}
\end{parts}
'''
    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def circuitSerieDerivation(fileExercices, fileCorrections):
    """Exo sur la construction d'un circuit en série puis en dérivation avec les mêmes composants."""
    composants = [("une DEL (à placer en sens passant)", "la DEL"), ("une lampe", "la lampe"),
                  ("un moteur", "le moteur")]
    composants1 = random.choice(composants)
    composant1 = composants1[0]
    comp1 = composants1[1]
    composants.remove(composants1)
    composants2 = random.choice(composants)
    composant2 = composants2[0]
    comp2 = composants2[1]
    composants.remove(composants2)
    composants3 = random.choice(composants)
    composant3 = composants3[0]
    comp3 = composants3[1]

    main = r'''\titledquestion{Circuit série : }
Vous disposez d'un nombre illimité de fils de connexion, d'une pile, d'\{composant1} et d'\{composant2} :\\

\tabComp{D4}

\begin{parts}
\part Faites un schéma (en utilisant une règle et un crayon à papier) d'un circuit en série comportant tous 
les dipôles à votre disposition.
\begin{solutionorbox}[5cm]
\end{solutionorbox}

\part Que se passe-t-il pour \{comp2} si \{comp1} cesse de fonctionner ?
\begin{solutionordottedlines}[2cm]
Le circuit étant un circuit série, les autres dipôles cessent de fonctionner. 
\end{solutionordottedlines}

\part Que se passerait-il pour \{comp1} et \{comp2} si on permutait les bornes du générateur ?
\begin{solutionordottedlines}[4cm]
\end{solutionordottedlines}
\end{parts}

\titledquestion{Circuit parallèle : }
Vous disposez d'un nombre illimité de fils de connexion, d'une pile, d'\{composant1}, d'\{composant2} et 
d'\{composant3}.

\tabComp{D4}

\begin{parts}
\part Faites un schéma (en utilisant une règle et un crayon à papier) d'un circuit en dérivation comportant tous 
les dipôles à votre disposition dans deux boucles. Les indications suivantes doivent être respectées :
\begin{itemize}
\item On veut avoir \{comp1} et \{comp2} branchés en série.
\item On veut avoir \{comp3} et \{comp1} branchés en dérivation.
\item L'interrupteur doit contrôler seulement \{comp3}.
\end{itemize}
\begin{solutionorbox}[5cm]
\end{solutionorbox}

\part Que se passe-t-il pour \{comp2} et \{comp3} si \{comp1} cesse de fonctionner ?
\begin{solutionordottedlines}[2cm]
On a \{comp1} et \{comp2} branchés en série donc \{comp2} cesse de fonctionner. On a
 \{comp3} et \{comp1} branchés en dérivation donc \{comp3} ccontinue de fonctionner.
\end{solutionordottedlines}

\part Que se passerait-il pour \{comp1}, \{comp3} et \{comp2} si on permutait les bornes du générateur ?
\begin{solutionordottedlines}[4cm]
\end{solutionordottedlines}

\end{parts}
\medskip
\medskip
\medskip

\tabComp{D1}
'''
    mainC = '''
'''

    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def conducteurIsolant(fileExercices, fileCorrections):
    """Exo sur """
    materiaux = ["règle en fer", "cannette en aluminium", "paille en plastique", "table en bois",
                 "règle en plastique", "boîte en carton", "règle en aluminium"]
    materiau = random.choice(materiaux)

    main = r'''\titledquestion{À quoi peut bien servir ce circuit ?}
Le schéma ci-dessous représente un circuit créé par un élève pour tester les matériaux qui l'entourent.

\begin{center}
\includegraphics[width = 0.8\textwidth]{cinquiemes/Energie/testConductivite.png}
\end{center}

\tabComp{D4}
\begin{parts}
\part Qu'est-ce que cet élève veut tester avec son circuit ?
\begin{solutionordottedlines}[2cm]
Il veut tester si les matériaux sont conducteurs ou isolant.
\end{solutionordottedlines}

\part Quel dipôle, qu'il est préférable de placer dans tous les circuits, n'a pas été placé dans ce circuit ?
\begin{solutionordottedlines}[2cm]
Il manque l'interrupteur dans ce circuit.
\end{solutionordottedlines}

\part À quoi servirait ce dipôle ?
\begin{solutionordottedlines}[2cm]
Il sert à éviter les court-circuit, c'est une mesure de sécurité.
\end{solutionordottedlines}

\part Que se passerait-il si on plaçait, pour la tester, une \{materiau} ?
\begin{solutionordottedlines}[2cm]
\end{solutionordottedlines}

\part Qu'est ce que cela nous apprend sur la \{materiau} ?
\begin{solutionordottedlines}[2cm]
\end{solutionordottedlines}
\end{parts}
'''
    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())