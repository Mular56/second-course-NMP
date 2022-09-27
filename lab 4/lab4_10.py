import numpy as np
import pandas as pd
a = np.random.randint(-9, 9, (4, 6))
print("a = \n", a)

b = [*map(sum, zip(*a))]
print('Середнє арифметичне кожного стовпця = ', b)

min = min(b)
print('Мінімальне значення = ' , min)



