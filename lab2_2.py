import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

def f(x):
    return (3*x**4) - (x**3) + (10*x**2) - (5*x) - 3

a = 1.
b = 2.
eps = 0.0001 

def hord (a, b, eps):
    if abs(f(b) - f(a)) < eps:
        print('Кореня немає')
        return
    if (f(a)*derivative(f, a, n = 2)):
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    while (abs(f(xi_1) - f(xi)) > eps):
        xi = xi_1
        xi_1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))

    else:
        print(f'Корінь  знаходиться в точці x =', xi_1)
hord(a, b, eps)