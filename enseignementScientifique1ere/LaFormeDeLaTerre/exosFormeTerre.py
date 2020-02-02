import random
import numpy as np
from math import *
import fonctionsSupplementaires
import fonctionsSimplifiantes

def eratosthene(fileExercices, fileCorrections):
    """Exo calcul circonférence à partir de l'angle entre deux points et de leur distance."""
    planete = random.choice(["Arcas", "Orbitar", "Intercrus", "Fafnir", "Helvetios", "Aldébaran", "Cancri",
                             "Chamelopardis", "Fomalhaut", "Gliese", "Smertrios", "Ogme"])
    distance = random.randint(600, 3000)
    ombre = random.randint(500, 899)
    ombre = ombre/1000
    angle = atan(ombre)*360/(2*pi)
    angle = round(angle, 2)
    circonference = floor(360*distance/angle)

    main = r'''\titledquestion{Méthode d'Ératosthène : }
Sur la planète \{planete}, deux villes sont le long d'un même méridien. Dans la première ville nommée A, le Soleil 
éclaire le fond d'un puit lors du solstice d'été à midi. Sur cette même planète, mais dans une autre ville, B, 
plus au Nord, un bâton de 1~m de haut fait une ombre sur le sol d'une longueur de \{ombre}~m.
\begin{parts}
\part Faire un schéma représentant la situation décrite dans l'exercice.
\begin{solutionorbox}[11cm]
\begin{center}
\includegraphics[width = 0.75\textwidth]{enseignementScientifique1ere/LaFormeDeLaTerre/eratosthene.png}
\end{center}
\end{solutionorbox}

\part L'angle entre les rayons du Soleil et le bâton planté dans le sol est de \{angle}$^{\circ}$.\\
Placez cet angle sur le schéma.\\





\part En déduire l'angle entre la ville A, le centre de la Terre et la ville B. Justifiez

\begin{solutionordottedlines}[2cm]
Les rayons du Soleil étant parallèles, l'angle entre la ville A, le centre de la Terre et la ville B est égal à 
l'angle entre les rayons du Soleil et le bâton planté dans le sol, soit \{angle}$^{\circ}$.
\end{solutionordottedlines}

\part Sachant que la distance entre A et B est de \{distance}~km, en déduire la circonférence de la 
planète \{planete}.\\
\begin{solutionordottedlines}[2cm]
Sachant qu'un tour complet représente 360$^{\circ}$, que la distance entre les villes est de \{distance}~km 
et qu'un angle de \{angle}$^{\circ}$ est formé par 
$\widehat{\mathrm{AOB}}$, une règle de 3 nous permet de conclure que la circonférence de \{planete} est 
d'environ \{circonference}~km.\\
\end{solutionordottedlines}

\end{parts}
'''

    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())

