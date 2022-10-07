import numpy as np
import math

mas_x = [2.4,2.6,2.8,3.0,3.2,3.4]
mas_y = [3.526,3.782,3.945,4.043,4.104,4.155]
h = mas_x[1] - mas_x[0]
print (h)

mas_1 = []
mas_2 = []
mas_3 = []
mas_4 = []

for i in range(len(mas_y)):
    mas_1.append(mas_y[i] - mas_y[i-1])
mas_1.pop (0)
print('mas_1 = ', mas_1)

for j in range(len(mas_1)):
    mas_2.append(mas_1[j] - mas_1[j-1])
mas_2.pop (0)
print('mas_2=',mas_2 )

for k in range(len(mas_2)):
    mas_3.append(mas_2[k] - mas_2[k-1])
mas_3.pop (0)
print('mas_3=',mas_3)

for l in range(len(mas_3)):
    mas_4.append(mas_3[l] - mas_3[l-1])
mas_4.pop (0)
print('mas_4=',mas_4)

y1 = 1/ h * (mas_1[1] - (mas_2[1]/ 2) + (mas_3[1] /3) - (mas_4[1]/4))
y2 = 1/ (h**2) * (mas_2[1] - mas_3[1] + 11/12*mas_4[1])

print ('Перша похідна =', y1)
print ('Друга похідна =', y2)