import numpy as np
import matplotlib.pyplot as plt

# Constants
V_t = 100  # total ETH
s = 100   # total token supply
r_ex_vals = [0.0, 0.33, 0.66, 1.0] # exit curve values
colors = ['blue', 'green', 'orange', 'red']

# Function for the exit curve
def exit_curve(x, r_ex):
    return (V_t * x / s) * ((1 - r_ex) + (r_ex * x / s))

# Values for plotting
x_values = np.linspace(0, s, 1000)

# Plotting
plt.figure(figsize=(10, 8))
for r, color in zip(r_ex_vals, colors):
    plt.plot(x_values, exit_curve(x_values, r), label=f"{int(r*100)}% exit curve", color=color)

plt.title(f"ETH Reclaimed by Burning Tokens With Different Exit Curves", fontsize=20)
plt.xlabel("Percent of Tokens Burned", fontsize=18)
plt.ylabel("Percent of ETH Reclaimed", fontsize=18)
plt.grid(True)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

