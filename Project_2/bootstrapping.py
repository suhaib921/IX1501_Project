import numpy as np

# Data array
data = np.array([56, 101, 78, 67, 93, 87, 64, 72, 80, 69])

n_bootstrap_samples = 10000  # Number of bootstrap samples
sample_mean = np.mean(data)  # Sample mean

# Define the bounds a and b
a = -4
b = 6

# Bootstrap resampling
bootstrap_means = []

np.random.seed(42)  # For reproducibility
for _ in range(n_bootstrap_samples):
    resample = np.random.choice(data, size=len(data), replace=True)
    bootstrap_mean = np.mean(resample)
    bootstrap_means.append(bootstrap_mean)

bootstrap_means = np.array(bootstrap_means)

# Estimate the probability that the bootstrap mean falls in the range [a, b] around the population mean
probability = np.mean((a < bootstrap_means - sample_mean) & (bootstrap_means - sample_mean < b))

print(f"Estimated probability: {probability}")
