import matplotlib.pyplot as plt
import numpy as np
import math
from numpy import sin, cos
w= 4* math.pi
x=np.linspace(0,w)
fx=(cos(2*x)+sin(3*x))
vx=(-2*sin(2*x)+3*cos(3*x))
plt.plot(x, fx, linewidth=3, color='k', marker='_', label= 'fx')
plt.plot(x, vx, linewidth=3, color='b', marker='o', label= 'vx')
plt.title('$F(x)=cos(2x)+sin(3x)$ \n V(x)=-2sin(2x)+3cos(3x)')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.legend()
plt.show()
