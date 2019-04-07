import numpy as np
import sympy as sp
from random import *
a = randint(1,10)
b = randint(-10,10)
c = randint(-10,10)

x = sp.symbols('x')

f = a*x**2+b

df = sp.diff(f,x)
print(df)
