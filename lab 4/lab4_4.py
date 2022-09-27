
import numpy as np
a = np.matrix('1 2 3; -1 2 1; 1 3 2')
a_det = np.linalg.det(a) #Визначник матриці
print(format(a_det, '.9g'))