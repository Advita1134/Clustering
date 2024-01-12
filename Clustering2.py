# -*- coding: utf-8 -*-
'''
- Create a list of numbers.
- Find the minimum and maximum of the numbers.
- Create an empty list.
- Add either 0 or 1 to the empty list depending on if the number is closer to the min or max.

'''


import matplotlib.pyplot as plt

X = [1,3,5.5,10]
#X = [3,4,1,6,10,5,2]
#X = [-1,-2,-3,100]
y = [] # Empty list that will hold 0 or 1 depending which group/cluster the number is in.

# Finding the minimum and maximum number of the list.
min_x = min(X)
max_x = max(X)

# Finding if the number is closer to the min or max.
for x in X:
    distance_from_min = x - min_x
    distance_from_max = max_x - x
    
    if distance_from_min > distance_from_max:
        y.append(0)
        
    else:
        y.append(1)
        
# Creates a plot to show the two different clusters with different colors.        
plt.scatter(X,[0]*len(X),c=y, cmap = "cool")
plt.colorbar()
#plt.grid()
plt.yticks([],labels = [])
plt.tight_layout()
plt.savefig("Clustering.png")
