import matplotlib.pyplot as plt
import numpy as np
from numpy import sin
t = np.linspace(0,24,250)
def h(t):
     return (sin(2*t)*np.exp(-0.1*t))
plt.plot(t, h(t), linewidth=3, color='b', marker='o')
plt.title('$sin(2t).exp^{-0.1t}$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.show()