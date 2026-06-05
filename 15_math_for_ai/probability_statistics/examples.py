# Examples: Probability and Statistics in NumPy

import numpy as np

def descriptive_statistics_demo():
    print("--- 1. Descriptive Statistics ---")
    # Let's generate server latency times (in milliseconds) for a web application
    # We include a few extreme outliers to show the difference between mean and median
    latencies = np.array([120, 115, 118, 122, 110, 125, 119, 130, 112, 121, 950, 880])
    
    print(f"Server Latencies (ms): {latencies}")
    print(f"Number of data points: {len(latencies)}")
    
    # 1. Central Tendency
    mean_lat = np.mean(latencies)
    median_lat = np.median(latencies)
    print(f"Mean Latency: {mean_lat:.2f} ms  (Sensitive to extreme outliers!)")
    print(f"Median Latency: {median_lat:.2f} ms  (Robust to extreme outliers!)")
    
    # 2. Dispersion / Spread
    variance_lat = np.var(latencies) # Population variance
    std_lat = np.std(latencies)      # Population standard deviation
    print(f"Variance: {variance_lat:.2f} ms^2")
    print(f"Standard Deviation: {std_lat:.2f} ms")
    
    # 3. Percentiles & IQR
    q1 = np.percentile(latencies, 25)  # 25th percentile (Q1)
    q3 = np.percentile(latencies, 75)  # 75th percentile (Q3)
    iqr = q3 - q1                      # Interquartile Range
    p90 = np.percentile(latencies, 90) # 90th percentile
    p99 = np.percentile(latencies, 99) # 99th percentile (Common SLA metric)
    
    print(f"25th Percentile (Q1): {q1:.2f} ms")
    print(f"75th Percentile (Q3): {q3:.2f} ms")
    print(f"Interquartile Range (IQR): {iqr:.2f} ms (Middle 50% of data)")
    print(f"90th Percentile: {p90:.2f} ms")
    print(f"99th Percentile (SLA threshold): {p99:.2f} ms")
    print("-" * 50)

def conditional_probability_demo():
    print("\n--- 2. Conditional Probability & Joint Probability ---")
    # Let's define a contingency table (joint frequency matrix) of website visitors:
    # Rows represent Dev Device: [0: Mobile, 1: Desktop]
    # Columns represent Action: [0: Abandoned Cart, 1: Completed Purchase]
    #
    #                 Abandoned (C0)    Purchased (C1)
    # Mobile (R0)         400                 100
    # Desktop (R1)        150                 350
    
    frequencies = np.array([[400, 100],
                            [150, 350]])
    
    total_visitors = np.sum(frequencies)
    print(f"Contingency Table (Joint Frequencies):\n{frequencies}")
    print(f"Total Visitors: {total_visitors}")
    
    # Convert frequencies to Joint Probabilities P(Device, Action)
    joint_probabilities = frequencies / total_visitors
    print(f"\nJoint Probabilities P(Device, Action):\n{joint_probabilities}")
    
    # Marginal Probabilities
    # P(Device) - Sum across columns
    p_device = np.sum(joint_probabilities, axis=1) # [P(Mobile), P(Desktop)]
    # P(Action) - Sum across rows
    p_action = np.sum(joint_probabilities, axis=0) # [P(Abandon), P(Purchase)]
    
    print(f"\nMarginal Probabilities:")
    print(f"  P(Mobile Device): {p_device[0]:.4f}")
    print(f"  P(Desktop Device): {p_device[1]:.4f}")
    print(f"  P(Completed Purchase): {p_action[1]:.4f}")
    
    # Conditional Probability: P(Purchase | Desktop)
    # Formula: P(Purchase and Desktop) / P(Desktop)
    p_purchase_and_desktop = joint_probabilities[1, 1]
    p_desktop = p_device[1]
    p_purchase_given_desktop = p_purchase_and_desktop / p_desktop
    
    # Conditional Probability: P(Purchase | Mobile)
    p_purchase_and_mobile = joint_probabilities[0, 1]
    p_mobile = p_device[0]
    p_purchase_given_mobile = p_purchase_and_mobile / p_mobile
    
    print(f"\nConditional Probabilities:")
    print(f"  P(Purchase | Desktop): {p_purchase_given_desktop:.4f} (Conversion rate on Desktop)")
    print(f"  P(Purchase | Mobile): {p_purchase_given_mobile:.4f} (Conversion rate on Mobile)")
    print("-" * 50)

