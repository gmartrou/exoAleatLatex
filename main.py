#!/usr/bin/python
# -*- coding: utf-8 -*-

from preambule import *

import random

import enseignementScientifique1ere.LeSoleil.exosLeSoleil
import cinquiemes.Mouvement.exosMouvement
# import enseignementScientifique1ere.Mouvement.exosMouvement.py
# nombreExercices = 6
nombreDevoirs = 16

for j in range(1, nombreDevoirs + 1):
    if j < 10:
        j = str(0) + str(j)
    else:
        j = str(j)
    header = headerBase
    headerC = headerBase
    main = ''
    mainC = ''
    header += r'''\enteteLFMCompetences{5$^{\text{ème}}$}{Chapitres 14 et 15 : Les mouvements}%''' + '\n\n'
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
    # for exo in [exosMouvement.py.EnergieOuPuissance,
    #             exosQuatrieme.cosinus3,
    #             exosQuatrieme.cosinus4,
    #             exosQuatrieme.cosinus6
    #                                          ]:
    for i in range(1):
        exo = np.random.choice([cinquiemes.Mouvement.exosMouvement.positionPlanetes])
        main, mainC = exo(main, mainC)
        exo = np.random.choice([cinquiemes.Mouvement.exosMouvement.vitessePlanete])
        main, mainC = exo(main, mainC)
        exo = np.random.choice([cinquiemes.Mouvement.exosMouvement.phasesLune])
        main, mainC = exo(main, mainC)
            
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
