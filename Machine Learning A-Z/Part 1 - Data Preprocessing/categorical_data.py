# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1. Importing the dataset
df = pd.read_csv('Data.csv' )

# 2. Need to determine the data feature (Independent data) and the dependent variables
X_feature = df.iloc[:, :-1].values     # symbol : means we take all the rows, and all the columns except the last one.
Y_dependent = df.iloc[:, 3].values

# 3. Taking care of missing data
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values = np.nan, strategy='mean')
# make the imputer fit on X_feature
imp = imp.fit(X_feature[:, 1:3])  # Upper bound is excluded, so index 1 and 2 columns are included
#Replace the missing data of the matrix X_feature by the mean of the column
X_feature[:, 1:3] = imp.transform(X_feature[:, 1:3])

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X_feature[:, 0] = labelencoder_X.fit_transform(X_feature[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X_feature).toarray()
# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
Y_dependent = labelencoder_y.fit_transform(Y_dependent)
