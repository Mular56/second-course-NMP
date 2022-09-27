
import numpy as np
a = np.matrix('2 1 0 0; 3 2 0 0; 1 1 3 4; 2 -1 2 3')
a_inv = np.linalg.inv(a)
print(a_inv)