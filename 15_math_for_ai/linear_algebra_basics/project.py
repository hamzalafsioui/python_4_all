"""
PROJECT: Multi-Featured AI Math Engine

This project demonstrates how core Linear Algebra operations power two essential 
components of modern AI:
1. A Content-Based Movie Recommendation Engine (using vector Cosine Similarity).
2. A Neural Network Layer Forward Pass Propagator (using matrix-vector multiplication).

"""

import numpy as np

# =====================================================================
# MODULE 1: Content-Based Movie Recommendation Engine
# =====================================================================

# Movie Database in 5D Genre Space:
# Vector components represent: [Action, Sci-Fi, Comedy, Drama, Romance]
# Scores range from 1.0 (none) to 5.0 (extreme)
MOVIE_DATABASE = {
    "The Matrix": np.array([5.0, 5.0, 1.0, 2.0, 1.0]),
    "Die Hard": np.array([5.0, 1.0, 2.0, 1.0, 1.0]),
    "Superbad": np.array([1.0, 1.0, 5.0, 1.0, 2.0]),
    "La La Land": np.array([1.0, 1.0, 4.0, 3.0, 5.0]),
    "Interstellar": np.array([3.0, 5.0, 1.0, 5.0, 2.0]),
    "The Notebook": np.array([1.0, 1.0, 2.0, 4.0, 5.0])
}

def cosine_similarity(u, v):
    """
    Calculates cosine similarity between two vectors.
    """
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    
    # Avoid division by zero
    if norm_u == 0 or norm_v == 0:
        return 0.0
        
    return dot_product / (norm_u * norm_v)

def get_movie_recommendations(user_profile, movie_db, top_n=2):
    """
    Calculates similarity between user preferences and all movies,
    returning the top recommended movies.
    """
    print("\nCalculating User-to-Movie Cosine Similarities:")
    print("-" * 50)
    
    similarities = []
    
    for movie_name, movie_vector in movie_db.items():
        sim_score = cosine_similarity(user_profile, movie_vector)
        print(f"  {movie_name:<15} | Cosine Similarity: {sim_score:.4f}")
        similarities.append((movie_name, sim_score))
        
    # Sort by similarity score in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities[:top_n]


# =====================================================================
# MODULE 2: Neural Network Layer Forward Pass
# =====================================================================

def sigmoid(z):
    """
    Applies the mathematical sigmoid activation function element-wise.
    Formula: 1 / (1 + e^-z)
    """
    return 1.0 / (1.0 + np.exp(-z))

def neural_forward_pass(x, W, b):
    """
    Performs the feedforward propagation for a single neural network layer.
    Formula: z = W @ x + b
             a = sigmoid(z)
    """
    print("\n--- Running Neural Network Forward Pass ---")
    print(f"Input Vector x (Shape {x.shape}):\n{x}")
    print(f"Weights Matrix W (Shape {W.shape}):\n{W}")
    print(f"Bias Vector b (Shape {b.shape}):\n{b}")
    
    # 1. Linear combination: z = W @ x + b
    # Dimension checking: (2, 3) @ (3, 1) -> (2, 1) + (2, 1) -> (2, 1)
    z = (W @ x) + b
    print(f"\nLinear Combination (z = W @ x + b, Shape {z.shape}):\n{z}")
    
    # 2. Non-linear Activation Function: a = sigmoid(z)
    a = sigmoid(z)
    print(f"Activated Output / Probabilities (a = sigmoid(z), Shape {a.shape}):\n{a}")
    
    return z, a


# =====================================================================
# MAIN ENGINE EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("AI MATH ENGINE: RECOMMENDATION & NEURAL PASS PIPELINE")
    print("=" * 60)
    
    # --- Part 1: Content Recommendation Engine ---
    # User Profile: loves Sci-Fi (5) & Action (4), moderate Drama (3), dislikes Romance (1) & Comedy (1)
    user_preferences = np.array([4.0, 5.0, 1.0, 3.0, 1.0])
    print(f"User Taste Profile Vector: {user_preferences}")
    
    recommendations = get_movie_recommendations(user_preferences, MOVIE_DATABASE, top_n=2)
    
    print("\nRECOMMENDED MOVIES FOR YOU:")
    print("-" * 50)
    for rank, (movie, score) in enumerate(recommendations, 1):
        print(f"  {rank}. {movie} (Match Score: {score*100:.1f}%)")
    print("=" * 60)
    
    # --- Part 2: Neural Network Layer ---
    # Suppose we have a 3D input vector (e.g., house square footage, bedrooms, age)
    # and we want to predict 2 classes (e.g. probability of selling fast vs. slow)
    input_x = np.array([[1.5], 
                        [-0.8], 
                        [2.2]]) # Shape: (3, 1) - Column Vector
                        
    # Layer weights (2 output classes, 3 input features)
    weights_W = np.array([[0.5, -0.2, 0.8], 
                          [-0.4, 0.6, 0.1]]) # Shape: (2, 3)
                          
    # Biases for the 2 output neurons
    bias_b = np.array([[0.25], 
                       [-0.5]]) # Shape: (2, 1) - Column Vector
                       
    z_linear, a_activated = neural_forward_pass(input_x, weights_W, bias_b)
    
    # Output class interpretation
    classes = ["Will Sell Fast", "Will Sell Slow"]
    fast_prob = a_activated[0, 0]
    slow_prob = a_activated[1, 0]
    
    print("\nNeural Network Final Classification Output:")
    print("-" * 50)
    print(f"  Probability '{classes[0]}': {fast_prob*100:.2f}%")
    print(f"  Probability '{classes[1]}': {slow_prob*100:.2f}%")
    
    predicted_class = classes[np.argmax(a_activated)]
    print(f"\n  Final Prediction: {predicted_class}")
    print("=" * 60)
    print("AI Math Engine completed successfully!")
