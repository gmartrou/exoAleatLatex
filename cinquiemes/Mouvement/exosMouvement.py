import random
import numpy as np
from math import *
import fonctionsSupplementaires
import fonctionsSimplifiantes

def positionPlanetes(fileExercices, fileCorrections):
    """Exo sur l'ordre des planètes."""
    planetes = [("Mercure", 1), ("Venus", 2), ("Terre", 3), ("Mars", 4), ("Jupiter", 5), ("Saturne", 6), ("Uranus", 7), ("Neptune", 8)]
    planete1 = random.choice(planetes)
    planetes.remove(planete1)
    planete2 = random.choice(planetes)
    planetes.remove(planete2)
    planete3 = random.choice(planetes)

    planetesOrd = [planete1, planete2, planete3]
    planetesOrd.sort(key=lambda planet: planet[1])

    main = r'''\titledquestion{L'ordre des planètes : }
Rangez, du plus proche au plus éloigné du Soleil, ces différentes planètes :\\
\{planete1[0]}, \{planete2[0]} et \{planete3[0]}.
\tabComp{D4}
\begin{solutionordottedlines}[2cm]
En partant du Soleil, la planète \{planete1[0]} est la \{planete1[1]}$^{\text{ième}}$ planète, la planète \{planete2[0]} la \{planete2[1]}$^{\text{ième}}$ et la planète \{planete3[0]} 
la \{planete3[1]}$^{\text{ième}}$. Nous avons donc l'ordre suivant : \{planetesOrd[0][0]}, \{planetesOrd[1][0]} puis \{planetesOrd[2][0]}. 
\end{solutionordottedlines}
'''
    mainC = '''
'''

    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())

def vitessePlanete(fileExercices, fileCorrections):

    planete = random.choice(["Arcas", "Orbitar", "Intercrus", "Fafnir", "Helvetios", "Aldébaran", "Cancri", "Chamelopardis", "Fomalhaut", "Gliese", "Smertrios", "Ogme"])
    rayon = random.randint(100, 1500)
    periodeAn = random.randint(2, 60)
    periodeJour = random.randint(35, 249)
    duree = periodeAn*365.25 + periodeJour
    distance = 2*pi*rayon
    distance = round(distance, 5)
    vitesse1 = round(distance/duree, 5)
    vitesse2 = round(vitesse1*1000000/24, 5)

    main = r'''\titledquestion{Vitesse d'une planète : }
La planète \{planete} se trouve à une distance moyenne de son étoile de \{rayon} millions de km. Sa période de révolution est de \{periodeAn} ans et \{periodeJour} jours.

\begin{parts}
\part Rappelez la définition d'une révolution.\\
\begin{solutionordottedlines}[2cm]
Mouvement orbital périodique d'un corps céleste, en particulier d'une planète ou d'un satellite, autour d'un autre d'une plus grande masse. Dans notre cas, d'une planète autour de son soleil.
\end{solutionordottedlines}

\part Quelle distance parcourt \{planete} au cours d'une révolution ?\\
\begin{solutionordottedlines}[5cm]
Les planètes ont des orbites quasi circulaire. La distance parcourue correspond donc au périmètre du cercle. Ce cercle a pour rayon la distance séparant la planète à son soleil.
On a donc $\text{rayon} = \{rayon} \text{ millions de km}$. Et la distance parcourue est donc de :\\
$\text{Distance} = 2 \times \pi \times \text{rayon} = 2 \times \pi \times \{rayon} \simeq \{distance} \text{ millions de km}$.
\end{solutionordottedlines}

\part Quelle est la période, en jour de la révolution de \{planete} ?\\
\begin{solutionordottedlines}[5cm]
On nous dit que sa période de révolution est de \{periodeAn} ans et \{periodeJour} jours. On a donc une durée de :\\
$\text{Durée} = \{periodeAn} \text{ ans} + \{periodeJour} \text{ jours} = \{periodeAn} \times \textcolor{red}{365,25 \text{ jours}} + \{periodeJour} \text{ jours} = \{duree} \text{ jours}$. 
\end{solutionordottedlines}

\part En déduire la vitesse en km/h de la planète \{planete} lors de son déplacement autour de son soleil.\\
\begin{solutionordottedlines}[5cm]
Nous savons que la vitesse se calcule grâce à la formule $\text{vitesse} = \dfrac{\text{Distance}}{\text{Durée}}$. On a donc, pour notre planète :\\
$\text{Vitesse} = \dfrac{\{distance} \text{ millions de km}}{\{duree} \text{ jours}} = \dfrac{\{vitesse1}~\text{\textcolor{red}{millions} de km}}{\textcolor{red}{\text{jour}}}$.\\  
Soit $\text{Vitesse} =\dfrac{\{vitesse1} \times \text{\textcolor{red}{ 1 000 000} de km}}{\textcolor{red}{24~\text{h}}} \simeq \{vitesse2} \dfrac{\text{km}}{\text{h}} $. 
\end{solutionordottedlines}
\end{parts}

\tabComp{D4}{D1}
'''
    mainC = '''
'''

    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())

def phasesLune(fileExercices, fileCorrections):

    phases = random.choice(["premier quartier", "dernier quartier"])
    eclipses = random.choice(["Soleil", "Lune"])
    moment = "nuit"
    phaseEclipse = "pleine Lune"
    if eclipses == "Soleil":
        moment = "journée"
        phaseEclipse = "nouvelle Lune"


    main = r'''\titledquestion{Le système Terre - Lune - Soleil : }
\begin{parts}
\part Faites un dessin de la Lune lors de la phase "\{phases}" (en "blanc" pour la partie visible et en noir ou bleu pour la partie non visible).\\
\begin{solution}[2cm]
\begin{center}'''

    if phases == "premier quartier":
        main += r'''\includegraphics[height = 2cm]{cinquiemes/Mouvement/images/PQ.png}
'''
    else :
        main += r'''\includegraphics[height = 2cm]{cinquiemes/Mouvement/images/DQ.png}
'''

    main += r'''
\end{center}
\end{solution}

\part Expliquez, avec vos propres mots et à l'aide d'un schéma, pourquoi nous voyons la Lune de cette manière.\\
\begin{minipage}{0.4\textwidth}
\begin{solutionordottedlines}[7.3cm]
Comme montré sur le schéma ci-contre, lorsque la Lune est dans la phase de \{phases}, nous voyons, depuis la Terre, une partie de la face éclairée 
de la Lune et une partie de la face non éclairée, ce qui nous apparaît donc être un quartier de Lune.
\end{solutionordottedlines}
\end{minipage}
\begin{minipage}{0.6\textwidth}
\begin{solutionorbox}[7.3cm]
\includegraphics[width = \textwidth]{cinquiemes/Mouvement/images/cycle.png}
\end{solutionorbox}
\end{minipage}

\part Durant quelle phase de la Lune peut-on voir une éclipse de \{eclipses} ? (Justifiez)\\
\begin{solutionordottedlines}[2cm]
D'après le schéma de la question précédente, une éclipse de \{eclipses} est visible seulement durant la \{phaseEclipse}.
\end{solutionordottedlines}

\part Cela se passe-t-il la journée ou la nuit ? (Justifiez)\\
\begin{solutionordottedlines}[1.5cm]
D'après le schéma et la réponse de la question précédente, une éclipse de \{eclipses} doit forcément se produire la \{moment}. En effet, un astre doit être visible pour être éclipsé.
\end{solutionordottedlines}
\end{parts}

\tabComp{D4}{D1}
'''
    mainC = '''
'''

    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())