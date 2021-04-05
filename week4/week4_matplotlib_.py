import numpy as np
import matplotlib.pyplot as plt

# -3.14 ~ 3.14 까지 256개의 값으로 표시해라.
x = np.linspace(-np.pi, np.pi, 256, endpoint=True) #256개 값
print(x.shape)

c = np.cos(x) # 256개 값
s = np.sin(x) # 256개 값

plt.plot(x, c)
plt.plot(x, s)
plt.show() 