import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos
w= 4*math.pi
t=np.linspace(0, w, 100)
ft=sin(3*t)*cos(2*t)
gt= (cos(2*t)/2)+(5*cos(5*t)/2)
plt.plot(t, ft, linewidth=3, color='k', markersize = 10, label='Ft')
plt.plot(t, gt, linewidth=3, color='c', markersize = 10, label='Gt')
plt.title('$F(t)=sin(3t)*cos(2t)$\n$G(x)=cos(2t)/2+5cos(5t)/2$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.legend()
plt.grid(True)
plt.show()
