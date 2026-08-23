# 15_math_for_ai

## What Will I Learn?
This module covers the core mathematical foundations essential for AI and Machine Learning:
- **Linear Algebra**: Vectors, vector operations, dot product, norms, cosine similarity, matrices, determinants, matrix inverse, and linear solvers.
- **Probability & Statistics**: Descriptive statistics (mean, median, std dev, IQR, percentiles), conditional probability, Bayes' Theorem, Gaussian/Normal distributions, Z-scores, and the Central Limit Theorem (CLT).
- **Vectors, Matrices & NumPy**: Efficient numerical computation, array memory layout, vectorization vs loops, scalar/vector broadcasting, and Markov chain probabilistic modeling.

## Why Is It Important?
Mathematics is the engine under the hood of Artificial Intelligence. Modern ML algorithms store data in vectors and matrices, compute feature interactions via linear algebra, model uncertainty using probability, and optimize parameters through high-performance vectorized array operations.

## Prerequisites
- `14_data_science_basics`

## Estimated Time
10–15 hours

## Learning Objectives
By the end of this module, you will be able to:
- Perform vector and matrix operations fluently using NumPy.
- Calculate and interpret Cosine Similarity for recommendation engines and text embeddings.
- Implement feedforward propagation for neural network layers from linear algebra principles.
- Apply Bayes' Theorem to build Naive Bayes text classification models from scratch.
- Monitor and flag system anomalies using Gaussian statistics and Z-scores.
- Harness vectorization and broadcasting for high-performance numerical computation.
- Model multi-state dynamical systems using Markov chain transition matrices.

## Files in This Module
- `README.md` | This file
- `requirements.txt` | Dependencies for this module
- `linear_algebra_basics/` | Vectors, dot products, norms, matrices, inverse, solvers, and neural forward pass
  - `README.md` / `theory.md` | Concepts and explanations
  - `examples.py` | Runnable code demonstrations
  - `exercises.py` | Practice problems with solutions
  - `project.py` | Movie recommendation engine & neural layer pass
  - `notebook.ipynb` | Interactive visual exploration notebook
- `probability_statistics/` | Descriptive stats, Bayes theorem, normal distribution, Z-scores, and CLT
  - `README.md` / `theory.md` | Concepts and explanations
  - `examples.py` | Runnable code demonstrations
  - `exercises.py` | Practice problems with solutions
  - `project.py` | Naive Bayes classifier & server anomaly detector
  - `notebook.ipynb` | Interactive visual exploration notebook
- `vectors_matrices_numpy/` | Array creation, vectorization, broadcasting, and Markov chains
  - `README.md` / `theory.md` | Concepts and explanations
  - `examples.py` | Runnable code demonstrations
  - `exercises.py` | Practice problems with solutions
  - `project.py` | E-commerce customer Markov chain simulator
  - `notebook.ipynb` | Interactive visual exploration notebook
