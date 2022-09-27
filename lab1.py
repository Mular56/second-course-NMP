import math
x1 = 12 
x2 = 19/12 
x1_1 = 3.46 
x2_2 = 1.58 

def f (x1, x1_1, x2, x2_2):
    dx1 = abs((math.sqrt(x1) - x1_1)/ math.sqrt (x1))
    dx2 = abs((x2 - x2_2)/x2)
    if (dx1>dx2):
        print ("Друга рівність точніше")
    else:
        print("Перша рівність точніше")
        
f(x1,x1_1,x2,x2_2)