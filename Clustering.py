'''
1D clustering using the biggest gap between the numbers.

- Put the numbers in numerical order.
- Find the distance between the first and second number, then the second and third number, and so on.
- Put the distances in a list.
- Find the index of the largest distance.
- Use that index to find where the group should be split.
- Make a plot using the clusters.
'''
import matplotlib.pyplot as plt
import numpy as np

# Data (Input)
#X = np.array([-8,-9,-10,-15,-16,-17,-18])
#X = np.array([1,2,3,5,6,7])
#X = np.array([3,5,12,2,4,10,17,18,19])
X = np.array([10,5,12,6,3,1,4,2])

X_sorted = sorted(X)
distances = np.array([])

# Find distances between each number
for i in range(len(X)-1):
    d = X_sorted[i+1] - X_sorted[i]
    distances = np.append(distances, d)
    

# Using max distance to make a boundary 
max_index = np.argmax(distances) # Use the list of distances and finds the max distance. 
boundary = X_sorted[max_index] # Use the max distance to make a boundary.
y_estimate = np.where(X<=boundary, 0, 1) # Use the boundary to split the numbers and make the two groups.

# Plotting points depending on clusters
plt.scatter(X,[0]*len(X),c=y_estimate, cmap = "cool")
plt.colorbar()
#plt.grid()
plt.yticks([],labels = [])
plt.tight_layout()
plt.savefig("Clustering.png")
