import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos
w= 2*math.pi
t=np.linspace(0, w, 100)
xt=(1+2*sin(t))*(cos(t))
yt=(1+2*sin(t))*(sin(t))
plt.plot(t, xt, linewidth=3, color='k', markersize = 10, marker = '*', label='Xt')
plt.plot(t, yt, linewidth=3, color='m', markersize = 10, marker = 'o', label='Yt')
plt.title('$F(t)=1+2sin(t)*cos(t)$\n$Y(t)=1+2sin(t)*sin(t)$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.show()