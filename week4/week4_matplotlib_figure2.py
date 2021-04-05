import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2*np.pi * x1) * np.exp(-x1)
y2 = np.cos(2*np.pi * x2)


axes1 = plt.subplot(2,1,1)
plt.plot(x1,y1, marker='o')
plt.title("subplot1 : y1")
plt.grid(True)

axes2 = plt.subplot(2,1,2)
plt.plot(x2, y2, marker='*')
plt.title("subplot2:y2")
plt.grid(True)

plt.tight_layout() # 그래프를 타이트하게 이쁘게 그려달라는 메소드

plt.show()