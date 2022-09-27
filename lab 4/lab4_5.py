
import numpy as np
a = np.matrix('2 3 4 1; 1 2 3 4; 3 4 1 2; 4 1 2 3')
a_det = np.linalg.det(a) #Визначник матриці
print(format(a_det, '.9g'))