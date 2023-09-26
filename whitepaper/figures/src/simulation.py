import matplotlib.pyplot as plt
import numpy as np

# Define the parameters
generations = np.arange(1, 51)
r_c = 0.05  # price ceiling curve
r_f = 0.33  # price floor curve
T_1 = 1  # initial price

# Calculate the price ceiling and floor over time
price_ceiling = T_1 * (1 - r_c) ** (generations - 1)
price_floor = T_1 * (1 - r_f) ** (generations - 1)

# Simulate the token price fluctuating between the price ceiling and floor
np.random.seed(0)
token_price = np.random.uniform(price_floor, price_ceiling)

# Plot the price ceiling, floor, and token price over time
plt.figure(figsize=(10, 6))
plt.plot(generations, price_ceiling, label='Price Ceiling')
plt.plot(generations, price_floor, label='Price Floor')
plt.plot(generations, token_price, label='Token Price', linestyle='--')
plt.xlabel('Generation')
plt.ylabel('Price')
plt.title('Price Ceiling, Floor, and Token Price Over Time')
plt.legend()
plt.grid(True)
plt.show()