import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib import lines, markers
from cycler import cycler

monochrome = (cycler('color', ['k']) * cycler('linestyle', ['-', '--', ':', '=.']) * cycler('marker', ['^',',', '.']))
c = 3*10**17 #nm.s-1
h = 6.62607015*10**(-16) #nJ.ns
k = 1.380649*10**(-5) #nJ.GK-1
xmin = 100
xmax = 600
X = np.linspace(xmin, xmax, 30)
f, ax = plt.subplots(1, 1, figsize=(12.75, 6))
plt.xlim(xmin, xmax)
ax.get_yaxis().set_visible(False)
plt.box(False)
mpl.rc('axes', titlesize=40)
Y = 0*X
ax.plot(X, Y, 'k')
ax.set_prop_cycle(monochrome)
for i in range(11000, 15200, 1000):
    Y = 10 ** (-3) * 2 * h * c ** 2 / (X ** 5 * (np.exp(h * c / (X * k * i)) - 1))
    label = str(i) + ' K'
    ax.plot(X, Y, label=label)

plt.xlabel("longueur d'onde (nm)")
plt.legend()
plt.show()

f.savefig("11k15k.pdf", bbox_inches='tight', transparent=True)

