# Not used in final paper. Included for reference.
import numpy as np
import matplotlib.pyplot as plt

# Constants
V_t = 100  # total ETH
s = 100   # total supply of tokens
r_ex = 0.50 # exit curve

# Function for the exit curve
def exit_curve(x, r_ex):
    return (V_t * x / s) * ((1 - r_ex) + (r_ex * x / s))

# Values for plotting
x_values = np.linspace(0, s, 1000)
y_values = exit_curve(x_values, r_ex)

# Plotting
plt.figure(figsize=(10, 8))
plt.plot(x_values, y_values, label="Exit Curve = 50%", color="blue")
plt.title(f"ETH Reclaimed by Burning Tokens With a {int(r_ex * 100)}% Exit Curve", fontsize=20)
plt.xlabel("Percent of Tokens Burned", fontsize=18)
plt.ylabel("Percent of ETH Reclaimed", fontsize=18)
plt.grid(True)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

