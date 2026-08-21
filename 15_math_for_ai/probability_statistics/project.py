"""
PROJECT: Probability & Statistics AI Engine

This project demonstrates two crucial real-world AI applications of probability and statistics:
1. A Naive Bayes Spam Classifier built entirely from scratch in NumPy/Python.
2. A Gaussian Anomaly Detector for server monitoring that leverages Z-scores.

Both parts contain fully functional, elegant, and highly educational implementations.
"""

import numpy as np
import re

# =====================================================================
# PART 1: NAIVE BAYES SPAM CLASSIFIER FROM SCRATCH
# =====================================================================

class NaiveBayesSpamClassifier:
    def __init__(self, alpha=1.0):
        """
        Naive Bayes classifier with Laplace smoothing.
        alpha: smoothing parameter (default 1.0)
        """
        self.alpha = alpha
        self.vocab = set()
        self.word_counts_spam = {}
        self.word_counts_ham = {}
        self.total_words_spam = 0
        self.total_words_ham = 0
        self.p_spam = 0.0
        self.p_ham = 0.0
        
    def _tokenize(self, text):
        """
        Cleans and tokenizes text into lowercase words.
        """
        clean_text = text.lower()
        # Keep only alphanumeric words and spaces
        clean_text = re.sub(r'[^a-z0-9\s]', '', clean_text)
        return clean_text.split()
        
    def fit(self, X_texts, y_labels):
        """
        Trains the classifier on labeled text data.
        X_texts: List of message strings
        y_labels: NumPy array of binary labels (1 for Spam, 0 for Ham)
        """
        num_docs = len(X_texts)
        num_spam = np.sum(y_labels)
        num_ham = num_docs - num_spam
        
        # 1. Calculate Priors: P(Spam) and P(Ham)
        self.p_spam = num_spam / num_docs
        self.p_ham = num_ham / num_docs
        
        # Reset frequencies
        self.vocab = set()
        self.word_counts_spam = {}
        self.word_counts_ham = {}
        self.total_words_spam = 0
        self.total_words_ham = 0
        
        # 2. Compute word frequencies per class
        for text, label in zip(X_texts, y_labels):
            tokens = self._tokenize(text)
            for token in tokens:
                self.vocab.add(token)
                if label == 1:
                    self.word_counts_spam[token] = self.word_counts_spam.get(token, 0) + 1
                    self.total_words_spam += 1
                else:
                    self.word_counts_ham[token] = self.word_counts_ham.get(token, 0) + 1
                    self.total_words_ham += 1
                    
        print(f"Naive Bayes Training Completed:")
        print(f"  Training messages: {num_docs} (Spam: {num_spam}, Ham: {num_ham})")
        print(f"  Vocabulary size (unique words): {len(self.vocab)}")
        print(f"  Total words in Spam class: {self.total_words_spam}")
        print(f"  Total words in Ham class: {self.total_words_ham}")
        print(f"  Prior Probability P(Spam): {self.p_spam * 100:.1f}%")
        print(f"  Prior Probability P(Ham): {self.p_ham * 100:.1f}%")
        print("-" * 50)
        
    def predict(self, message):
        """
        Classifies an input message as Spam (1) or Ham (0).
        Uses Log-Probabilities to prevent float underflow.
        """
        tokens = self._tokenize(message)
        vocab_size = len(self.vocab)
        
        # We start with the log of the prior probability: log(P(Class))
        log_prob_spam = np.log(self.p_spam)
        log_prob_ham = np.log(self.p_ham)
        
        # Compute product of word likelihoods (accumulated via addition in log space)
        # Using Laplace smoothing: P(word | Class) = (count + alpha) / (total_words + alpha * vocab_size)
        for word in tokens:
            # We only evaluate words present in our training vocabulary to maintain stability
            if word in self.vocab:
                # Spam class likelihood
                count_spam = self.word_counts_spam.get(word, 0)
                p_word_spam = (count_spam + self.alpha) / (self.total_words_spam + self.alpha * vocab_size)
                log_prob_spam += np.log(p_word_spam)
                
                # Ham class likelihood
                count_ham = self.word_counts_ham.get(word, 0)
                p_word_ham = (count_ham + self.alpha) / (self.total_words_ham + self.alpha * vocab_size)
                log_prob_ham += np.log(p_word_ham)
                
        # Compare log scores
        prediction = 1 if log_prob_spam > log_prob_ham else 0
        
        # Calculate relative percentage probabilities using standard Softmax
        max_log = max(log_prob_spam, log_prob_ham)
        exp_spam = np.exp(log_prob_spam - max_log)
        exp_ham = np.exp(log_prob_ham - max_log)
        sum_exp = exp_spam + exp_ham
        
        prob_spam = exp_spam / sum_exp
        prob_ham = exp_ham / sum_exp
        
        return prediction, prob_spam, prob_ham


# =====================================================================
# PART 2: GAUSSIAN ANOMALY DETECTOR FOR SERVERS
# =====================================================================

