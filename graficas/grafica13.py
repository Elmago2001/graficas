import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
import math
w=2*math.pi
t=np.linspace(0,w)
r=(2-2*sin(t))+(sin(t)*np.divide(np.sqrt(np.absolute(cos(t))), (sin(t)+1.4)))
x=r*cos(t)
y=r*sin(t)
#plt.plot(y, x, linewidth=5, color='b', label='x')
plt.plot(x, y, linewidth=5, color='k', label='y')
#plt.plot(-x, -y, linewidth=1, color='k', label='y')
#plt.plot(-y, -x, linewidth=1, color='k', label='y')
#plt.plot(t, r, linewidth=3, color='r', markersize = 10, label='r')
plt.fill_between(x,y,color='red')
plt.axis('equal')
plt.axis('off')
plt.legend()
plt.show()