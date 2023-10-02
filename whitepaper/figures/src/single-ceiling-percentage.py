import numpy as np
import matplotlib.pyplot as plt

# Given parameters
T0 = 1  # Assuming initial tokens issued per ETH is 1
r = 0.05  # 5% entry curve
days = 50

# Generation numbers
x = np.linspace(1, days, 1000)

# Calculate number of tokens issued per ETH in the nth generation
Tn = T0 * (1 - r)**np.floor(x - 1)

# Plotting the graph
plt.figure(figsize=(10, 8))
plt.step(x, Tn, where='post', color='blue')
plt.title(f"Tokens Issued per ETH Over {days} Days With a {int(r*100)}% Price Ceiling Increase Percentage", fontsize=20)
plt.xlabel("Day (t/f)", fontsize=18)
plt.ylabel("Tokens Issued per ETH ($T_t$)", fontsize=18)
plt.grid(True)
plt.xticks(np.arange(1, days + 1, 5), fontsize=14)
plt.yticks(fontsize=14)
plt.tight_layout()
plt.show()
