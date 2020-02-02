#!/usr/bin/python
# -*- coding: utf-8 -*-

from preambule import *

import random

import enseignementScientifique1ere.LeSoleil.exosLeSoleil
import enseignementScientifique1ere.LaFormeDeLaTerre.exosFormeTerre
import cinquiemes.Energie.exosEnergie
import cinquiemes.Mouvement.exosMouvement
# import enseignementScientifique1ere.Mouvement.exosEnergie.py
# nombreExercices = 6
nombreDevoirs = 5

for j in range(1, nombreDevoirs + 1):
    if j < 10:
        j = str(0) + str(j)
    else:
        j = str(j)
    header = headerBase
    headerC = headerBase
    main = ''
    mainC = ''
    header += r'''\enteteLFMCompetences{5$^{\text{ème}}$}{Chapitres 16 à 21 : Énergie et électricité.}%''' + '\n\n'
    # header += r'''\enteteLFM{Chapitre 8 : La forme de la Terre}%''' + '\n\n'
    header += r'''\begin{questions}
'''
    nomFichierExo = 'exercices' + str(j)
    nomFichierCor = 'corrections' + str(j)
    # for chapitre in niveau:
    #     for i in range(20):
    #         for exo in chapitre:
    #             main, mainC = exo(main, mainC)
        
    #     exo = np.random.choice(chapitre)
    #     main, mainC = exo(main, mainC)
    # for exo in [exosEnergie.py.EnergieOuPuissance,
    #             exosQuatrieme.cosinus3,
    #             exosQuatrieme.cosinus4,
    #             exosQuatrieme.cosinus6
    #                                          ]:
    for i in range(1):
        exo = np.random.choice([cinquiemes.Energie.exosEnergie.centraleElectrique])
        main, mainC = exo(main, mainC)
        exo = np.random.choice([cinquiemes.Energie.exosEnergie.conducteurIsolant])
        main, mainC = exo(main, mainC)
        main += r'''
\newpage
'''
        exo = np.random.choice([cinquiemes.Energie.exosEnergie.circuitSerieDerivation])
        main, mainC = exo(main, mainC)
        # exo = np.random.choice([enseignementScientifique1ere.LaFormeDeLaTerre.exosFormeTerre.triangulation])
        # main, mainC = exo(main, mainC)
            
    #for i in range(10):
        # chapitre = vecteurs
        # exo = np.random.choice(chapitre)
        # main, mainC = exo(main, mainC)
        # chapitre = probabilites
        # exo = np.random.choice(chapitre)
        # main, mainC = exo(main, mainC)
        # #for exo in chapitre:
        # exo = np.random.choice([exosQuatrieme.cosinus5, exosQuatrieme.cosinus6])
        # main, mainC = seconde.tableauxDeSignes.problemesSimples.tableauDeSigneBasique(main, mainC)
        # main, mainC = exo(main, mainC)

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
