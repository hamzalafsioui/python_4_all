The code is essentially a **mini Probability & Statistics course using NumPy**. It covers the most important statistical concepts that are used in:

* Data Science
* Machine Learning
* AI
* Analytics
* Software Performance Monitoring
* A/B Testing

---

# 1. Descriptive Statistics

Goal: **Describe a dataset with a few numbers.**

Dataset:

```python
latencies = np.array([
120,115,118,122,110,125,119,130,112,121,950,880
])
```

Most values are around 120 ms.

But:

```python
950
880
```

are extreme outliers.

---

## np.mean()

Calculates the average.

```python
mean_lat = np.mean(latencies)
```

Formula:


$$
Mean = \frac{\sum x}{n}
$$


Example:

```python
[10,20,30]
```

Mean:


$$
\frac{10+20+30}{3}=20
$$


---

## np.median()

Middle value after sorting.

```python
median_lat = np.median(latencies)
```

Example:

```python
[10,20,30]
```

Median = 20

Example:

```python
[10,20,30,40]
```

Median:


$$
\frac{20+30}{2}=25
$$


---

### Why Median?

Suppose:

```python
[100,110,120,130,5000]
```

Mean:


$$
1092
$$


which is misleading.

Median:


$$
120
$$


Much more realistic.

---

## np.var()

Variance measures spread.

```python
variance_lat = np.var(latencies)
```

Formula:


$$
Variance=
\frac{\sum(x-\mu)^2}{n}
$$


Steps:

1. Find mean
2. Distance from mean
3. Square distances
4. Average them

Large variance = data spread out.

---

## np.std()

Standard deviation.

```python
std_lat = np.std(latencies)
```

Formula:


$$
Std=\sqrt{Variance}
$$


Why?

Because variance uses squared units.

If latency is in milliseconds:

```text
Variance -> ms²
Std -> ms
```

Standard deviation is easier to interpret.

---

## np.percentile()

```python
np.percentile(data, 25)
```

Finds a value below which 25% of data lies.

---

### Quartiles

```python
Q1 = 25%
Q2 = Median = 50%
Q3 = 75%
```

Example:

```python
1 2 3 4 5 6 7 8
```

Q1 ≈ 2.5

Q2 = 4.5

Q3 ≈ 6.5

---

### IQR

```python
iqr = q3 - q1
```

Measures middle 50% spread.

Useful for detecting outliers.

---

### P90 and P99

```python
p90 = np.percentile(data,90)
p99 = np.percentile(data,99)
```

Used heavily in backend systems.

Example:

```text
P90 = 200 ms
```

Means:

90% of requests finish under 200 ms.

---

# 2. Conditional Probability

Topic:

> What is the probability of A given B?

Notation:


$$
P(A|B)
$$


---

### Contingency Table

```python
frequencies = np.array([
[400,100],
[150,350]
])
```

| Device  | Abandon | Purchase |
| ------- | ------- | -------- |
| Mobile  | 400     | 100      |
| Desktop | 150     | 350      |

---

## np.sum()

Adds numbers.

```python
total = np.sum(frequencies)
```

Result:

```python
1000
```

---

### Joint Probability

```python
joint_probabilities = frequencies / total
```

Example:

Desktop + Purchase:


$$
\frac{350}{1000} = 0.35
$$


Meaning:

35% of all visitors are desktop users who purchased.

---

### Marginal Probability

```python
np.sum(joint_probabilities, axis=1)
```

Axis explanation:

```python
axis=0
↓
Columns

axis=1
→
Rows
```

---

### Conditional Probability

Formula:


$$
P(A|B)=\frac{P(A\cap B)}{P(B)}
$$


Example:


$$
P(Purchase|Desktop) = \frac{0.35}{0.50} = 0.70
$$


Meaning:

70% of desktop visitors purchase.

---

# 3. Bayes Theorem

One of the most important formulas in AI.

---

Formula:

