import numpy as np
import matplotlib.pyplot as plt

np.random.seed(11)
x=np.random.randn(100)
f1 = plt.figure(figsize=(20,4))
plt.title("my figure: size (20,4)")
plt.plot(x)
plt.show()