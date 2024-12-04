# -*- coding: utf-8 -*-
"""digit classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v4LC3g__EUehu59G9s8g-6P3E2fxug-R
"""

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()

dir(digits)

plt.gray()
for i in range(5):
    plt.matshow(digits.images[i])

digits.data[0]

digits.target[1]

digits.data[1796]

digits.target[502]

plt.matshow(digits.images[502])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, train_size=0.2)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(x_train, y_train)

model.score(x_test, y_test)

model.predict(digits.data[[100]])

plt.matshow(digits.images[100])

plt.matshow(digits.images[200])

digits.data[200]

digits.target[100]

digits.target[200]
