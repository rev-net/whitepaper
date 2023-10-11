import numpy as np
import matplotlib.pyplot as plt

for mean, variance in [(0, 0.5), (0, 1), (1, 0.5), (1, 1)]:
    sample = np.random.lognormal(mean, np.sqrt(variance), 1000)
    plt.hist(sample, bins=100, alpha=0.5, label=f'mean={mean}, variance={variance}')

plt.legend()
plt.show()
