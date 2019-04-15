#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np


def repereDebut(main, xmin, ymin, xmax, ymax):
    taille = 0.4*(xmax - xmin)/(ymax - ymin)
    main += r'''\begin{adjustbox}{width='''+str(taille)+r'''\textwidth,center}
    \begin{tikzpicture}[]
    \tiny
    \begin{axis}[axis lines=middle, 
          xlabel=$x$,xlabel style={anchor=north},
          ylabel=$y$,ylabel style={anchor=east},
          x axis line style = {-latex}, y axis line style = {-latex},
          xtick={'''+str(xmin + 1)+r','+str(xmin + 2)+r',...,'+str(xmax - 1)+r'''},
          xticklabels={'''+str(xmin + 1)+r','+str(xmin + 2)+r',...,'+str(xmax - 1)+r'''},
          ytick={'''+str(ymin + 1)+r','+str(ymin + 2)+r',...,'+str(ymax - 1)+r'''},
          yticklabels={'''+str(ymin + 1)+r','+str(ymin + 2)+r',...,'+str(ymax - 1)+r'''},
          ymin = '''+str(ymin)+r''',
          ymax = '''+str(ymax)+r''',
          xmin = '''+str(xmin)+r''',
          xmax = '''+str(xmax)+r''',
          axis equal image,
          xmajorgrids,
          ymajorgrids,
          restrict y to domain='''+str(ymin)+r''':'''+str(ymax)+r''',
          ]\\
    '''
    return main


def repereFin(main):
    main += r'''\end{axis}
    \end{tikzpicture}
    \end{adjustbox}\\
    '''
    return main


def signT(x):
    if np.signbit(x):
        return ' - '
    else:
        return ' + '
    
    
def signOpT(x):
    print('banane')
    if np.signbit(x):
        return ' - '
    else:
        return ' + '


def varReplacerOld(texte, tableau):
    for element in tableau:
        texte = texte.replace('\{' + element + '}', str(tableau[element]))
    return texte


def varReplacer(text, tableau):
    locals().update(tableau)
    encore = False
    if text.find("\{") != -1:
        encore = True
    while encore:
        debut = text.find("\{")
        fin = text.find("}", debut + 2)
        mySubString = text[debut + 2:fin]
        text = text.replace("\{" + mySubString + "}", str(eval(mySubString)))
        if "\{" not in text:
            encore = False
    return text


def endExercice(main, mainC, fileExercices, fileCorrections, localV):
    main += '\n' + '\n'
    mainC += '\n' + '\n'
    main = varReplacer(main, localV)
    mainC = varReplacer(mainC, localV)
    fileExercices += main
    fileCorrections += mainC
    return fileExercices, fileCorrections
