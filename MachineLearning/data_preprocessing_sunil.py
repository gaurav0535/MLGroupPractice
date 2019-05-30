#Import Library
import numpy as np
np.set_printoptions(threshold=100)
import matplotlib.pyplot as plt
import pandas as pd # import and manage datasets

#Import Dataset and create dependent and independent variables
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values # -1 - > take all the cols except the last one
Y = dataset.iloc[:,3].values 


#Splitting into Training set and test set
# y_train -> training part of the dependent variable
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2
                                                    ,random_state = 0)
#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
