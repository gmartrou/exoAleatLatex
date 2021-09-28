import random
import numpy as np
from math import *
import fonctionsSupplementaires
import fonctionsSimplifiantes

def EnergieOuPuissance(fileExercices, fileCorrections):
    """Calcul de l'énergie rayonnée par une étoile pendant une certaine durée en connaissant la puissance rayonnée par l'étoile."""
    exposant = random.randint(21, 24)
    coeff = round(random.uniform(1.2, 9.8), 1)
    P = coeff*10**exposant #puissance rayonnée par l'étoile
    pT = fonctionsSimplifiantes.notation_scientifique(P, 1)
    t = random.choice([60, 3600, 3600*24]) #temps en seconde pendant lequel on veut connaître l'énergie rayonnée
    E = P*t
    eT = fonctionsSimplifiantes.notation_scientifique(E, 1)
    etoile = random.choice(['Sirius', 'Achernar', 'Rigal', ' Mira', 'Crucis', 'Altair', 'Beltelgeux', 'Vega', 'Antares', 'R. Hydrae', 'Canopus', 'Arcturus', 'Capella'])
    duree = 'minute'
    unune = 'Une'
    if t == 3600:
        duree = 'heure'
        unune = 'Une'
    elif t == 3600 * 24:
        duree = 'jour'
        unune = 'Un'
    main = r'''
%Premier exercice
\titledquestion{Énergie ou puissance : }
L'étoile \{etoile} rayonne une puissance de $\{pT}~\si{W}$.
\begin{parts}
\part[5] Calculer l'énergie, $\Delta E$, rayonnée par \{etoile} chaque \{duree}.\\
\textbf{\underline{DONNEE} :} \{unune} \{duree} = \{t} secondes.
\begin{solutionordottedlines}[4cm]
\{etoile} rayonne une puissance de $\{pT}~\si{\watt}$. On sait que l'énergie rayonnée, $\Delta E$, 
par un objet rayonnant une puissance $P$ durant un intervalle de temps $\Delta t$ est obtenue par la formule 
$\Delta E = P \times \Delta t$. Donc, chaque seconde, elle rayonne une énergie 
$\Delta E = \{pT}~\si{\watt} \times 1~\si{\second} = \{pT}~\si{\joule}$. 
Chaque \{duree}, l'énergie rayonnée par \{etoile} sera donc égale à 
$\Delta E = \{pT}~\si{\joule} \times \{t} \simeq \{eT}~\si{\joule}$
\end{solutionordottedlines}
\part[5] En déduire la masse perdue par \{etoile} chaque \{duree}.\\
\textbf{\underline{DONNEE} :} $\Delta E = \Delta m \times c^2$.
\begin{solutionordottedlines}[4cm]
Chaque \{duree}, \{etoile} rayonne $\{eT}~\si{\joule}$. La relation d'Einstein $\Delta E = \Delta m \times c^2$, 
que l'on peut aussi écrire $\Delta m = \dfrac{\Delta E}{c^2}$ nous permet de calculer la masse perdue par 
l'étoile \{etoile} chaque \{duree}.\\
Chaque \{duree} la perte de masse $\Delta m = \dfrac{\{eT}~\si{\joule}}{(300000~\si{\km \per \second})^2}= 
\dfrac{\{eT}~\si{\joule}}{(3\times 10^8~\si{\meter \per \second})^2}$. 
Soit $\Delta m \simeq \{notation_scientifique((P*t)/(3*10**8),1)}~\si{\kilogram}$
\end{solutionordottedlines}
\end{parts}
'''
    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())

def tempEtoile(fileExercices, fileCorrections):
    etoile = random.choice(
        ['Sirius', 'Achernar', 'Rigal', ' Mira', 'Crucis', 'Altair', 'Beltelgeux', 'Vega', 'Antares', 'R. Hydrae',
         'Canopus', 'Arcturus'])
    main = r'''
\titledquestion{Température d'une étoile : }
Dans les documents ci-après, les sept premiers graphiques donnent l'émission énergétique émise en fonction de la longueur d'onde (en \si{\nm}) pour des corps noirs à différentes températures. Le huitième graphique représente l'irradiance spectrale en fonction de la longueur d'onde (en \si{\um}) de différentes étoiles.\\
\textbf{\underline{DONNEE} :} 1 \si{\um} = 1 000 \si{\nm}

\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/4k5k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/1k14k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/3k4k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/6k10k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/11k15k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/5k6k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/2k3k.pdf}\\
\includegraphics[width=\textwidth]{enseignementScientifique1ere/LeSoleil/plankLaw/Stars.png}\\

\begin{parts}
\part[5] À partir des documents, donner la température de l'étoile \{etoile}. Vous ferez cela en justifiant toutes les étapes de votre raisonnement et en traçant tout ce qui est nécessaire sur les graphiques.\\
\begin{solutionordottedlines}[5cm]
À partir du huitième graphique, on remarque que la longueur d'onde correspondant au maximum d'intensité, $\lambda_{max}$, est d'environ $1,5~\si{\um}$, soit $\lambda_{max} \simeq 1 500~\si{\nm}$.\\
En se basant sur le cinquième graphique, on remarque que cela correspond à un corps à une température d'environ 2000~\si{\kelvin}.
\end{solutionordottedlines}

\part[5] En utilisant la loi de Wien, calculer la température de l'étoile \{etoile}. Comparez ces deux valeurs. \\
\textbf{Rappel :} $\lambda_{max} = \dfrac{k}{T}$ avec $k = 2,898 \times 10^{-3}~\si{\meter \kelvin}$.\\
\begin{solutionordottedlines}[4cm]
On sait que $\lambda_{max} \simeq 1 500~\si{\nm}$ et, d'après la loi de Wien $k = \lambda_{max} \times T$ que l'on peut aussi écrire $T = \dfrac{k}{\lambda_{max}} \simeq \dfrac{2,898 \times 10^{-3}~\si{\meter \kelvin}}{1 500~\si{\nm}} \simeq \dfrac{2,898 \times 10^{-3}~\si{\meter \kelvin}}{1 500 \times 10^{-9}~\si{\meter}} \simeq 2415~\si{\kelvin}$. On a une valeur proche de ce que l'on a trouvé grâce au graphique.
\end{solutionordottedlines}
\end{parts}
'''
    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
