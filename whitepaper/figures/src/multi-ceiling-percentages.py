import numpy as np
import matplotlib.pyplot as plt

T0 = 1  # Assuming initial tokens issued per ETH is 1
days = 50

rates = [0.01, 0.05, 0.10, 0.25] # different price ceiling increase percentages (1%, 5%, 10%, 25%)
colors = ['blue', 'green', 'orange', 'red']
labels = ['1% price ceiling increase percentage', '5% price ceiling increase percentage', '10% price ceiling increase percentage', '25% price ceiling increase percentage']

x = np.linspace(1, days, 1000)

plt.figure(figsize=(10, 8))

for rate, color, label in zip(rates, colors, labels):
    Tn = T0 * (1 - rate)**np.floor(x - 1)
    plt.step(x, Tn, where='post', color=color, label=label)

plt.title(f"Tokens Issued per ETH Over {days} Days for Different Price Ceiling Curves", fontsize=20)
plt.xlabel("Day (t/f)", fontsize=16)
plt.ylabel("Tokens Issued per ETH ($T_t$)", fontsize=16)
plt.grid(True)
plt.xticks(np.arange(1, days + 1, 5), fontsize=14)
plt.yticks(fontsize=14)
plt.legend(loc='upper right', fontsize=16)
plt.tight_layout()
plt.show()

