import numpy as np
from matplotlib import pyplot as plt
import math 
def f(x, y):
    return x + math.cos(y/math.sqrt(1.25))
x0 = 0.4
b = 1.4
h = 0.1
x = np.arange(x0, b+h, h)
n = len(x) - 1
y = np.empty(n+1)
y[0] = 0.8

for i in range(n):
    y[i+1] = y[i] + (f(x[i], y[i]) + f(x[i+1], y[i] + h*f(x[i], y[i])))*h/2

y_rounded = np.round_(y, 4)

print ('x = ', x, '\ny = ', y_rounded)

plt.plot(x, y, 'o', x, y, 'purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера-Коші')
plt.legend(['точки', 'x + cos(y/math.sqrt(1,25))'])
plt.grid()
plt.show()