$$
P(H|E)=\frac{P(E|H)P(H)}{P(E)}
$$
Where:

* H = hypothesis
* E = evidence

---

### Spam Example

Known:

```python
P(Spam)=0.20
```

20% emails are spam.

---

```python
P(FREE|Spam)=0.70
```

70% of spam emails contain FREE.

---

```python
P(FREE|Ham)=0.05
```

Only 5% of normal emails contain FREE.

---

### Step 1

Find:


$$
P(FREE)
$$


Total probability:


$$
P(FREE)=
P(FREE|Spam)P(Spam)
+
P(FREE|Ham)P(Ham)
$$


---

### Step 2

Apply Bayes.

Result:

```python
77.78%
```

Meaning:

If an email contains FREE, there is about a 78% chance it's spam.

---

# 4. Normal Distribution & Z-Score

The famous bell curve.


$$
z=\frac{x-\mu}{\sigma}
$$


---

Variables:

* x = observed value
* μ = mean
* σ = standard deviation

---

Example:

```python
mean = 10
std = 0.2
sensor = 10.6
```

Compute:
$$
z = \frac{10.6-10}{0.2} = 3
$$

---

Interpretation

| Z Score | Meaning   |
| ------- | --------- |
| 0       | Average   |
| ±1      | Normal    |
| ±2      | Uncommon  |
| ±3      | Very Rare |

---

Why important?

Used in:

* Fraud detection
* Anomaly detection
* Manufacturing
* Machine Learning

---

# 5. Central Limit Theorem (CLT)

One of the most important concepts in statistics.

The theorem says:

> Even if the original data is not normal, the averages of many samples become approximately normal.

---

Original distribution:

```python
Exponential
```

which is heavily skewed.

---

Generate samples:

```python
samples =
np.random.exponential(
scale,
size=(2000,sample_size)
)
```

Creates:

```python
2000 samples
```

each containing:

```python
sample_size
```

values.

---

## np.random.exponential()

Creates random numbers from an exponential distribution.

Example:

```python
np.random.exponential(10,5)
```

Output:

```python
[5.2, 1.1, 7.3, 20.5, 2.8]
```

---

### Sample Means

```python
sample_means =
np.mean(samples, axis=1)
```

Each row becomes one average.

---

### Standard Error

Theory says:

$$
SE=\frac{\sigma}{\sqrt{n}}
$$
As sample size grows:

```text
n ↑
SE ↓
```

Means estimates become more stable.

---

### Skewness

```python
skewness =
np.mean((x-mean)**3) / std**3
```

Measures asymmetry.

| Value | Meaning    |
| ----- | ---------- |
| 0     | Symmetric  |
| >0    | Right skew |
| <0    | Left skew  |

For large sample sizes:

```python
2 → 10 → 50
```

skewness approaches:

```python
0
```

which confirms the CLT.

---

# Important NumPy Methods Used

| Method                    | Purpose                            |
| ------------------------- | ---------------------------------- |
| `np.array()`              | Create arrays                      |
| `np.mean()`               | Average                            |
| `np.median()`             | Median                             |
| `np.var()`                | Variance                           |
| `np.std()`                | Standard deviation                 |
| `np.percentile()`         | Percentiles                        |
| `np.sum()`                | Sum values                         |
| `np.random.exponential()` | Generate exponential random values |
| `len()`                   | Number of elements                 |
| `axis=0`                  | Work column-wise                   |
| `axis=1`                  | Work row-wise                      |

# What You Should Learn After This

A good learning order is:

1. Mean, Median, Mode
2. Variance & Standard Deviation
3. Percentiles & IQR
4. Probability Basics
5. Joint Probability
6. Conditional Probability
7. Bayes Theorem
8. Normal Distribution
9. Z-Scores
10. Sampling
11. Central Limit Theorem
12. Hypothesis Testing
13. Correlation
14. Linear Regression
15. Machine Learning Statistics


