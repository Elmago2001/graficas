import math
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0, 2, 100)
fx= x*(np.exp(-3*x))
gx= 1-3*(np.exp(-3*x))
plt.plot(x, fx, linewidth=3, color='r', markersize = 3, marker = 's', label='fx')
plt.plot(x, gx, linewidth=3, color='c', markersize = 3, marker = 's', label='gx')
plt.title('$F(x)=xe^{-3x}$\n $G(x)=1-3e^{-3x}$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.grid(True)
plt.legend()
plt.show()
