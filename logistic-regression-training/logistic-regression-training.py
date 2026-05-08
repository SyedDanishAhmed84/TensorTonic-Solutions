import numpy as np

def _sigmoid(z):
    # Numerically stable sigmoid
    z = np.clip(z, -500, 500)
    return 1 / (1 + np.exp(-z))

def train_logistic_regression(X, y, lr=0.1, steps=500):
    # Convert inputs to NumPy arrays
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    # Number of samples (N) and features (D)
    N, D = X.shape

    # Initialize parameters
    w = np.zeros(D)
    b = 0.0

    # Gradient Descent Training Loop
    for _ in range(steps):

        # Linear combination
        z = np.dot(X, w) + b

        # Predicted probabilities
        p = _sigmoid(z)

        # Compute gradients
        dw = (1 / N) * np.dot(X.T, (p - y))
        db = (1 / N) * np.sum(p - y)

        # Update parameters
        w -= lr * dw
        b -= lr * db

    return w, b