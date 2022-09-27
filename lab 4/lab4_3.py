
import numpy as np
a = np.matrix('5 8 -4; 6 9 -5; 4 7 -3')
b = np.matrix('3 2 5; 4 -1 3; 9 6 5')
c = a.dot(b)
print(c)