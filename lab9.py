import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [0.8, 1.2, 1.4, 1.7, 2.2]
y = [3.18, 2.15, 4.18, 3.81, 5.07]

spl = UnivariateSpline(x, y)
xs = np.linspace(0, 4.5, 1000)
plt.plot(x,y,'ro', xs, spl(xs), 'g', label="Апроксимуюча функція", color='green')
plt.show()