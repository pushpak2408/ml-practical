# -*- coding: utf-8 -*-
"""polinomial regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NUmJLnG2siCKgsWX5POb6KaH4pVGuR9w
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

mca=pd.read_csv('https://raw.githubusercontent.com/apratim777/apratim777/refs/heads/master/Position_Salaries.csv')
mca

plt.xlabel('Level')
plt.ylabel('Salary')
plt.scatter(mca.Level,mca.Salary)

x=mca.drop(['Position','Salary'],axis=1)
x

y=mca.Salary
y

reg=linear_model.LinearRegression()

reg.fit(x,y)

reg.score(x,y)

plt.xlabel('Level')
plt.ylabel('Salary')
plt.scatter(mca.Position,mca.Salary)
plt.plot(x,reg.predict(x))

from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=4)

x_poly=poly.fit_transform(x)
x_poly

lin2=linear_model.LinearRegression()

lin2.fit(x_poly,y)

lin2.predict(x_poly)

lin2.score(x_poly,y)

plt.scatter(x,y)
plt.plot(x,reg.predict(x))

plt.scatter(x,y)
plt.plot(x,lin2.predict(x_poly))

lin2.predict(x_poly)

reg.predict(x)
