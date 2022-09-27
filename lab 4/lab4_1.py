
import numpy as np
a = np.matrix('1 2; 4 -1')
b = np.matrix('2 -3; -4 1')
c1 = a.dot(b)
c2 = b.dot(a)
c = c1 - c2
print(c)