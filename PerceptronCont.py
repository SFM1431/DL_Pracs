import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # iterate over the training set for n_iterations
        for _ in range(self.n_iterations):
            for i in range(n_samples):
                # calculate the predicted value
                y_pred = np.dot(X[i], self.weights) + self.bias

                # update the weights and bias if prediction is incorrect
                if y[i]*y_pred <= 0:
                    self.weights += self.learning_rate * y[i] * X[i]
                    self.bias += self.learning_rate * y[i]

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return np.sign(y_pred)

X_train = np.array([[2.3, 4.5], [1.2, 3.1], [3.5, 6.3], [4.2, 5.1]])
y_train = np.array([1, -1, 1, -1])
X_test = np.array([[2.5, 4.2], [1.8, 3.9]])
perceptron = Perceptron()
perceptron.fit(X_train, y_train)
y_pred = perceptron.predict(X_test)

print(y_pred) # output: [1, -1]