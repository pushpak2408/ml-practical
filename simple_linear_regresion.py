# -*- coding: utf-8 -*-
"""simple linear regresion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R_-xa9sneT5X0NjDuIUpHgZpV1jkFBiW
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

mca=pd.read_csv('https://raw.githubusercontent.com/apratim777/apratim777/refs/heads/master/homeprices.csv')
mca

plt.xlabel('area')
plt.ylabel('price')
plt.scatter(mca.area,mca.price,color='red',marker='+')

mca.price

new_x=mca.drop('price',axis=1)
new_x

new_y=mca.drop('area',axis=1)
new_y

reg=linear_model.LinearRegression()

reg.fit(new_x,new_y)

reg.predict([[2600]])

reg.score(new_x,new_y)

