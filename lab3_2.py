import numpy as np
import math
from scipy.misc import derivative

def f(x):
    return 3*x**4 + x**3 + 10*x**2 - 3*x - 9

a = -2.
b = -1/2
eps = 0.001 
 
def komb(a, b, eps):
    if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0):
        an = a
        bn = b
        an_1 = an - f(an)*(bn - an)/(f(bn) - f(an))
        bn_1 = bn - f(bn)/derivative(f, bn, n = 1)
    else:
        an_1 = an - f(an)/derivative(f, an, n = 1)
        bn_1 = bn - f(bn)*(bn - an)/(f(bn) - f(an))
    while (abs(bn_1 - an_1)>eps):
        an = an_1
        bn = bn_1
    if (derivative(f, an, n = 1) * derivative(f, an, n= 2) > 0):
        an_1 = an - f(an) * (bn - an)/(f(bn) - f(bn))
        bn_1 = bn - f(bn) - f(bn)/derivative(f, bn, n = 1)
    else:
        an_1 = an - f(an) - f(an)/derivative(f, an, n = 1)
        bn_1 = bn - f(bn)*(bn - an)/(f(bn) - f(an))
    return print("Розв’язання нелінійного рівняння комбінованим методом x = ", x)
komb(a, b, eps)