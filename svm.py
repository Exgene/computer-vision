import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Create a synthetic dataset for classification
x, y = datasets.make_classification(
    n_samples=500, n_features=6, n_informative=5, n_redundant=0, random_state=42)

# split into training and testing datasets
x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2, random_state=42)

# Create a SVM classifier
svm_clf = SVC(kernel='rbf', C=1.0)

# Train the SVM classifier on the training data
svm_clf.fit(x_train, y_train)

# Make predictions on the test data
y_pred = svm_clf.predict(x_test)

# Display the test score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
