# Data Preprocessing

# Importing the libraries
import numpy as np                  # numpy is the library that contains mathematical tools
import matplotlib.pyplot as plt     # help plot charts
import pandas as pd                 # import data sets and manage data sets

# 1. Importing the dataset
dataset = pd.read_csv('Data.csv' )
dataset = pd.read_csv('Data.csv')

# 2. Need to determine the data feature (Independent data) and the dependent variables
X_feature = dataset.iloc[:, :-1].values     # symbol : means we take all the rows, and all the columns except the last one.
Y_dependent = dataset.iloc[:, 3].values

# Tip: ‘NaN’ has to be replaced by ‘np.nan’. This is due to an update in the sklearn library.

# Taking care of missing data
#  scikit-learn : machine learning library in python
# sklearn.preprocessing.Imputer: help process missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# # Splitting the dataset into the Training set and Test set
# from sklearn.cross_validation import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
#
# # Feature Scaling
# """from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)
# sc_y = StandardScaler()
# y_train = sc_y.fit_transform(y_train)"""