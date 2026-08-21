"""
EXERCISES: Vectors, Matrices, and NumPy Mechanics

This script contains 3 practical exercises on broadcasting, vectorization, and matrix math.
Complete the TODO sections or review the provided implementations.
"""

import numpy as np

# =====================================================================
# EXERCISE 1: Standardizing Data (Broadcasting)
# =====================================================================
# In Machine Learning, we often need to "standardize" our features so they have a 
# mean of 0 and a standard deviation of 1.
# Formula: standardized_data = (data - mean) / standard_deviation

# Let's say we have a dataset of 4 houses (rows) with 2 features (columns):
# Feature 1: Square Footage, Feature 2: Age in years
house_data = np.array([
    [2000, 10],
    [1500, 5],
    [3000, 20],
    [2500, 15]
])

def standardize_features(data):
    """
    Standardizes each feature (column) of the dataset using broadcasting.
    """
    # TODO 1: Calculate the mean of each column. 
    # Hint: use np.mean with axis=0. The shape should be (2,)
    feature_means = np.mean(data, axis=0)
    
    # TODO 2: Calculate the standard deviation of each column. (axis=0)
    feature_stds = np.std(data, axis=0)
    
    # TODO 3: Standardize the data. 
    # NumPy will broadcast the 1D arrays (means and stds) across the 2D data array!
    standardized = (data - feature_means) / feature_stds
    
    return standardized, feature_means, feature_stds

print("=== Exercise 1: Data Standardization ===")
std_data, means, stds = standardize_features(house_data)

print(f"Original Data:\n{house_data}")
print(f"\nFeature Means: {means}")
print(f"Feature Stds:  {stds}")
print(f"\nStandardized Data (Notice how values are scaled around 0):\n{std_data}")
print("-" * 50)


# =====================================================================
# EXERCISE 2: The ReLU Activation Function (Vectorization)
# =====================================================================
# The most common activation function in Neural Networks is ReLU (Rectified Linear Unit).
# It simply replaces all negative numbers with 0, and keeps positive numbers as they are.
# You must do this WITHOUT any 'for' loops!

hidden_layer_outputs = np.array([
    [-1.5, 2.0, -0.5],
    [ 3.1, -2.2, 0.0],
    [ 0.5,  1.1, -1.9]
])

def relu_activation(matrix):
    """
    Applies the ReLU activation function using vectorized NumPy operations.
    """
    # TODO: Implement ReLU. 
    # Hint: np.maximum(array, 0) compares every element to 0 and keeps the max.
    activated = np.maximum(matrix, 0)
    return activated

print("\n=== Exercise 2: ReLU Activation ===")
relu_result = relu_activation(hidden_layer_outputs)

print(f"Pre-activation Outputs:\n{hidden_layer_outputs}")
print(f"\nPost-activation (ReLU) Outputs:\n{relu_result}")
print("-" * 50)


# =====================================================================
# EXERCISE 3: The Linear Layer (Matrix Multiplication)
# =====================================================================
# Compute the output of a single linear layer in a neural network: Y = X @ W
# X is the input data (batch of 3 samples, 4 features each).
# W is the weight matrix mapping 4 features to 2 output neurons.

X_inputs = np.array([
    [1.0, 0.5, 0.2, 0.1],
    [0.9, 0.6, 0.3, 0.0],
    [0.8, 0.4, 0.1, 0.2]
]) # Shape: (3, 4)

W_weights = np.array([
    [0.2, -0.1],
    [0.5,  0.8],
    [-0.3, 0.2],
    [0.1,  0.4]
]) # Shape: (4, 2)

print("\n=== Exercise 3: Linear Layer Output ===")

# TODO: Perform matrix multiplication between X and W to get the predictions Y.
# The resulting shape should be (3, 2).
Y_predictions = X_inputs @ W_weights

print(f"Input Matrix X shape: {X_inputs.shape}")
print(f"Weights Matrix W shape: {W_weights.shape}")
print(f"\nPredictions Matrix Y (X @ W):\n{Y_predictions}")
print(f"Predictions Shape: {Y_predictions.shape}")
print("=" * 60)

if __name__ == "__main__":
    print("\nAll NumPy Vector and Matrix exercises completed successfully!")
