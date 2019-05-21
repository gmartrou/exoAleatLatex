#!/usr/bin/python
# -*- coding: utf-8 -*-

from preambule import *

import seconde.tableauxDeSignes.problemesSimples
import seconde.probas.problemes
import seconde.Vecteurs.problemesCoordonnees
import seconde.Vecteurs.applicationFormules
import seconde.Vecteurs.problemesChasles
import seconde.fonctionsSecondDegre.traceCourbes

# # Chapitres 4ème
# cosinus = [exosQuatrieme.cosinus1,
#            exosQuatrieme.cosinus2,
#            exosQuatrieme.cosinus3,
#            exosQuatrieme.cosinus4,
#            ]
# puissances = [exosQuatrieme.puissance1,
#               exosQuatrieme.puissance2,
#               exosQuatrieme.puissance3,
#               ]
# equations = [exosQuatrieme.equation1,
#              exosQuatrieme.equation2,
#              exosQuatrieme.equation3]
# pythagore = [exosQuatrieme.pythagore1,
#              exosQuatrieme.pythagore2,
#              exosQuatrieme.pythagore3,
#              exosQuatrieme.pythagore4,
#              exosQuatrieme.pythagore5,
#              ]
# fractions = [exosQuatrieme.fraction1,
#              ]
#
# calculLitteral = [exosQuatrieme.doubleDeveloppement,
#                   ]
#
# # Chapitres 2nd
#
# fonctionsAffines = [exosSeconde.fonctionsAffineIntersection,
#                     ]
#
# tableauDeSigne = [exosSeconde.tableauDeSigneUn1,
#                   exosSeconde.tableauDeSigneUn2,
#                   exosSeconde.tableauDeSigneUn3,
#                   exosSeconde.tableauDeSigneUn4,
#                   exosSeconde.tableauDeSigneDeux1,
#                   exosSeconde.tableauDeSigneDeux2,
#                   exosSeconde.tableauDeSigneDeux3,
#                   exosSeconde.tableauDeSigneDeux4,
#                   ]
vecteurs = [seconde.Vecteurs.problemesCoordonnees.vecteursParall1,
            seconde.Vecteurs.problemesCoordonnees.vecteursParall2,
            seconde.Vecteurs.problemesCoordonnees.vecteursCalculCoord1,
            seconde.Vecteurs.problemesCoordonnees.vecteursDroitesColineaires,
            ]

probabilites = [seconde.probas.problemes.probasMaladies,
                seconde.probas.problemes.probasViennoiseries]

fonctions = [
             seconde.fonctionsSecondDegre.traceCourbes.fonctionsSecondDegreTrace,
             seconde.fonctionsSecondDegre.traceCourbes.fonctionsHomographiqueTrace]
#
# # Niveaux
# quatrieme = [cosinus,
#              pythagore,
#              equations,
#              puissances,
#              fractions,
#              calculLitteral,
#              ]
#
chapitresSeconde = [
#                    tableauDeSigne,
 #                    vecteurs,
#                     fonctionsAffines,
#                     probabilites,
                     fonctions,
                     ]
#
niveau = chapitresSeconde

# nombreExercices = 6
nombreDevoirs = 2

for j in range(1, nombreDevoirs + 1):
    if j < 10:
        j = str(0) + str(j)
    else:
        j = str(j)
    header = headerBase
    headerC = headerBase
    main = ''
    mainC = ''
    header += r'''\enteteLSMI{\today}{Entrainement Interrogation fonctions}%''' + '\n\n'
    headerC += r'''\enteteLSMI{\today}{Correction entrainement Interrogation fonctions}%''' + '\n\n'
    
    nomFichierExo = 'exercices' + str(j)
    nomFichierCor = 'corrections' + str(j)
    for chapitre in niveau:
        for i in range(20):
            for exo in chapitre:
                main, mainC = exo(main, mainC)
        
    #     exo = np.random.choice(chapitre)
    #     main, mainC = exo(main, mainC)
    # for exo in [exosQuatrieme.cosinus2,
    #             exosQuatrieme.cosinus3,
    #             exosQuatrieme.cosinus4,
    #             exosQuatrieme.cosinus6]:
            #exo = np.random.choice([exosQuatrieme.cosinus6])
            
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
    
    contentExercices = header + main + footer
    
    with open(nomFichierExo + '.tex', 'w', encoding='utf-8') as f:
        f.write(contentExercices)
    
    # commandLine =
    subprocess.check_call(['pdflatex', nomFichierExo + '.tex'])
    os.unlink(nomFichierExo + '.aux')
    os.unlink(nomFichierExo + '.log')
    # os.unlink(nomFichierExo+'.tex')
    
    contentCorrections = headerC + mainC + footerC
    
    with open(nomFichierCor + '.tex', 'w', encoding='utf-8') as f:
        f.write(contentCorrections)
    
    # commandLine =
    subprocess.check_call(['pdflatex', nomFichierCor + '.tex'])
    
    os.unlink(nomFichierCor + '.aux')
    os.unlink(nomFichierCor + '.log')
    # os.unlink(nomFichierCor+'.tex')
