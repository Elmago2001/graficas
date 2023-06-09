import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
import math
w=4*math.pi
t=np.arange(0,w,0.04)
r=105+100*sin(4.5*t)
z=t-np.divide(cos(10*t), 10)
x=320+r*cos(z)
y=-240-r*sin(z)
plt.plot(x, y, linewidth=5, color='k', label='y')
plt.fill_between(x,y,color='violet')
plt.axis('equal')
plt.axis('off')
plt.show()