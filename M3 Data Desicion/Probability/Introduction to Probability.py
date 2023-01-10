import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
from math import factorial

# random distribution + plot

# ns = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
# np.random.seed(42) # for reproducibility
# np.random.rand(3,4)
# np.random.randn(3,4)
# np.random.binomial(1, 0.5)
# heads_count = [np.random.binomial(n, 0.5) for n in ns]
# proportion_heads = heads_count/ns
#
#
# fig, ax = plt.subplots()
# plt.xlabel('Number of coin flips in experiment')
# plt.ylabel('Proportion of flips that are heads')
# plt.axhline(0.5, color='orange')
# ax.scatter(ns, proportion_heads)
# np.cov(x, y, ddof=0)
# st.pearsonr(x, y)[0]
# Covariance and correlation only account for linear relationships. Two variables could be non-linearly related to each other and these metrics could come out as zero
# plt.show()



# statistics
# n_experiments = 1000
# heads_count = np.random.binomial(5, 0.5, n_experiments)
#
# heads, event_count = np.unique(heads_count, return_counts=True)
# event_proba = event_count/n_experiments
#
# plt.bar(heads, event_proba, color='mediumpurple')
# plt.xlabel('Heads flips (out of 5 tosses)')
# plt.ylabel('Event probability')
#
# plt.show()

# distribution
# x_array = np.arange(-5, 5, 0.03)
# y_pdf = st.norm.pdf(x_array,0,1)
# y_pdf = st.skewnorm.pdf(x_array,0,1)
# plt.plot(x_array, y_pdf)
# plt.show()
#
# z_score_stat, p_value = st.normaltest(y_pdf)
# print(z_score_stat,p_value)



# def coinflip_prob(n, k):
#     n_choose_k = factorial(n)/(factorial(k)*factorial(n-k))
#     return n_choose_k/2**n
#
# P = [coinflip_prob(5, x) for x in range(6)]
# E = sum([P[x]*x for x in range(6)])
#
# count = [1,2,3,4,5,6,7,7]
# np.mean(count)
# np.var(x)
# np.std(x)
# np.median(count)
# st.sem(x)
# print(st.mode(count)[0][0])

#
x = st.skewnorm.rvs(0, size=1000)
q = np.percentile(x, [25, 50, 75])
np.quantile(x, [.95, .99])

sns.set(style='whitegrid')
sns.boxplot(x=x)
plt.hist(x, color = 'lightgray')
print(q)
plt.show()
# Box edges define the inter-quartile range (IQR):
#

