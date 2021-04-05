import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256)
c = np.cos(x)

plt.plot(x, c, color='black', ls='--')
plt.title("my graph")
plt.yticks([-1,0,1]) #y축 지정
plt.xticks([-np.pi, -np.pi/2,0, np.pi/2, np.pi]) #x축 지정
plt.grid(True)
plt.show()