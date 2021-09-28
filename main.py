#!/usr/bin/python
# -*- coding: utf-8 -*-

from preambule import *

import random

# On importe les dossiers contenants les exercices en Python
import enseignementScientifique1ere.LeSoleil.exosLeSoleil
import enseignementScientifique1ere.LaFormeDeLaTerre.exosFormeTerre
import cinquiemes.Energie.exosEnergie
import cinquiemes.Mouvement.exosMouvement
# import enseignementScientifique1ere.Mouvement.exosEnergie.py

# nombreExercices = 6   # Le nombre d'exercices que tu veux par devoir. Dans le cas où tu as un nombre variable d'exo
                        # (C'est pas le cas dans la suite, raison pour laquelle c'est commenté).
nombreDevoirs = 19       # Max 99 mais en modifiant le code on peut aller plus loin.

for j in range(1, nombreDevoirs + 1):
    if j < 10:
        j = str(0) + str(j)
    else:
        j = str(j)
    header = headerBase
    headerC = headerBase
    main = ''
    mainC = ''

    # 3 types d'entêtes, explicites je pense.
    # header += r'''\enteteLFMCompetencesNotes{5$^{\text{ème}}$}{Chapitres 16 à 21 : Énergie et électricité.}{20}%''' + '\n\n'
    # header += r'''\enteteLFMCompetences{5$^{\text{ème}}$}{Chapitres 16 à 21 : Énergie et électricité.}%''' + '\n\n'
    # header += r'''\enteteLFM{Chapitre 8 : La forme de la Terre}%''' + '\n\n'
    header += r'''\enteteLFM{Thème 1 : Chapitre 1 : Le rayonnement solaire}%''' + '\n\n'
    header += r'''\begin{questions}
'''
    nomFichierExo = 'devoir' + str(j)
    nomFichierCor = 'correction' + str(j)

    """Exemple d'exos dans le fichier. Il y a 2 exos, je change ensuite de page avec \newpage puis un dernier exo"""
    exo = enseignementScientifique1ere.LeSoleil.exosLeSoleil.EnergieOuPuissance
    main, mainC = exo(main, mainC)
    exo = enseignementScientifique1ere.LeSoleil.exosLeSoleil.tempEtoile
    main, mainC = exo(main, mainC)

    """Tout ce qui est à la suite correspond à la compilation, une première fois avec la commande \noprintanswers qui
    n'affiche donc pas la correction (c'est à dire l'énoncé) et une seconde fois sans ça. Si tu as bien mis les
    corrections comme il faut elles seront affichées dans ce deuxième fichier."""

    contentExercices = header + r'''\noprintanswers
    ''' + main + footer
    
    with open(nomFichierExo + '.tex', 'w', encoding='utf-8') as f:
        f.write(contentExercices)
    
    # commandLine =
    subprocess.check_call(['xelatex', nomFichierExo + '.tex'])
    os.unlink(nomFichierExo + '.aux')
    os.unlink(nomFichierExo + '.log')
    # os.unlink(nomFichierExo+'.tex')
    
    contentCorrections = header + main + footer
    
    with open(nomFichierCor + '.tex', 'w', encoding='utf-8') as f:
        f.write(contentCorrections)
    
    # commandLine =
    subprocess.check_call(['xelatex', nomFichierCor + '.tex'])
    
    os.unlink(nomFichierCor + '.aux')
    os.unlink(nomFichierCor + '.log')
    # os.unlink(nomFichierCor+'.tex')
