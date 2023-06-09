import matplotlib.pyplot as plt
import numpy as np
t= np.linspace(-1, 5, 300)
ft= t*np.exp(-2*t)
plt.plot(t, ft, linewidth=3, color='r', marker='o')
plt.title('$F(t)= t.exp^{-2t}$')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.show()