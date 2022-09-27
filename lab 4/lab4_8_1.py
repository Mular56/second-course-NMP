import numpy as np
A = np.matrix('3 2 1; 2 -1 1; 1 5 0')
B = np.matrix('5; 6; -3')
print('A = \n', A)
print('B = \n',B)
A_inv = np.linalg.inv(A)
print(A_inv)
X = A_inv.dot(B)
print('X = \n',X)

X = np.linalg.solve(A, B)

print('Перевірка X = \n', X)