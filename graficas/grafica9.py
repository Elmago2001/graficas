import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos
w= 2*math.pi
t= np.linspace(0,w)
x=cos(t)**3
y=sin(t)**3
plt.plot(t, x, linewidth=3, color='k', markersize = 10, marker = '*', label='x')
plt.plot(t, y, linewidth=3, color='m', markersize = 10, marker = '*',label='y')
plt.title('$F(t)=cos^{3}(t)$\n$Y(t)=sin^{3}(t)$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.legend()
plt.show()