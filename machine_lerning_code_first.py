# -*- coding: utf-8 -*-
"""MACHINE LERNING CODE FIRST.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oaatEni-NaBGi8kMw3hKYgb_0_9UUhKd
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# %matplotlib inline
import tensorflow as tfwait
from tensorflow import keras

(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()

len(x_test)

len(x_train)

x_train[0].shape# 0 element check the train deta shape

x_train[0]

plt.matshow(x_train[1])

plt.matshow(x_train[0])

y_train[0]

x_train=x_train/255
x_test=x_test/255

x_train[0]

x_train_flattened=x_train.reshape(len(x_train),28*28)
x_test_flattened=x_test.reshape(len(x_test),28*28)

x_train_flattened.shape

x_train_flattened[0]

x_train_flattened[0].shape

len(y_test)

len(y_train)

"""## very simple neural network with no hidden layers"""

from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train_flattened, y_train, epochs=5)

model.evaluate(x_test_flattened,y_test)

"""### using hidden layer"""

from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(100,input_shape=(784,),activation='relu'),
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train_flattened, y_train, epochs=5)

model.evaluate(x_test_flattened,y_test)

from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(100,input_shape=(784,),activation='relu'),
    keras.layers.Dense(100,input_shape=(784,),activation='relu'),
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train_flattened, y_train, epochs=5)

model=keras.Sequential([
    keras.layers.Dense(100,input_shape=(784,),activation='relu'),
    keras.layers.Dense(50,input_shape=(784,),activation='sigmoid'),
    keras.layers.Dense(10,activation='sigmoid')

])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train_flattened,y_train,epochs=5)

y_predicted=model.predict(x_test_flattened)
y_predicted[0]

np.argmax(y_predicted[0])

plt.matshow(x_test[4])

np.argmax(y_predicted[4])

y_predicted_labels=[np.argmax(i) for i in y_predicted]

cm=tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels)
cm

import seaborn as sn
plt.figure(figsize=(7,5))
sn.heatmap(cm,annot=True,fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

""" ## Small image classification"""

import tensorflow as tf
from tensorflow.keras import datasets,layers,models
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
x_train.shape

y_train.shape

y_train[:5]

y_train=y_train.reshape(-1,)
y_train = y_train.flatten()
y_train[:5]

y_test = y_test.reshape(-1)

classes=["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

def plot_sample(x,y,index):
    plt.figure(figsize=(15,2))
    plt.imshow(x[index])
    plt.xlabel(classes[y[index]])

plot_sample(x_train,y_train,20)

x_train=x_train/255
x_test=x_test/255

"""build simple artificial neural  network for image classification"""

ann=models.Sequential([
    layers.Flatten(input_shape=(32,32,3)),
    layers.Dense(3000,activation='relu'),
    layers.Dense(1000,activation='relu'),
    layers.Dense(10,activation='sigmoid')
])
ann.compile(optimizer='SGD',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
ann.fit(x_train,y_train,epochs=3)

from sklearn.metrics import confusion_matrix,classification_report
import numpy as np
y_pred=ann.predict(x_test)
y_pred_classes=[np.argmax(element) for element in y_pred]