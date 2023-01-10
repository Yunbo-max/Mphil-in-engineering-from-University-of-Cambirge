import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
x_i = 85

mu = 90
sigma = 2
y = np.random.normal(mu, sigma, 10000)
sns.displot(y, color='gray')
plt.axvline(mu, color='orange')
for v in [-3, -2, -1, 1, 2, 3]:
    plt.axvline(mu+v*sigma, color='olivedrab')
    plt.axvline(x_i, color='purple')

z = (x_i - np.mean(y))/np.std(y)

print(100*len(np.where(y > 85)[0])/10000)
print(np.percentile(y, 1))
plt.show()


# limited number of data and for one data
# z = (85 - mu)/xigma
len(np.where(y > 85)[0])

# seems like infinity of data
st.norm.ppf(.025)
st.norm.ppf(.975)
# +-1.959963984540054 xigma  a/2=5%/2 = 2.5%
p_below = st.norm.cdf(-2.5)
p_above = 1-st.norm.cdf(2.5)
# +-2.5xigma ---> concrete number in the graph
p_outside = p_below + p_above
# p-values


# Where z-scores apply to individual values only, t-tests enables us to compare (the mean of) a sample of multiple values to a reference mean.
# single-sample t-test(1 samples)
x = [48, 50, 54, 60]
xbar = np.mean(x)
sx = st.sem(x)
t = (xbar-50)/sx
st.ttest_1samp(x, 50)
# Ttest_1sampResult(statistic=1.1338934190276817, pvalue=0.3392540508564543)

# Welch's Independent t-test (2samples)
sf = f.var(ddof=1)
sm = m.var(ddof=1)
nf = f.size
nm = m.size
t = (fbar-mbar)/(sf/nf + sm/nm)**(1/2)
# p value
st.ttest_ind(f, m, equal_var=False)

# Student's Paired t-test
# Indeed, with an independent t-test we could even have different sample sizes in the two groups whereas this is impossible with a paired t-test.
# t = (dbar-0)/sd(statistic=3.3541019662496847), pvalue=0.02846020325433834
st.ttest_rel(min15, min1)



# Machine Learning Examples
# Single-sample: Does my stochastic model tend to be more accurate than an established benchmark?
# Independent samples: Does my model have unwanted bias in it, e.g., do white men score higher than other demographic groups with HR model?
# Paired samples: Is new TensorFlow.js model significantly faster? (paired by browser / device)


# Confidence Intervals
def CIerr_calc(my_z, my_s, my_n):
    return my_z*(my_s/my_n**(1/2))
xbar = x.mean()
s = x.std()
n = x.size
CIerr = CIerr_calc(z, s, n)
xbar + CIerr
xbar - CIerr


# ANOVA: Analysis of Variance , enables us to compare more than two samples
# To apply ANOVA, we must make three assumptions:
# Independent samples
# Normally-distributed populations
# Homoscedasticity: Population standard deviations are equal
st.f_oneway(t, b, d)
# F_onewayResult(statistic=0.22627752438542714, pvalue=0.7980777848719299)



#Pearson Correlation Coefficient

# covariance provides a measure of how related the variables are to each other:
product = []
for i in range(n):
    product.append((x[i]-xbar)*(y[i]-ybar))
cov = sum(product)/n
# Correlation
r = cov/(np.std(x)*np.std(y))

# correlation + p value
st.pearsonr(x, y)
# The Coefficient of Determination
st.pearsonr(iris.sepal_length, iris.sepal_width)[0]**2




# In brief, three criteria are required for inferring causal relationships:
# Covariation: Two variables vary together (this criterion is satisfied by sepal and petal length)
# Temporal precedence: The affected variable must vary after the causal variable is varied.
# Elimination of extraneous variables: We must be sure no third variable is causing the variation. This can be tricky for data we obtained through observation alone, but easier when we can control the causal variable, e.g., with (ideally double-blind) randomized control trials.



# Bonferroni correction
# If you perform 20 statistical tests where there is no real effect (i.e., the null hypothesis is true), then we would expect one of them to come up significant by chance alone (i.e., a false positive or Type I error).
# If you perform a hundred tests in such a circumstance, then you should expect five false positives.
a = 0.05, a/n = 0.05/10 =0.005