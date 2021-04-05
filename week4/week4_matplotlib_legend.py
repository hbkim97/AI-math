import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256)
c = np.cos(x)
s = np.sin(x)

plt.title("my COS and SIN graph")
plt.plot(x, c, ls='--', label='cosine')
plt.plot(x, s, ls='--', label='sine')
plt.grid(True)
plt.legend(loc=0) #범례 0:자동으로 좋은 위치 / 2:왼쪽 위 
plt.show()