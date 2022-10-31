import sympy as sp
from math import factorial

def taylor(x):
    y = 0
    d1 = sp.diff(f, x) # перша похідна
    d2 = sp.diff(d1, x) #друга похідна
    d3 = sp.diff(d2, x)  # третя похідна
    print('d1=',d1,'d2=',d2,'d3=',d3)
    y += f + d1*x + d2*(x-0)**2/factorial(2) + d3*(x-0)**3/factorial(3)
    print ('y = ', y)
    
    return y
x = sp.symbols('x')
f = sp.sin(2*x) - (2 * x)
taylor_x = taylor(x)

sp.plot(taylor_x, f, (x, -1, 1), label='Taylor')