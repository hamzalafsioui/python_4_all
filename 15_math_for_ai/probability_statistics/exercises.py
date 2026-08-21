"""
EXERCISES: Probability and Statistics Basics

This script contains 3 practical exercises on descriptive statistics, probability, 
and z-scores using NumPy. Complete or review the TODO sections to understand 
how to translate mathematical statistics to Python code.
"""

import numpy as np

# =====================================================================
# EXERCISE 1: Descriptive Analytics for SLA Latencies
# =====================================================================
# As a Reliability Engineer, you are monitoring API request latencies (in milliseconds).
# You need to calculate critical statistics to assess if your API complies with the 
# Service Level Agreement (SLA). The SLA requires that 90% of requests are below 200ms.

latencies = np.array([105, 120, 115, 98, 350, 112, 125, 420, 130, 108, 118, 145])

def calculate_sla_metrics(data):
    """
    Calculates key descriptive statistics for a latency dataset:
    Mean, Median, 90th Percentile, IQR, and Variance.
    """
    # TODO: Calculate and return the descriptive metrics using NumPy
    mean_val = np.mean(data)
    median_val = np.median(data)
    p90_val = np.percentile(data, 90)
    
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr_val = q3 - q1
    
    variance_val = np.var(data)
    
    return {
        "mean": mean_val,
        "median": median_val,
        "p90": p90_val,
        "iqr": iqr_val,
        "variance": variance_val
    }

print("=== Exercise 1: Descriptive SLA Metrics ===")
metrics = calculate_sla_metrics(latencies)

print(f"API Latencies: {latencies}")
print(f"Mean Latency: {metrics['mean']:.2f} ms")
print(f"Median Latency: {metrics['median']:.2f} ms")
print(f"90th Percentile: {metrics['p90']:.2f} ms")
print(f"Interquartile Range (IQR): {metrics['iqr']:.2f} ms")
print(f"Variance: {metrics['variance']:.2f} ms^2")

# Verify SLA Compliance: 90th percentile must be < 200 ms
sla_compliant = metrics['p90'] < 200.0
print(f"Is API SLA Compliant? {sla_compliant} (90th percentile must be < 200ms)")
print("-" * 50)


# =====================================================================
# EXERCISE 2: Bayesian Spam Filtering
# =====================================================================
# Implement a function to calculate the probability that an email is spam, 
# given that it contains a specific keyword.
# Formula: P(Spam | Word) = [ P(Word | Spam) * P(Spam) ] / P(Word)
# where: P(Word) = P(Word | Spam) * P(Spam) + P(Word | Ham) * P(Ham)

def calculate_bayes_posterior(p_prior_spam, p_word_given_spam, p_word_given_ham):
    """
    Computes P(Spam | Word) using Bayes' Theorem.
    """
    # TODO 1: Compute P(Ham) which is 1 - P(Spam)
    p_prior_ham = 1.0 - p_prior_spam
    
    # TODO 2: Compute total probability of the evidence: P(Word)
    p_word = (p_word_given_spam * p_prior_spam) + (p_word_given_ham * p_prior_ham)
    
    # TODO 3: Apply Bayes' Theorem to find P(Spam | Word)
    p_spam_given_word = (p_word_given_spam * p_prior_spam) / p_word
    
    return p_spam_given_word

print("\n=== Exercise 2: Bayesian Spam Inference ===")

# Scenario: The keyword is "CASH".
# Prior probability of spam: 25% of all emails are spam
# 85% of spam emails contain the word "CASH"
# Only 4% of legitimate emails contain the word "CASH"
prior_spam = 0.25
likelihood_cash_spam = 0.85
likelihood_cash_ham = 0.04

post_spam = calculate_bayes_posterior(prior_spam, likelihood_cash_spam, likelihood_cash_ham)

print(f"Prior probability of Spam: {prior_spam * 100:.1f}%")
print(f"Likelihood P('CASH' | Spam): {likelihood_cash_spam * 100:.1f}%")
print(f"Likelihood P('CASH' | Ham): {likelihood_cash_ham * 100:.1f}%")
print(f"Posterior probability P(Spam | 'CASH'): {post_spam * 100:.2f}%")
print("-" * 50)


# =====================================================================
# EXERCISE 3: Outlier Anomaly Filter
# =====================================================================
# Real-world datasets often contain erroneous outliers due to sensor errors.
# In a normal distribution, data points with a z-score magnitude >= 2.0 
# are statistically uncommon (less than 5% probability).
# Write a function to calculate z-scores and identify outliers.

temperatures = np.array([22.1, 21.8, 22.5, 23.0, 19.5, 22.0, 21.9, 38.5, 22.2, 22.4, 5.2, 22.0])

def detect_outliers_zscore(data, threshold=2.0):
    """
    Identifies data points that are statistical outliers based on z-scores.
    Returns:
        z_scores: np.ndarray containing z-scores for all elements.
        outliers_mask: boolean np.ndarray where True indicates an outlier.
    """
    mu = np.mean(data)
    sigma = np.std(data)
    
    # Avoid division by zero in case std is 0
    if sigma == 0:
        return np.zeros_like(data), np.zeros_like(data, dtype=bool)
        
    # TODO 1: Implement the z-score formula: z = (x - mu) / sigma
    # Note: NumPy allows this to be vectorized (computed all at once!)
    z_scores = (data - mu) / sigma
    
    # TODO 2: Create a boolean mask where True indicates absolute z-score >= threshold
    outliers_mask = np.abs(z_scores) >= threshold
    
    return z_scores, outliers_mask

print("\n=== Exercise 3: Z-Score Outlier Filter ===")
z_scores, outliers_mask = detect_outliers_zscore(temperatures, threshold=2.0)

print(f"Temperature Data: {temperatures}")
print("\nCalculated Z-scores:")
for temp, z, is_outlier in zip(temperatures, z_scores, outliers_mask):
    status = "[OUTLIER]" if is_outlier else "[NORMAL]"
    print(f"  Temp: {temp:>4.1f} C | Z-score: {z:>+5.2f} | Status: {status}")

# Retrieve the clean data and outlier data
clean_temps = temperatures[~outliers_mask]
outlier_temps = temperatures[outliers_mask]

print(f"\nFiltered Outliers: {outlier_temps}")
print(f"Cleaned Dataset: {clean_temps}")
print("=" * 60)

if __name__ == "__main__":
    print("\nAll probability and statistics exercises completed successfully!")
