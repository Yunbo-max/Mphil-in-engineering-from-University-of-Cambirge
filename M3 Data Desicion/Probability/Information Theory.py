
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns
# Shannon and Differential Entropy
# Shannon entropy for a binary random variable (e.g., coin flip) is:

def binary_entropy(my_p):
    return (my_p-1)*np.log(1-my_p) - my_p*np.log(my_p)

p = np.linspace(0.001, 0.999, 1000)

H = binary_entropy(p)

fig, ax = plt.subplots()
plt.title('Shannon entropy of Bernoulli trial')
plt.xlabel('p')
plt.ylabel('H (nats)')
ax.plot(p,H)


# Cross-Entropy
# Cross-entropy is a concept derived from KL divergence. Its detail is beyond the scope of this series except to mention that it provides us with the cross-entropy cost function.
def cross_entropy(y, a):
    return -1*(y*np.log(a) + (1-y)*np.log(1-a))

cross_entropy(1, 0.3)
