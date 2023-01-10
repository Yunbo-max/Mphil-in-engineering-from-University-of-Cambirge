import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
from math import factorial

u = np.random.uniform(size=10000)
sns.displot(u)

x = np.random.normal(size=10000)
sns.displot(x, kde=True)


def sample_mean_calculator(input_dist, sample_size, n_samples):
    sample_means = []
    for i in range(n_samples):
        sample = np.random.choice(input_dist, size=sample_size, replace=False)
        sample_means.append(sample.mean())
    return sample_means
sns.displot(sample_mean_calculator(x, 100, 1000), color='green', kde=True)


s = st.skewnorm.rvs(10, size=10000)
sns.displot(sample_mean_calculator(s, 10, 1000), color='green', kde=True)


# Sampling from a multimodal distribution
# The Central Limit Theorem
m = np.concatenate((np.random.normal(size=5000), np.random.normal(loc = 4.0, size=5000)))
sns.displot(sample_mean_calculator(m, 1000, 1000), color='green', kde=True)

# Log-Normal Distribution
# Its logarithm has a skewed distribution:
x = np.random.lognormal(size=10000) # defaults to standard normal mu=0, sigma=1

# Laplace Distribution
x = np.random.laplace(size=10000)
sns.displot(x)
sns.displot(x, kde=True)

# discrete distribution
# Binomial Distribution
n = 5
n_experiments = 1000
heads_count = np.random.binomial(n, 0.5, n_experiments)
heads, event_count = np.unique(heads_count, return_counts=True)
event_proba = event_count/n_experiments
plt.bar(heads, event_proba, color='mediumpurple')
plt.xlabel('Heads flips (out of 5 tosses)')
_ = plt.ylabel('Event probability')

# Poisson Distribution
lam=5
n=1000
samples = np.random.poisson(lam, n)
samples[0:20]
x, x_count = np.unique(samples, return_counts=True)
Px = x_count/n
plt.bar(x, Px, color='mediumpurple')
plt.title('PMF of Poisson with lambda = {}'.format(lam))
plt.xlabel('x')
plt.ylabel('P(x)')

# Gaussian mixture model (GMM) is common type of mixture distribution, wherein all of the component distributions are normal.


plt.show()
