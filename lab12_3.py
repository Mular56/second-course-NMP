from scipy import integrate
import math

eps = 0.001
a = 1.3
b = 0.5
n = 8

def f1(x):
    return 1 / math.sqrt(pow(x, 2) + 2)

def simpson(a,b,n):
    h = (b - a) / n
    integr = f1(a) + f1(b)
    for i in range(1,n):
        k = a + i*h
        if i%2 == 0:
            integr += 2 * f1(k)
        else:
            integr += 4 * f1(k)
    integr *= h/3
    return integr

if abs(simpson(b, a, 2*n) -simpson(b, a, n))/ 15. <= eps:
    print("Метод Сімпсона: ",round (simpson(b, a, n), 5))

v,err = integrate.quad(f1,b, a)#Перевірка
print("Перевірка методу Сімпсона = ",round(v, 5))