import numpy as np
import math
import matplotlib.pyplot as plt

def f(x):
    return (3*x**4) - (x**3) + (10*x**2) - (5*x) - 3

a = 1.
b = 2.
eps = 0.0001

def rec_dyhotomy(a, b, eps):
    if abs(f(b) - f(a)) < eps:
        print('Кореня немає')
        return

    mid = (a + b) / 2
    if f(mid) == 0 or abs(f(mid)) < eps:
        print(f'Корінь знаходиться в точці x = {mid}')
    elif f(a)*f(mid) < 0:
       rec_dyhotomy(a, mid, eps)
    else:
       rec_dyhotomy(mid, b, eps)

rec_dyhotomy(a, b, eps)

x = np.arange(1, 2, 0.0001)

plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод ділення навпіл')
plt.grid()
plt.show()