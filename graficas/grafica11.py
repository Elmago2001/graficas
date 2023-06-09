import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos
w= 2*math.pi
t= np.linspace(-w, w)
x=sin(3*t)
y=cos(4*t)
plt.plot(t, x, linewidth=3, color='g', markersize = 5, label='x')
plt.plot(t, y, linewidth=1, color='m', markersize = 4, label='y', marker='o')
plt.title('$F(t)=sin(3t)$\n$Y(t)=cos(4t)$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.grid(True)
plt.show()