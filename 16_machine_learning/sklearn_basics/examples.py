# Examples: Scikit-Learn Basics

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report
)
from sklearn.pipeline import Pipeline


def dataset_exploration_demo():
    """Demonstrate how to load and inspect a built-in sklearn dataset."""
    print("--- 1. Dataset Exploration: The Iris Dataset ---")
    
    # Load the Iris dataset
    iris = load_iris()
    
    # What's inside?
    print(f"Keys: {list(iris.keys())}")
    print(f"Feature Matrix (X) shape: {iris.data.shape}")
    print(f"Target Vector (y) shape: {iris.target.shape}")
    print(f"Feature names: {iris.feature_names}")
    print(f"Target names (classes): {iris.target_names}")
    
    # Quick peek at the data
    print(f"\nFirst 5 samples:")
    for i in range(5):
        features = iris.data[i]
        label = iris.target_names[iris.target[i]]
        print(f"  Sample {i}: {features} → {label}")
    
    # Class distribution
    unique, counts = np.unique(iris.target, return_counts=True)
    print(f"\nClass distribution:")
    for cls, count in zip(iris.target_names, counts):
        print(f"  {cls}: {count} samples ({count/len(iris.target)*100:.0f}%)")
    
    print("-" * 60)
    return iris


def train_test_split_demo(iris):
    """Demonstrate splitting data into training and test sets."""
    print("\n--- 2. Train/Test Split ---")
    
    X, y = iris.data, iris.target
    
    # Split: 80% train, 20% test, with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,       # 20% for testing
        random_state=42,     # Reproducible split
        stratify=y           # Keep class ratios equal
    )
    
    print(f"Full dataset:  X={X.shape}, y={y.shape}")
    print(f"Training set:  X={X_train.shape}, y={y_train.shape}")
    print(f"Test set:      X={X_test.shape}, y={y_test.shape}")
    
    # Verify stratification preserved class ratios
    print(f"\nClass distribution check:")
    for name, subset, total in [("Full", y, len(y)), 
                                 ("Train", y_train, len(y_train)),
                                 ("Test", y_test, len(y_test))]:
        _, counts = np.unique(subset, return_counts=True)
        ratios = counts / total * 100
        print(f"  {name:5s}: {[f'{r:.1f}%' for r in ratios]}")
    
    print("-" * 60)
    return X_train, X_test, y_train, y_test


def feature_scaling_demo(X_train, X_test):
    """Demonstrate feature scaling with StandardScaler and MinMaxScaler."""
    print("\n--- 3. Feature Scaling ---")
    
    print("Before scaling:")
    print(f"  X_train mean per feature: {X_train.mean(axis=0).round(2)}")
    print(f"  X_train std per feature:  {X_train.std(axis=0).round(2)}")
    print(f"  X_train range: [{X_train.min():.1f}, {X_train.max():.1f}]")
    
    # --- StandardScaler ---
    std_scaler = StandardScaler()
    X_train_std = std_scaler.fit_transform(X_train)  # fit + transform on train
    X_test_std = std_scaler.transform(X_test)         # ONLY transform on test
    
    print("\nAfter StandardScaler:")
    print(f"  X_train mean per feature: {X_train_std.mean(axis=0).round(4)}")
    print(f"  X_train std per feature:  {X_train_std.std(axis=0).round(4)}")
    
    # --- MinMaxScaler ---
    mm_scaler = MinMaxScaler()
    X_train_mm = mm_scaler.fit_transform(X_train)
    X_test_mm = mm_scaler.transform(X_test)
    
    print("\nAfter MinMaxScaler:")
    print(f"  X_train range: [{X_train_mm.min():.1f}, {X_train_mm.max():.1f}]")
    print(f"  X_test range:  [{X_test_mm.min():.2f}, {X_test_mm.max():.2f}]")
    print(f"  (Test may exceed [0,1] because scaler was fit on train data only)")
    
    print("-" * 60)
    return X_train_std, X_test_std


def first_model_demo(X_train_scaled, X_test_scaled, y_train, y_test, iris):
    """Train a KNN classifier and make predictions."""
    print("\n--- 4. Your First Model: K-Nearest Neighbors ---")
    
    # Create and train the model
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train_scaled, y_train)
    
    # Make predictions
    y_pred = knn.predict(X_test_scaled)
    
    # Show some predictions
    print("Sample predictions (first 10):")
    print(f"  Actual:    {[iris.target_names[i] for i in y_test[:10]]}")
    print(f"  Predicted: {[iris.target_names[i] for i in y_pred[:10]]}")
    
    # Overall accuracy
    accuracy = knn.score(X_test_scaled, y_test)
    print(f"\nTest Accuracy: {accuracy:.2%}")
    
    # Predict on completely new data
    new_flower = np.array([[5.0, 3.4, 1.5, 0.2]])  # Looks like setosa
    # Scale using the same scaler (already fitted on training data)
    # Note: In practice, use a Pipeline to avoid manual scaling
    prediction = knn.predict(new_flower)  # This works but isn't properly scaled!
    print(f"\nNew flower {new_flower[0]} → Predicted: {iris.target_names[prediction[0]]}")
    
    print("-" * 60)
    return knn, y_pred


