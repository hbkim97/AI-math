import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

np.random.seed(0)
axes[0, 0].plot(np.random.rand(5))
axes[0, 0].set_title("figure1")
axes[0, 1].plot(np.random.rand(5))
axes[0, 1].set_title("figure2")
axes[1, 0].plot(np.random.rand(5))
axes[1, 0].set_title("figure3")
axes[1, 1].plot(np.random.rand(5))
axes[1, 1].set_title("figure4")

plt.tight_layout()

plt.show()