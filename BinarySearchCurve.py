import matplotlib.pyplot as plt
import numpy as np

# Define the range of n values to plot
n = np.arange(1, 10000, 100)

# Calculate the time complexity for each case
best_case = np.ones_like(n)
average_case = np.log(n)
worst_case = np.log(n)

# Plot the curves
plt.plot(n, best_case, label='Best case: O(1)')
plt.plot(n, average_case, label='Average case: O(log n)')
plt.plot(n, worst_case, label='Worst case: O(log n)')

# Add labels and legend
plt.xlabel('n')
plt.ylabel('Time complexity')
plt.legend()

# Show the plot
plt.show()