def evaluation_metrics_demo(y_test, y_pred, iris):
    """Demonstrate confusion matrix and classification report."""
    print("\n--- 5. Evaluation Metrics ---")
    
    # Accuracy
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.2%}")
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    print(f"\nConfusion Matrix:")
    print(f"  (Rows = Actual, Columns = Predicted)")
    
    # Pretty print with labels
    header = "          " + "  ".join(f"{name:>10}" for name in iris.target_names)
    print(header)
    for i, row in enumerate(cm):
        row_str = "  ".join(f"{val:>10}" for val in row)
        print(f"  {iris.target_names[i]:>8} {row_str}")
    
    # Classification Report (precision, recall, F1 per class)
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    print("-" * 60)


def cross_validation_demo(iris):
    """Demonstrate cross-validation for more reliable model evaluation."""
    print("\n--- 6. Cross-Validation ---")
    
    X, y = iris.data, iris.target
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    knn = KNeighborsClassifier(n_neighbors=5)
    
    # 5-fold cross-validation
    cv_scores = cross_val_score(knn, X_scaled, y, cv=5, scoring='accuracy')
    
    print(f"5-Fold CV Scores: {cv_scores.round(4)}")
    print(f"Mean Accuracy:    {cv_scores.mean():.2%}")
    print(f"Std Deviation:    {cv_scores.std():.2%}")
    print(f"Interpretation:   The model averages {cv_scores.mean():.2%} accuracy,")
    print(f"                  varying by ±{cv_scores.std():.2%} across folds.")
    
    # Compare different K values
    print(f"\nComparing different K values:")
    print(f"  {'K':>3}  {'Mean Accuracy':>15}  {'Std':>8}")
    print(f"  {'---':>3}  {'-------------':>15}  {'---':>8}")
    for k in [1, 3, 5, 7, 9, 11]:
        model = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
        print(f"  {k:>3}  {scores.mean():>15.2%}  {scores.std():>8.2%}")
    
    print("-" * 60)


def pipeline_demo(iris):
    """Demonstrate building a leak-free Pipeline."""
    print("\n--- 7. Pipelines: The Professional Way ---")
    
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Build a pipeline: scaler → KNN
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', KNeighborsClassifier(n_neighbors=5))
    ])
    
    # Use the pipeline like a single model
    pipe.fit(X_train, y_train)
    
    # Score
    train_score = pipe.score(X_train, y_train)
    test_score = pipe.score(X_test, y_test)
    print(f"Pipeline Train Accuracy: {train_score:.2%}")
    print(f"Pipeline Test Accuracy:  {test_score:.2%}")
    
    # Cross-validate the entire pipeline
    cv_scores = cross_val_score(pipe, X_train, y_train, cv=5, scoring='accuracy')
    print(f"\nPipeline 5-Fold CV: {cv_scores.mean():.2%} ± {cv_scores.std():.2%}")
    
    # Predict on new data (pipeline handles scaling automatically)
    new_flowers = np.array([
        [5.1, 3.5, 1.4, 0.2],  # Looks like setosa
        [6.7, 3.0, 5.2, 2.3],  # Looks like virginica
        [5.9, 3.0, 4.2, 1.5],  # Looks like versicolor
    ])
    predictions = pipe.predict(new_flowers)
    print(f"\nPredicting new flowers:")
    for flower, pred in zip(new_flowers, predictions):
        print(f"  {flower} → {iris.target_names[pred]}")
    
    # Access pipeline steps
    print(f"\nPipeline steps:")
    for name, step in pipe.named_steps.items():
        print(f"  '{name}': {step.__class__.__name__}")
    
    print("-" * 60)


if __name__ == "__main__":
    print("=" * 60)
    print("SCIKIT-LEARN BASICS: COMPLETE DEMO")
    print("=" * 60)
    
    iris = dataset_exploration_demo()
    X_train, X_test, y_train, y_test = train_test_split_demo(iris)
    X_train_scaled, X_test_scaled = feature_scaling_demo(X_train, X_test)
    knn, y_pred = first_model_demo(X_train_scaled, X_test_scaled, y_train, y_test, iris)
    evaluation_metrics_demo(y_test, y_pred, iris)
    cross_validation_demo(iris)
    pipeline_demo(iris)
    
    print("=" * 60)
    print("DEMO FINISHED SUCCESSFULLY")
    print("=" * 60)
