nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3]
import numpy as np
import matplotlib.pyplot as plt

np.array(nums)
np.array(bins)
plt.figure(figsize=(10, 8))
plt.hist(nums, bins, color="orange")
plt.ylabel("bins", fontsize=20)
plt.xlabel("nums", fontsize=20)
plt.title("Histogram of nums against bins", fontsize=25)
plt.show()
