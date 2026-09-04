# Import necessary libraries
from sklearn.cluster import DBSCAN
import numpy as np
# Sample data(eg points in 2D space)
X = np.array([[1,2],[2,2],[2,3],[8,7],[8,8],[25,80]])
# Initialise amd fit the model
dbscan = DBSCAN(eps=3,min_samples=2)
dbscan.fit(X)
# Get the labesls(-1 indicates noise)
labels = dbscan.labels_
print("Lables: ",labels)