#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import numpy as np
import fonctionsSimplifiantes















def exerciceDemo(fileExercices, fileCorrections):
    """Description de l'exercice."""
    
    # Définition des variables.
    a = 2
    b = 3
    # Fin des variables.
    
    # Enoncé de l'exercice.
    main = r'''\exo{Exo démo}
J'ai achété \{a} pommes et\{b} poires.
Combien ai-je acheté de fruits ?
'''
    # Fin de l'énoncé.
    
    # Fichier texte de la correction.
    mainC = r'''\cor{Nom de l'exercice}
J'ai acheté \{a}+\{b} = \{a+b} fruits.
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())


def exercice(fileExercices, fileCorrections):
    """Description de l'exercice."""
    
    # Définition des variables.
    
    # Fin des variables.
    
    # Enoncé de l'exercice.
    main = r'''\exo{Nom de l'exercice}
'''
    # Fin de l'énoncé.
    
    # Fichier texte de la correction.
    mainC = r'''\cor{Nom de l'exercice}
'''
    return fonctionsSimplifiantes.endExercice(main, mainC, fileExercices, fileCorrections, locals())
