import matplotlib.pyplot as plt
import numpy as np

x = [10,20,30,40]
y = [1,4,9,16]

plt.plot(x,y, color = 'red', marker='o', ls='--', mew=5, mec='green', mfc='yellow') #수정해보면서 비교
plt.xlim(0,50) #수정해보면서 비교
plt.ylim(-10,30) #수정해보면서 비교
plt.show()