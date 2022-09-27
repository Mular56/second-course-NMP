import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = -1
y0 = -0.5
delta = 0.1

def f1(y):
    return (math.cos(y + 0.5) - 2) #задаємо функції
def f2 (x):
    return ((-1 + math.sin(x)) / 2) #задаємо функції

def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Simple iteration:')
    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)
iter(x0,y0,0.0001)

def f3(x): #Задаємо функцію для перевірки
    return math.cos(x + 0.5) - 2, -1 + math.sin(x) / 2
s = optimize.root(f3, [0.,0.], method = 'hybr') #Перевірка розв*язку 
print ('Chek',s.x)
print ('Chek',s.x)