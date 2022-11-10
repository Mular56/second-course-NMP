from scipy import integrate
import math

eps = 0.001
a = 2.5
b = 1.3
n = 10

def f1(x):
    return 1/math.sqrt(0.2*x + 1)
def left_rec(f1,a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(0,n):
        sum+=f1(a+i*h)
    return sum*h

v,err = integrate.quad(f1, a, b) #Перевірка

if abs(left_rec(f1, a, b, 2*n) - left_rec(f1, a, b, n))/3. <=eps:
    print("лівий прямокутник: ",round (left_rec(f1, a, b, n), 5))
def right_rec(f1,a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(1,n+1):
        sum+=f1(a+i*h)
    return sum*h
print("правильний прямокутник: ",round (right_rec(f1, a, b, n), 5))
def aver_rec(f1,a, b, n):
    h=0.08
    sum=0
    for i in range(0,n):
        sum+=f1(a+i*h)
    return sum*h
print("середній прямокутник: ",round (aver_rec(f1,1.2,2,10), 5))
print("Перевірка методу прямокутника = ",round (v, 5))