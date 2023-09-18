import numpy as np
import matplotlib.pyplot as plt

T0 = 1  # Assuming initial tokens issued per ETH is 1
generations = 50

rates = [0.01, 0.05, 0.10, 0.25] # different entry curves (1%, 5%, 10%, 25%)
colors = ['blue', 'green', 'orange', 'red']
labels = ['1% entry curve', '5% entry curve', '10% entry curve', '25% entry curve']

x = np.linspace(1, generations, 1000)

plt.figure(figsize=(10, 8))

for rate, color, label in zip(rates, colors, labels):
    Tn = T0 * (1 - rate)**np.floor(x - 1)
    plt.step(x, Tn, where='post', color=color, label=label)

plt.title(f"Tokens Issued per ETH Over {generations} Generations for Different Entry Curves", fontsize=20)
plt.xlabel("Generation Number (n)", fontsize=16)
plt.ylabel("Tokens Issued per ETH ($T_n$)", fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1, generations + 1, 5), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(loc='upper right', fontsize=16)
plt.tight_layout()
plt.show()

