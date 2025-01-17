# -*- coding: utf-8 -*-
"""Machine Learning Bootcamp Demo

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/155iMMdkz1WNcsyQtFhpDxYMDXSzNh8-M
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
path = "/content/drive/MyDrive/Dataset/Iris.csv"
df = pd.read_csv(path)
x = df.drop(columns=["Species"])
y =df["Species"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = DecisionTreeClassifier(max_depth=3)
model.fit(x_train, y_train)
model.score(x_test, y_test)