import numpy as np
from math import factorial
import matplotlib.pyplot as plt

x=[0.17, 0.18, 0.19, 0.20, 0.21, 0.22]
y=[5.4739, 6.0496, 6.6859, 7.3891, 8.1662, 9.0250]
h = x[1] - x[0]

x1=0.1
x2=0.9

q=(x1 - x[0])/h
q1 = (x2-x[-1])/h

def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0) 
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)


s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print ('Значення функції в точці x1 = ', x1, 'використовуючи першу інтерполяційну формулу Ньютона', 
round(n_1,5))

#Друга інтерполяційна формула Ньютона
k_1 = y[-1] + q1 * n(y,1)[-2] + q1 * (q1 + 1) * n(y,2)[-3] / factorial(2)
k_2 = q1 * (q1 + 1) * (q1 + 2) * n(y,3)[-1] / factorial(3)
k_3 = q1 * (q1 + 1) * (q1 + 2) * (q1 + 3) * n(y,4)[-1] / factorial(4)
k_4 = q1 * (q1 + 1) * (q1 + 2) * (q1 + 3) * (q1 + 4) * n(y,5)[-1] / factorial(5)
n_2 = k_1 + k_2 + k_3 + k_4
print ('Значення функції в точці x2 = ', x2, 'використовуючи другу інтерполяційну формулу Ньютона', 
round(n_2,5))

x_1 = np.linspace(np.min(x), np.max(x))
y_1 = np.interp(x_1, x, y)
plt.plot(x, y, 'o', x_1, y_1)
plt.title('Графік інтерполяційної функції')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()