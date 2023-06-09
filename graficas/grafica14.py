import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
import math
w=2*math.pi
t=np.arange(0,w,0.015)
r=-250*sin(5*t)*cos(4*t)
z=t+sin(r/100)
x=320+r*cos(z)
y=-240-r*sin(z)
plt.plot(x, y, linewidth=5, color='k', label='y')
plt.fill_between(x,y,color='green')
plt.axis('equal')
plt.axis('off')
plt.show()