def distancesLatitudesLongitudes(fileExercices, fileCorrections):
    """Exo calcul distance entre points dont on connaît les coordonnées GPS."""
    latitudeA = random.randint(600, 900)/10
    latitudeB = random.randint(1, 299) / 10
    longitudeA = random.randint(1, 300) / 10
    longitudeB = random.randint(600, 900) / 10
    difLat = round(latitudeA - latitudeB, 1)
    rayonTerre = 6370
    circonferenceTerre = floor(2*pi*rayonTerre)
    rayonParallele = floor(rayonTerre * cos(latitudeB*pi/180))
    circonferenceParallele = floor(circonferenceTerre * cos(latitudeB*pi/180))
    distanceAB = floor(difLat*circonferenceTerre/360)
    difLong = round(longitudeB - longitudeA, 1)
    distanceBC = floor(difLong * circonferenceParallele / 360)

    main = r'''\titledquestion{Distances sur Terre : }
Nous ne connaissons que les coordonnées GPS de trois points (A, B et C) sur la Terre. En utilisant les données 
ci-dessous, répondez aux questions suivantes.\\
\textbf{DONNÉES : A(\{latitudeA}$^{\circ}$N; \{longitudeA}$^{\circ}$E), 
B(\{latitudeB}$^{\circ}$N; \{longitudeA}$^{\circ}$E), 
C(\{latitudeB}$^{\circ}$N; \{longitudeB}$^{\circ}$E). \\
Rayon de la Terre : R$_T$= 6370~km. Longueur d'un méridien L$_m$= 40023~km.\\}
\begin{parts}
\part Placez les villes A, B et C sur la carte ci-dessous :
\begin{center}
\includegraphics[width = 0.8\textwidth]{enseignementScientifique1ere/LaFormeDeLaTerre/GeodesieNB.png}
\end{center}

\part Quelle est la distance entre les points A et B ? Justifier votre réponse.
\begin{solutionordottedlines}[4cm]
Les villes A et B sont sur le même méridien. La longueur du méridien est de $2 \times \pi \times \text{R}_T \simeq$ 
\{circonferenceTerre}~km. La différence de latitude entre les villes A et B est de \{difLat}$^{\circ}$. En faisant une 
règle de 3, on trouve une distance d'environ \{distanceAB}~km.
\end{solutionordottedlines}

\part Calculer la longueur du parallèle \{latitudeB}$^{\circ}$N :
\begin{solutionordottedlines}[5cm]
Le parallèle \{latitudeB}$^{\circ}$N a une longueur égale à $L_p = L_m \times \text{cos}(\{latitudeB}^{\circ}) \simeq \{circonferenceParallele}$ km.
\end{solutionordottedlines}

\part Quelle est la distance entre les points B et C ? Justifier votre réponse.
\begin{solutionordottedlines}[5cm]
Les villes B et C sont sur le même parallèle. Le rayon du parallèle \{latitudeB}$^{\circ}$N est de 
$\text{R}_p = \text{R}_T \times \text{cos}(\{latitudeB}) \simeq \{rayonParallele}~km$. La longueur du parallèle est donc 
de $2 \times \pi \times \text{R}_p \simeq$ \{circonferenceParallele}~km. La différence de longitude entre les villes 
B et C est de \{difLong}$^{\circ}$. En faisant une règle de 3, on trouve une distance d'environ \{distanceBC}~km.
\end{solutionordottedlines}




\end{parts}
'''

    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())

def triangulation(fileExercices, fileCorrections):
    """Exo calcul distance entre points dont on connaît les coordonnées GPS."""
    angleA = random.randint(51, 70)
    angleBa = random.randint(30, 50)
    angleCa = 180 - angleA - angleBa
    angleBb = random.randint(51, 70)
    angleCb = random.randint(30, 50)
    angleD = 180 - angleCb - angleBb
    AB = random.randint(11, 19)
    BC = round(AB * sin(angleA * pi / 180) / sin(angleCa * pi / 180), 1)
    CD = round(BC * sin(angleBb * pi / 180) / sin(angleD * pi / 180), 1)

    main = r'''\titledquestion{Mesure par triangulation : }
La but de cet exercice est de calculer la longueur de CD en ayant au préalable mesuré la 
longueur AB et en ayant toutes les mesures d'angles nécessaires.

\begin{minipage}{0.33\textwidth}
\includegraphics[width = 0.9\textwidth]{enseignementScientifique1ere/LaFormeDeLaTerre/ABCD.png}
\end{minipage}
\begin{minipage}{0.33\textwidth}
Données :\\
$\widehat{\mathrm{CAB}} = \{angleA}^{\circ}$\\
$\widehat{\mathrm{ABC}} = \{angleBa}^{\circ}$\\
$\widehat{\mathrm{CBD}} = \{angleBb}^{\circ}$\\
$\widehat{\mathrm{BCD}} = \{angleCb}^{\circ}$\\
AB = \{AB}~km\\

\end{minipage}
\begin{minipage}{0.33\textwidth}
\includegraphics[width = 0.9\textwidth]{enseignementScientifique1ere/LaFormeDeLaTerre/loiSinus.png}
\end{minipage}
\begin{parts}
\part Calculez les valeurs des angles $\widehat{\mathrm{ACB}}$ et $\widehat{\mathrm{CDB}}$.
\begin{solutionordottedlines}[4cm]
$\widehat{\mathrm{ACB}} = \{angleCa}^{\circ}$\\
$\widehat{\mathrm{CDB}} = \{angleD}^{\circ}$\\
\end{solutionordottedlines}

\part En utilisant la loi des sinus, calculez la longueur BC.
\begin{solutionordottedlines}[4cm]
BC = \{BC}~km.
\end{solutionordottedlines}

\part En utilisant la loi des sinus, calculez maintenant la longueur CD.
\begin{solutionordottedlines}[4cm]
CD = \{CD}~km.
\end{solutionordottedlines}
\end{parts}
'''

    mainC = '''
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
