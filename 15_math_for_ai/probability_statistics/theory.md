# Probability and Statistics for AI

While Linear Algebra lets us represent and transform data, **Probability and Statistics** let us reason about uncertainty and noise. In AI and Machine Learning, real-world data is inherently uncertain: sensors have noise, users behave unpredictably, and we rarely have complete information. 

Probability and statistics are the mathematical foundations used to train models to make predictions under uncertainty.

---

## 1. Descriptive Statistics: Summarizing Data

Before a model can learn, we must understand the shape of our data.

### Measures of Central Tendency
These describe the "center" or typical value of a dataset:
*   **Mean ($\mu$ or $\bar{x}$)**: The arithmetic average.
    $$\mu = \frac{1}{N} \sum_{i=1}^N x_i$$
*   **Median**: The middle value when data is sorted. It is highly robust to outliers (extreme values).
*   **Mode**: The most frequent value in the dataset.

### Measures of Dispersion (Spread)
These describe how spread out the data points are around the center:
*   **Variance ($\sigma^2$)**: The average of squared differences from the Mean.
    $$\sigma^2 = \frac{1}{N} \sum_{i=1}^N (x_i - \mu)^2$$
*   **Standard Deviation ($\sigma$)**: The square root of the variance. It is in the same units as the original data, making it easy to interpret.
    $$\sigma = \sqrt{\sigma^2}$$
*   **Percentiles**: The value below which a percentage of data falls (e.g., the 90th percentile is the value that is greater than 90% of all data points).
*   **Interquartile Range (IQR)**: The difference between the 75th percentile ($Q_3$) and 25th percentile ($Q_1$). Represents the middle 50% of the data.

---

## 2. Probability Basics: Reasoning under Uncertainty

Probability is a numerical measure of the likelihood that an event will occur, ranging from $0$ (impossible) to $1$ (certain).

### Types of Probability:
1.  **Marginal Probability**: The probability of a single event occurring, denoted as $P(A)$.
2.  **Joint Probability**: The probability of two events occurring simultaneously, denoted as $P(A \cap B)$ or $P(A, B)$.
3.  **Conditional Probability**: The probability of event $A$ occurring *given that* event $B$ has already occurred, denoted as $P(A | B)$.
    $$P(A | B) = \frac{P(A \cap B)}{P(B)}$$

---

## 3. Bayes' Theorem: Updating Beliefs

**Bayes' Theorem** is one of the most important equations in AI. It allows us to update the probability of a hypothesis ($H$) based on new incoming evidence ($E$):

$$P(H | E) = \frac{P(E | H) P(H)}{P(E)}$$

Where:
*   **$P(H | E)$ (Posterior)**: The updated probability of the hypothesis after observing the evidence.
*   **$P(E | H)$ (Likelihood)**: The probability of observing the evidence if the hypothesis is true.
*   **$P(H)$ (Prior)**: The initial probability of the hypothesis before seeing the evidence.
*   **$P(E)$ (Evidence)**: The total probability of the evidence occurring across all possible hypotheses.
    $$P(E) = P(E | H)P(H) + P(E | \text{not } H)P(\text{not } H)$$

*AI Application*: Used for classification (e.g. **Naive Bayes Classifiers** for email spam filtering, where we calculate $P(\text{Spam} | \text{Words})$).

---

## 4. Probability Distributions

A **probability distribution** is a mathematical function that describes the likelihood of obtaining various possible values for a variable.

### Discrete Distributions (Countable Outcomes)
*   **Binomial Distribution**: Models the number of successes in $n$ independent binary trials (e.g. coin flips, success/failure).
*   **Poisson Distribution**: Models the number of events occurring within a fixed interval of time or space (e.g. number of server requests per minute).

### Continuous Distributions (Infinite Outcomes)
*   **Normal (Gaussian) Distribution**: The famous "bell curve". It is symmetric around its mean ($\mu$), and its shape is entirely determined by its mean and standard deviation ($\sigma$).
    $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2}$$

#### The Empirical Rule ($68-95-99.7$ Rule):
In a normal distribution:
*   **$68.2\%$** of all data points fall within $1$ standard deviation of the mean ($\mu \pm 1\sigma$).
*   **$95.4\%$** fall within $2$ standard deviations ($\mu \pm 2\sigma$).
*   **$99.7\%$** fall within $3$ standard deviations ($\mu \pm 3\sigma$).

### The z-score (Standardization)
The $z$-score measures how many standard deviations a specific data point $x$ is away from the mean:
$$z = \frac{x - \mu}{\sigma}$$
*   A $z$-score of $+1.5$ means the point is $1.5$ standard deviations above the average.
*   A $z$-score magnitude $> 3.0$ represents an extremely rare event ($<0.3\%$ probability), making it highly useful for **Anomaly Detection**.

### The Central Limit Theorem (CLT)
The CLT states that if you take sufficiently large random samples from *any* population (regardless of its original distribution), the distribution of the sample means will follow a **Normal Distribution**. This is why the Normal Distribution is so prevalent in nature and statistics!

## Resources

- **Khan Academy: Statistics and Probability** – https://www.khanacademy.org/math/statistics-probability
- **3Blue1Brown: Probability (YouTube)** – https://www.youtube.com/watch?v=HZGCoVF3YvM
- **StatQuest: Statistics Fundamentals (YouTube)** – https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9
- **Think Stats (Free Book, Allen Downey)** – https://greenteapress.com/thinkstats2/
- **Mathematics for Machine Learning – Chapter 6: Probability** – https://mml-book.github.io/book/mml-book.pdf
- **SciPy Stats Module** – https://docs.scipy.org/doc/scipy/reference/stats.html
