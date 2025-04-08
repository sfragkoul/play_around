
import numpy as np

# Create a 2D NumPy array
data = np.random.randint(0, 100, size=(5, 4))  # 5 rows, 4 columns
print("Array:\n", data)


# Basic statistics
mean_val = np.mean(data)
max_val = np.max(data)
col_sums = np.sum(data, axis=0)

print("Mean:", mean_val)
print("Max:", max_val)
print("Column sums:", col_sums)


# Accessing rows and columns
first_row = data[0, :]
second_col = data[:, 1]

print("First row:", first_row)
print("Second column:", second_col)
