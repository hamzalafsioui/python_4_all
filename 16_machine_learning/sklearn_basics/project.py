"""
PROJECT: Flower Species Classifier — End-to-End ML Pipeline

This project demonstrates a complete machine learning workflow using
scikit-learn, from data loading to model comparison. It builds a flower
species classifier on the Iris dataset using best practices:
  1. Data exploration and understanding
  2. Proper train/test splitting with stratification
  3. Feature scaling inside a Pipeline (no data leakage)
  4. Model training and evaluation
  5. Cross-validation for reliable assessment
  6. Hyperparameter comparison to find the best K
  7. Final evaluation with confusion matrix and classification report
  8. Prediction on new unseen data
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report
)


# =====================================================================
# STAGE 1: Data Exploration
# =====================================================================

def explore_dataset():
    """Load and thoroughly explore the Iris dataset."""
    print("=" * 60)
    print("STAGE 1: DATA EXPLORATION")
    print("=" * 60)
    
    iris = load_iris()
    X, y = iris.data, iris.target
    
    print(f"\nDataset: {iris.DESCR[:200]}...\n")
    print(f"Shape: {X.shape[0]} samples × {X.shape[1]} features")
    print(f"Features: {iris.feature_names}")
    print(f"Classes:  {list(iris.target_names)}")
    
    # Statistics per feature
    print(f"\nFeature Statistics:")
    print(f"  {'Feature':<20} {'Min':>8} {'Max':>8} {'Mean':>8} {'Std':>8}")
    print(f"  {'-'*20:<20} {'-'*8:>8} {'-'*8:>8} {'-'*8:>8} {'-'*8:>8}")
    for i, name in enumerate(iris.feature_names):
        col = X[:, i]
        print(f"  {name:<20} {col.min():>8.2f} {col.max():>8.2f} "
              f"{col.mean():>8.2f} {col.std():>8.2f}")
    
    # Class balance
    unique, counts = np.unique(y, return_counts=True)
    print(f"\nClass Balance:")
    for cls_idx, count in zip(unique, counts):
        bar = "█" * (count // 3)
        print(f"  {iris.target_names[cls_idx]:<12} {count:>3} samples  {bar}")
    
    balanced = len(set(counts)) == 1
    print(f"  → Dataset is {'BALANCED ✓' if balanced else 'IMBALANCED ⚠️'}")
    
    return iris, X, y


# =====================================================================
# STAGE 2: Data Splitting
# =====================================================================

def split_data(X, y):
    """Split data with stratification and verify the split."""
    print(f"\n{'=' * 60}")
    print("STAGE 2: TRAIN/TEST SPLIT")
    print("=" * 60)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    
    print(f"\nSplit ratio: 80% train / 20% test")
    print(f"Training set: {X_train.shape[0]} samples")
    print(f"Test set:     {X_test.shape[0]} samples")
    
    # Verify stratification
    print(f"\nStratification check:")
    for name, subset in [("Full", y), ("Train", y_train), ("Test", y_test)]:
        _, counts = np.unique(subset, return_counts=True)
        pcts = counts / len(subset) * 100
        print(f"  {name:<6}: " + " | ".join(f"{p:.1f}%" for p in pcts))
    
    return X_train, X_test, y_train, y_test


# =====================================================================
# STAGE 3: Pipeline Construction
# =====================================================================

def build_pipeline(n_neighbors=5):
    """Build a Pipeline with StandardScaler → KNN."""
    return Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', KNeighborsClassifier(n_neighbors=n_neighbors))
    ])


# =====================================================================
# STAGE 4: Hyperparameter Search — Find the Best K
# =====================================================================

def find_best_k(X_train, y_train):
    """Compare different K values using cross-validation."""
    print(f"\n{'=' * 60}")
    print("STAGE 3: HYPERPARAMETER COMPARISON (Finding Best K)")
    print("=" * 60)
    
    k_values = [1, 3, 5, 7, 9, 11, 13, 15, 21]
    results = []
    
    print(f"\n  {'K':>3}  {'Mean CV Acc':>12}  {'Std':>8}  {'Visual':>20}")
    print(f"  {'─'*3}  {'─'*12}  {'─'*8}  {'─'*20}")
    
    for k in k_values:
        pipe = build_pipeline(n_neighbors=k)
        scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy')
        mean_score = scores.mean()
        std_score = scores.std()
        results.append((k, mean_score, std_score))
        
        bar_len = int(mean_score * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {k:>3}  {mean_score:>12.2%}  {std_score:>8.2%}  {bar}")
    
    # Find the best K
    best_k, best_score, best_std = max(results, key=lambda x: x[1])
    print(f"\n  ★ Best K = {best_k} → {best_score:.2%} ± {best_std:.2%}")
    
    return best_k, best_score


# =====================================================================
# STAGE 5: Final Training and Evaluation
# =====================================================================

def train_and_evaluate(X_train, X_test, y_train, y_test, best_k, iris):
    """Train the final model and produce a full evaluation."""
    print(f"\n{'=' * 60}")
    print(f"STAGE 4: FINAL MODEL (K={best_k})")
    print("=" * 60)
    
    # Build and train the final pipeline
    final_pipe = build_pipeline(n_neighbors=best_k)
    final_pipe.fit(X_train, y_train)
    
    # Predictions
    y_pred = final_pipe.predict(X_test)
    
    # Accuracy
    train_acc = final_pipe.score(X_train, y_train)
    test_acc = final_pipe.score(X_test, y_test)
    print(f"\n  Training Accuracy: {train_acc:.2%}")
    print(f"  Test Accuracy:     {test_acc:.2%}")
    
    gap = train_acc - test_acc
    if gap > 0.1:
        print(f"  ⚠️ Gap = {gap:.2%} — possible overfitting")
    else:
        print(f"  ✓ Gap = {gap:.2%} — model generalizes well")
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n  Confusion Matrix:")
    print(f"  {'':>12} " + "  ".join(f"{n:>10}" for n in iris.target_names))
    for i, row in enumerate(cm):
        row_str = "  ".join(f"{v:>10}" for v in row)
        print(f"  {iris.target_names[i]:>12} {row_str}")
    
    # Classification Report
    print(f"\n  Classification Report:")
    report = classification_report(y_test, y_pred, target_names=iris.target_names)
    for line in report.split('\n'):
        print(f"  {line}")
    
    # Per-sample analysis: show any misclassifications
    errors = np.where(y_pred != y_test)[0]
    if len(errors) > 0:
        print(f"\n  Misclassified samples ({len(errors)}):")
        for idx in errors:
            actual = iris.target_names[y_test[idx]]
            predicted = iris.target_names[y_pred[idx]]
            print(f"    Sample {idx}: Actual={actual}, Predicted={predicted}")
    else:
        print(f"\n  ✓ Zero misclassifications! Perfect test accuracy.")
    
    return final_pipe


# =====================================================================
# STAGE 6: Prediction on New Data
# =====================================================================

def predict_new_data(pipe, iris):
    """Use the trained pipeline to classify new flowers."""
    print(f"\n{'=' * 60}")
    print("STAGE 5: PREDICTING NEW FLOWERS")
    print("=" * 60)
    
    # Simulated new flower measurements
    new_flowers = np.array([
        [5.1, 3.5, 1.4, 0.2],   # Typical setosa
        [6.3, 2.8, 5.1, 1.5],   # Typical versicolor  
        [7.2, 3.6, 6.1, 2.5],   # Typical virginica
        [5.8, 2.7, 3.9, 1.2],   # Ambiguous — could be versicolor
        [4.9, 3.1, 1.5, 0.1],   # Another setosa-like
    ])
    
    descriptions = [
        "Small petals, wide sepals",
        "Medium everything",
        "Large petals, long sepals",
        "Ambiguous measurements",
        "Tiny petals, compact flower",
    ]
    
    predictions = pipe.predict(new_flowers)
    
    print(f"\n  {'#':>3}  {'Description':<28} {'Sepal L':>8} {'Sepal W':>8} "
          f"{'Petal L':>8} {'Petal W':>8}  {'→ Predicted':>15}")
    print(f"  {'─'*3}  {'─'*28} {'─'*8} {'─'*8} {'─'*8} {'─'*8}  {'─'*15}")
    
    for i, (flower, pred, desc) in enumerate(zip(new_flowers, predictions, descriptions)):
        species = iris.target_names[pred]
        print(f"  {i+1:>3}  {desc:<28} {flower[0]:>8.1f} {flower[1]:>8.1f} "
              f"{flower[2]:>8.1f} {flower[3]:>8.1f}  → {species:>14}")


# =====================================================================
# MAIN PIPELINE EXECUTION
# =====================================================================

if __name__ == "__main__":
    print("╔" + "═" * 58 + "╗")
    print("║  🌸 FLOWER SPECIES CLASSIFIER — End-to-End ML Pipeline  ║")
    print("╚" + "═" * 58 + "╝")
    
    # Stage 1: Explore
    iris, X, y = explore_dataset()
    
    # Stage 2: Split
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Stage 3: Find best hyperparameter
    best_k, best_cv_score = find_best_k(X_train, y_train)
    
    # Stage 4: Train and evaluate
    final_pipe = train_and_evaluate(X_train, X_test, y_train, y_test, best_k, iris)
    
    # Stage 5: Predict new data
    predict_new_data(final_pipe, iris)
    
    print(f"\n{'=' * 60}")
    print("🏁 PIPELINE COMPLETED SUCCESSFULLY")
    print(f"   Best model: KNN with K={best_k}")
    print(f"   CV Accuracy: {best_cv_score:.2%}")
    print(f"   Ready for production!")
    print("=" * 60)
