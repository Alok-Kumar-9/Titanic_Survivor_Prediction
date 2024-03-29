# -*- coding: utf-8 -*-
"""titanic_survivor_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLuHDY77GYtrxlO9St81AtLH929D1k54
"""

# Commented out IPython magic to ensure Python compatibility.
from sklearn.base import MetaEstimatorMixin
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn import tree

df = pd.read_csv('/content/titanic_dataset.csv')
df.head()

X = df.drop(['PassengerId','Survived', 'Name', 'SibSp', 'Parch', 'Ticket','Cabin', 'Embarked'],axis='columns')
Y = df['Survived']

X

Y

le1 = LabelEncoder()
X['Gender'] = le1.fit_transform(X['Sex'])
X

X = X.drop(['Sex'],axis='columns')
X

rr = np.mean(df['Age'])
rr

X.fillna(value={'Age':rr},axis='rows',inplace=True)

X

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = tree.DecisionTreeClassifier()

model.fit(X_train, Y_train)

predicted = model.predict(X_test)
predicted

from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test , predicted)
acc

cm = confusion_matrix(Y_test , predicted)
cm

plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True)
plt.xlabel('Predicted Values')
plt.ylabel('Real Values')

