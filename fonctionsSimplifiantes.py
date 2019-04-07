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