class GaussianAnomalyDetector:
    def __init__(self, threshold=3.0):
        """
        threshold: Z-score magnitude boundary for flagging anomalies (default 3.0)
        """
        self.threshold = threshold
        self.mu = 0.0
        self.sigma = 0.0
        
    def fit(self, baseline_data):
        """
        Fits a Gaussian profile (calculates Mean and Std Dev) on healthy historical data.
        """
        self.mu = np.mean(baseline_data)
        self.sigma = np.std(baseline_data)
        print(f"Gaussian Profile Established on Healthy Baseline:")
        print(f"  Historical sample points: {len(baseline_data)}")
        print(f"  Baseline Mean (mu): {self.mu:.4f}")
        print(f"  Baseline Standard Deviation (sigma): {self.sigma:.4f}")
        print("-" * 50)
        
    def monitor_stream(self, data_stream):
        """
        Processes an incoming stream of real-time measurements, 
        calculating z-scores and flagging anomalies.
        """
        print("Starting Real-Time Telemetry Monitoring:")
        print(f"  Anomaly Alert Threshold: |Z| >= {self.threshold}")
        print("-" * 75)
        print(f"  {'Reading Value':<15} | {'Calculated Z-Score':<20} | {'Status Indicator':<25}")
        print("-" * 75)
        
        anomalies_flagged = 0
        for i, val in enumerate(data_stream, 1):
            # Compute z-score relative to healthy baseline parameters
            z = (val - self.mu) / self.sigma
            
            # Check if z-score magnitude exceeds the anomaly threshold
            is_anomaly = abs(z) >= self.threshold
            
            if is_anomaly:
                status = "(: CRITICAL ANOMALY ALERT"
                anomalies_flagged += 1
            else:
                status = ":) Normal Operation"
                
            print(f"  Observation #{i:02d}: {val:>5.1f} | {z:>+19.4f} | {status}")
            
        print("-" * 75)
        print(f"Monitoring Session Finished. Flagged {anomalies_flagged} anomalies.")


# =====================================================================
# MAIN PIPELINE RUNNER
# =====================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("=== DUAL ENGINE: PROBABILITY & STATISTICS PROJECT ===")
    print("=" * 60)
    
    # -----------------------------------------------------------------
    # PIPELINE 1: Naive Bayes Text Spam Classifier
    # -----------------------------------------------------------------
    print("\n--- PIPELINE 1: Text Classification via Bayes' Theorem ---")
    
    # Toy dataset of training messages
    training_messages = [
        # Legitimate messages (Ham = Class 0)
        "Hey, are we still meeting for lunch today at 1 PM?",
        "Could you send me the latest reports for the team review?",
        "Will call you later tonight after the project meeting",
        "Let's go grab a warm cup of coffee this afternoon.",
        "Can you log in and verify the server status database?",
        "Thanks for the help, the document looks solid.",
        
        # Spam messages (Spam = Class 1)
        "WIN FREE CASH PRIZE NOW! CLICK THIS UNSECURED LINK!",
        "Buy cheap stock options fast! High return guaranteed!",
        "Get free retail gift cards and vouchers today!",
        "Claim your urgent cash bonus before it expires!",
        "Free notification: Your bank account is locked, click here!",
        "Earn easy money working from home! Earn big cash daily!"
    ]
    
    # Labeled outcomes: 0 = Legitimate, 1 = Spam
    training_labels = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
    
    classifier = NaiveBayesSpamClassifier(alpha=1.0)
    classifier.fit(training_messages, training_labels)
    
    # Test messages to evaluate our classifier
    test_messages = [
        "Hey, let's grab coffee tomorrow morning.",
        "URGENT: WIN FREE CASH TODAY! CLICK NOW!",
        "Can you send over the reports for the databases?"
    ]
    
    print("Testing spam classifier predictions:")
    for test in test_messages:
        pred, p_spam, p_ham = classifier.predict(test)
        label = "SPAM" if pred == 1 else "LEGITIMATE (HAM)"
        confidence = p_spam if pred == 1 else p_ham
        print(f"\n  Message: '{test}'")
        print(f"  Classification: {label} (Confidence: {confidence * 100:.2f}%)")
        print(f"  P(Spam|Message): {p_spam * 100:.2f}% | P(Ham|Message): {p_ham * 100:.2f}%")
        
    print("\n" + "=" * 60)
    
    # -----------------------------------------------------------------
    # PIPELINE 2: Gaussian Anomaly Detector
    # -----------------------------------------------------------------
    print("\n--- PIPELINE 2: Gaussian Server Anomaly Detector ---")
    
    # Let's generate synthetic historical server temperature measurements (in Celsius)
    # Healthy operation mean is 65 degrees, with standard deviation of 1.5.
    # We draw 200 random normal values representing standard operation baseline logs.
    np.random.seed(42)  # For deterministic reproducibility
    healthy_baseline = np.random.normal(loc=65.0, scale=1.5, size=200)
    
    detector = GaussianAnomalyDetector(threshold=3.0)
    detector.fit(healthy_baseline)
    
    # Telemetry stream of new incoming readings.
    # Includes standard variations and a few severe anomalies (e.g. overheating or sensor crashes)
    incoming_stream = [
        64.8, 66.2, 65.1, 70.2, 63.9, 
        80.5, # Critical Anomaly: CPU overheating spike! (Z-score should be high)
        64.5, 65.3, 66.0, 
        50.1, # Critical Anomaly: Sensor freeze / failure reading! (Z-score should be extremely low)
        65.2, 64.9
    ]
    
    detector.monitor_stream(incoming_stream)
    
    print("\n" + "=" * 60)
    print("=== All Pipeline Executions Finished Successfully ===")
    print("=" * 60)
