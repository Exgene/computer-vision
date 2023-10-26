import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate some sample data for clustering
np.random.seed(0)

x = np.random.rand(100, 2)
# No of clusters
k = 3

# Initialize the k means model
kmeans = KMeans(n_clusters=k)

# FIt the model
kmeans.fit(x)

# Get the clusters center and labels
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Plot the data points and cluster centers
plt.scatter(x[:, 0], x[:, 1], c=labels)

plt.scatter(cluster_centers[:, 0], cluster_centers[:,
            1], marker='x', s=200, color='red')
plt.title(f"K Means Clustering(k={k})")

# Shows the plotted graph
plt.show()