def bayes_theorem_demo():
    print("\n--- 3. Bayes' Theorem in Action ---")
    # Scenario: Let's build a simple spam filter for a single word: "FREE".
    # We want to find P(Spam | "FREE") - the probability an email is spam given it contains "FREE".
    #
    # Known prior probabilities:
    # P(Spam) = 0.20  (20% of incoming emails are spam)
    # P(Ham) = 0.80   (80% are legitimate)
    #
    # Known likelihoods (from historical training data):
    # P("FREE" | Spam) = 0.70  (70% of spam emails contain the word "FREE")
    # P("FREE" | Ham) = 0.05   (Only 5% of legitimate emails contain "FREE")
    
    p_spam = 0.20
    p_ham = 0.80
    
    p_free_given_spam = 0.70
    p_free_given_ham = 0.05
    
    # 1. Calculate the Total Probability of the evidence P("FREE")
    # P(E) = P(E | H)P(H) + P(E | not H)P(not H)
    p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)
    
    # 2. Calculate the Posterior Probability P(Spam | "FREE") using Bayes' Theorem
    # P(H | E) = [ P(E | H) * P(H) ] / P(E)
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free
    
    print(f"Prior Probability P(Spam): {p_spam:.2f}")
    print(f"Likelihood P('FREE' | Spam): {p_free_given_spam:.2f}")
    print(f"Likelihood P('FREE' | Ham): {p_free_given_ham:.2f}")
    print(f"Total Probability of Evidence P('FREE'): {p_free:.4f}")
    print(f"Posterior Probability P(Spam | 'FREE'): {p_spam_given_free:.4f}")
    print(f"Meaning: If an email contains 'FREE', there is a {p_spam_given_free*100:.2f}% chance it is Spam!")
    print("-" * 50)

def normal_distribution_zscore_demo():
    print("\n--- 4. Normal Distribution & Z-scores ---")
    # Imagine a manufacturer of high-precision sensor chips. 
    # The sensor thickness follows a Normal distribution with:
    # Mean (mu) = 10.0 mm, Standard Deviation (sigma) = 0.2 mm
    
    mu, sigma = 10.0, 0.2
    print(f"Sensor Thickness Distribution: Normal(mu={mu} mm, sigma={sigma} mm)")
    
    # Let's inspect three different manufactured sensors
    sensors = np.array([10.1, 9.4, 10.6])
    
    print("\nZ-score analysis for manufactured sensors:")
    for sensor in sensors:
        # z = (x - mu) / sigma
        z = round((sensor - mu) / sigma, 4)
        print(f"  Sensor thickness: {sensor:.2f} mm | Z-score: {z:+.2f}")
        
        # Interpret using empirical rule or standard statistical thresholds
        if abs(z) >= 3.0:
            print(f"    --> Outlier Alert! Extreme anomaly (probability < 0.3%). Reject sensor.")
        elif abs(z) >= 2.0:
            print(f"    --> Warning! Uncommon dimension (probability ~ 4.5%). Keep under monitoring.")
        else:
            print(f"    --> Standard/Typical sensor (within 95% threshold).")
    print("-" * 50)

def central_limit_theorem_demo():
    print("\n--- 5. Central Limit Theorem (CLT) Simulation ---")
    # The CLT states that if we sample from *any* population, the sample means will be normally distributed.
    # Let's start with a highly skewed Exponential distribution (representing times between phone calls).
    # Population Mean = 10.0
    scale = 10.0
    
    # We take 2000 samples, but each "sample" is actually the average of `sample_size` individuals.
    num_samples = 2000
    
    print(f"Starting simulation of Central Limit Theorem...")
    print(f"Original Distribution: Skewed Exponential (Scale = {scale})")
    
    for sample_size in [2, 10, 50]:
        # Generate 2000 samples, each of size `sample_size`, and compute the mean of each sample
        # np.random.exponential(scale, size=(num_samples, sample_size)) creates a shape (2000, sample_size)
        samples = np.random.exponential(scale, size=(num_samples, sample_size))
        sample_means = np.mean(samples, axis=1) # Shape: (2000,)
        
        # Calculate statistics of the sample means
        mean_of_means = np.mean(sample_means)
        std_of_means = np.std(sample_means)
        
        # Skewness is a measure of asymmetry. A normal distribution has skewness of 0.
        # We can calculate skewness using a simple formula: Mean cubed deviation / std cubed
        skewness = np.mean((sample_means - mean_of_means)**3) / (std_of_means**3)
        
        print(f"  Sample Size: {sample_size:<2} | Mean of Sample Means: {mean_of_means:.2f} (Expected: {scale}) | Std (Standard Error): {std_of_means:.4f} (Expected: {scale/np.sqrt(sample_size):.4f}) | Skewness: {skewness:+.4f}")
    
    print("\nNotice how Skewness drops dramatically towards 0 as Sample Size increases!")
    print("This proves the sample means are converging to a perfectly symmetric Normal Distribution!")
    print("-" * 50)

if __name__ == "__main__":
    print("=" * 60)
    print("=== STARTING PROBABILITY & STATISTICS BASICS DEMO ===")
    print("=" * 60)
    descriptive_statistics_demo()
    conditional_probability_demo()
    bayes_theorem_demo()
    normal_distribution_zscore_demo()
    central_limit_theorem_demo()
    print("=== DEMO FINISHED SUCCESSFULLY ===")
    print("=" * 60)
