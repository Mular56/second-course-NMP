from scipy import integrate
import math

eps = 0.001
a = 3.3
b = 2.5
n = 20

def f1(x):
    return (math.log10(pow(x, 2)+ 0.8)) / (x - 1)
    
def trap(f1, a, b, n):
    h=(b-a)/n
    sum=0.5*(f1(a)+f1(b))
    for i in range(1,n):
        sum+=f1(a+i*h)
    return sum*h

v,err = integrate.quad(f1, a, b) #Перевірка
if abs (trap(f1,a, b, 2*n) -trap(f1, a, b, n))/3. <= eps:
    print("Метод трапеції: ",round (trap(f1, a, b, n), 5))
print("Перевірка методу трапеції = ",round(v, 5))