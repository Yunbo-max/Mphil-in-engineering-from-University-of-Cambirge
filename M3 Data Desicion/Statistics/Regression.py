import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

# Linear Least Squares for Fitting a Line to Points on a Cartesian Plane
#  fitting a line to points on a Cartesian plane (2-D surface, with -axis perpendicular to horizontal -axis). To fit such a line, the only parameters we require are a -intercept (say, ) and a slope (say, ):

# beta1 = cov/np.var(x)
# beta0 = ybar - beta1*xbar
# xline = np.linspace(4, 8, 1000)
# yline = beta0 + beta1*xline
#
# sns.scatterplot(x=x, y=y)
# plt.plot(xline, yline, color='orange')



x = np.array([0, 1, 2, 3, 4, 5, 6, 7.])
y = np.array([1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37])

cov_mat = np.cov(x, y)
beta1 = cov_mat[0,1]/cov_mat[0,0]
beta0 = y.mean() - beta1*x.mean()
xline = np.linspace(0, 7, 1000)
yline = beta0 + beta1*xline
sns.scatterplot(x=x, y=y)
x_i = 4.5
y_i = beta0 + beta1*x_i
plt.title("Clinical Trial")
plt.xlabel("Drug dosage (mL)")
plt.ylabel("Forgetfulness")
plt.plot(xline, yline, color='orange')
plt.scatter(x_i, y_i, marker='o', color='purple')
plt.show()


# Ordinary Least Squares
# estimate the parameters of regression models that have more than one predictor variable
x = np.array([1, 2, 3, 4.])
y = np.array([6, 5, 7, 10.])
A = np.array([[8, 20],[20, 60]])
z = np.array([56, 154])
Ainv = np.linalg.inv(A)
w = np.dot(Ainv, z)
xline = np.linspace(1, 4, 1000)
yline = w[0] + w[1]*xline
fig, ax = plt.subplots()
plt.title('Generative Adversarial Network')
plt.xlabel('Number of convolutional layers')
plt.ylabel('Image realism (out of 10)')
ax.scatter(x, y)
plt.plot(xline, yline, color='orange')

# ncidentally, residuals are the distances between
X = np.concatenate([np.matrix(np.ones(x.size)).T, np.matrix(x).T], axis=1)
yhat = np.dot(X, w)
fig, ax = plt.subplots()
plt.title('Generative Adversarial Network')
plt.xlabel('Number of convolutional layers')
plt.ylabel('Image realism (out of 10)')
ax.scatter(x, y)
plt.plot(xline, yline, color='orange')
for i in range(x.size):
    plt.plot([x[i],x[i]], [y[i],yhat[0,i]], color='darkred')
plt.show()

# The above OLS approach expands to a wide variety of circumstances:
#
# Multiple features (, the predictors)
# Polynomial (typically quadratic) features, e.g.,
# Interacting features, e.g.,
# Discrete, categorical features, incl. any combination of continuous and discrete features

import statsmodels.api as sm
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=iris)
dummy = pd.get_dummies(iris.species)
y = iris.petal_length
X = pd.concat([iris.sepal_length, dummy.setosa, dummy.versicolor], axis=1)
X = sm.add_constant(X)
model = sm.OLS(y, X)
result = model.fit()
result.summary()
beta = result.params
xline = np.linspace(4, 8, 1000)
vi_yline = beta[0] + beta[1]*xline
se_yline = beta[0] + beta[1]*xline + beta[2]
ve_yline = beta[0] + beta[1]*xline + beta[3]
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=iris)
plt.plot(xline, vi_yline, color='darkgreen')
plt.plot(xline, se_yline, color='darkblue')
_ = plt.plot(xline, ve_yline, color='orange')
plt.show()


# Logistic Regression----- a binary outcome

gender = pd.get_dummies(titanic['sex'])
clas = pd.get_dummies(titanic['class'])
y = titanic.survived
X = pd.concat([clas.First, clas.Second, gender.female, titanic.age], axis=1)
X = sm.add_constant(X)
model = sm.Logit(y, X, missing='drop') # some rows contain NaN
result = model.fit()
result.summary()

