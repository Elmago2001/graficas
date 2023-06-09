import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos
w= 2*math.pi
t= np.linspace(-w, w)
x=t+2*sin(2*t)
y=t + 2*cos(5*t)
plt.plot(t, x, linewidth=3, color='k', markersize = 2, label='x')
plt.plot(t, y, linewidth=3, color='m', markersize = 2, label='y')
plt.title('$F(t)=t+2sin(2t)\n$Y(t)=t+2cos(5t)$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.legend
plt.show()