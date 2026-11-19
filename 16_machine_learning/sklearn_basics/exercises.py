"""
EXERCISES: The Sklearn Apprentice

This script contains 3 practical exercises on scikit-learn basics.
Complete the TODO sections to solve them.
"""

import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# =====================================================================
# EXERCISE 1: Dataset Explorer
# =====================================================================
# The Wine dataset contains chemical analysis results of wines from
# 3 different cultivars (grape varieties) grown in Italy.
# Your job: Load it, inspect it, split it properly, and verify
# that stratification preserves class balance.

print("=== Exercise 1: Dataset Explorer ===")

# TODO 1: Load the Wine dataset
wine = load_wine()
X, y = wine.data, wine.target

# TODO 2: Print the number of samples, features, and class names
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")
print(f"Feature names: {wine.feature_names}")
print(f"Class names: {wine.target_names}")

# TODO 3: Print the class distribution (how many samples per class)
unique, counts = np.unique(y, return_counts=True)
print(f"\nClass distribution in full dataset:")
for cls_idx, count in zip(unique, counts):
    print(f"  {wine.target_names[cls_idx]}: {count} ({count/len(y)*100:.1f}%)")

# TODO 4: Split into train (75%) and test (25%) with stratification
#          Use random_state=42
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print(f"\nAfter split:")
print(f"  Train: {X_train.shape[0]} samples")
print(f"  Test:  {X_test.shape[0]} samples")

# TODO 5: Verify stratification by printing class ratios for both sets
print(f"\nStratification verification:")
for name, subset in [("Train", y_train), ("Test", y_test)]:
    _, sub_counts = np.unique(subset, return_counts=True)
    ratios = sub_counts / len(subset) * 100
    print(f"  {name}: {[f'{r:.1f}%' for r in ratios]}")

print("-" * 60)


# =====================================================================
# EXERCISE 2: Scaling Showdown
# =====================================================================
# Many beginners skip feature scaling or do it incorrectly.
# Your job: Prove that scaling matters by comparing KNN accuracy
# with and without scaling, AND show the data leakage mistake.

print("\n=== Exercise 2: Scaling Showdown ===")

# We already have X_train, X_test, y_train, y_test from Exercise 1

# --- Part A: No Scaling ---
# TODO 1: Train KNN (k=5) on raw (unscaled) data and get test accuracy
knn_raw = KNeighborsClassifier(n_neighbors=5)
knn_raw.fit(X_train, y_train)
acc_raw = knn_raw.score(X_test, y_test)
print(f"Accuracy WITHOUT scaling: {acc_raw:.2%}")

# --- Part B: Correct Scaling ---
# TODO 2: Use StandardScaler — fit on train, transform both
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit + transform on TRAIN
X_test_scaled = scaler.transform(X_test)         # ONLY transform on TEST

knn_scaled = KNeighborsClassifier(n_neighbors=5)
knn_scaled.fit(X_train_scaled, y_train)
acc_scaled = knn_scaled.score(X_test_scaled, y_test)
print(f"Accuracy WITH correct scaling: {acc_scaled:.2%}")

# --- Part C: Data Leakage (THE WRONG WAY) ---
# TODO 3: Show the WRONG way — fit_transform on ALL data before splitting
#          This causes data leakage because the scaler sees test data
leaky_scaler = StandardScaler()
X_all_scaled = leaky_scaler.fit_transform(X)  # WRONG: sees ALL data including test
X_train_leaky = X_all_scaled[:len(X_train)]
X_test_leaky = X_all_scaled[len(X_train):]

knn_leaky = KNeighborsClassifier(n_neighbors=5)
knn_leaky.fit(X_train_leaky, y_train)
acc_leaky = knn_leaky.score(X_test_leaky, y_test)
print(f"Accuracy WITH data leakage:    {acc_leaky:.2%}")

# TODO 4: Print the comparison and explain
print(f"\n--- Comparison ---")
print(f"  No scaling:      {acc_raw:.2%}")
print(f"  Correct scaling: {acc_scaled:.2%}")
print(f"  Leaky scaling:   {acc_leaky:.2%}")
print(f"\n  Scaling improves accuracy because KNN relies on distances.")
print(f"  The leaky version may appear similar but uses illegal info from")
print(f"  the test set — in production, this gives falsely optimistic results.")

print("-" * 60)


# =====================================================================
# EXERCISE 3: Pipeline Builder
# =====================================================================
# Build a proper Pipeline, evaluate it with cross-validation,
# and compare different hyperparameters.

print("\n=== Exercise 3: Pipeline Builder ===")

# TODO 1: Build a Pipeline with StandardScaler → KNeighborsClassifier(k=5)
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=5))
])

# TODO 2: Cross-validate the pipeline with 5-fold CV on the TRAINING set
cv_scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy')
print(f"Pipeline 5-Fold CV Scores: {cv_scores.round(4)}")
print(f"Pipeline Mean Accuracy: {cv_scores.mean():.2%} ± {cv_scores.std():.2%}")

# TODO 3: Train the pipeline on full training set and evaluate on test set
pipe.fit(X_train, y_train)
test_accuracy = pipe.score(X_test, y_test)
print(f"\nPipeline Test Accuracy: {test_accuracy:.2%}")

# TODO 4: Print the full classification report
y_pred = pipe.predict(X_test)
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# TODO 5: Compare pipelines with different K values using cross-validation
print("Comparing different K values via Pipeline + CV:")
print(f"  {'K':>3}  {'Mean CV Accuracy':>18}  {'Std':>8}")
print(f"  {'---':>3}  {'-'*18:>18}  {'---':>8}")

best_k = 1
best_score = 0

for k in [1, 3, 5, 7, 9, 11, 15, 21]:
    test_pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', KNeighborsClassifier(n_neighbors=k))
    ])
    scores = cross_val_score(test_pipe, X_train, y_train, cv=5, scoring='accuracy')
    mean_score = scores.mean()
    print(f"  {k:>3}  {mean_score:>18.2%}  {scores.std():>8.2%}")
    
    if mean_score > best_score:
        best_score = mean_score
        best_k = k

print(f"\n  Best K = {best_k} with CV accuracy = {best_score:.2%}")

# TODO 6: Train the best pipeline and get final test score
final_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', KNeighborsClassifier(n_neighbors=best_k))
])
final_pipe.fit(X_train, y_train)
final_score = final_pipe.score(X_test, y_test)
print(f"  Final Test Accuracy with K={best_k}: {final_score:.2%}")

print("=" * 60)

if __name__ == "__main__":
    print("\nAll sklearn basics exercises completed successfully!")
