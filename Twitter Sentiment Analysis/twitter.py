import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#use ctrl+I for more info on a feature and see in help

#IMPORTING THE DATASET
train_dataset = pd.read_csv('0000000000002747_training_twitter_x_y_train.csv')
X = train_dataset.iloc[:,:].values 

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:,1] = labelencoder_X.fit_transform(X[:,1])
print(X[:,1])
X_test = pd.read_csv('0000000000002747_test_twitter_x_test.csv')  

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
#classifier.fit(X_train, y_train)

import keras