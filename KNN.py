import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Generate some sample data for classification
np.random.seed(0)

# Feature Matrix
x = np.random.rand(100, 2)

# Target Vector (Binary Classification)
y = np.random.choice([0, 1], size=100)

# Spilt into training and testing dataset
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=42)

# Create a KNN classifier with k=3
k = 3
knn = KNeighborsClassifier(n_neighbors=k)

# Fit the classifer to the training data
knn.fit(x_train, y_train)

# Make predictions on the test dataset
y_pred = knn.predict(x_test)

# Calculate the accuracy of the classifier
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy = {acc*100:.2f}%")
