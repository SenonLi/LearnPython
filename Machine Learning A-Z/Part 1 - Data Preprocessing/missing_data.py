# Data Preprocessing

# Importing the libraries
# import matplotlib.pyplot as plt
#  library pandas offers data structures and operations for manipulating numerical tables and time series
import numpy as np
import pandas as pd

# Importing the dataset
df = pd.read_csv('Data.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, 3].values

# Taking care of missing data
from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imp = imp.fit(X[:, 1:3])
X[:, 1:3] = imp.transform(X[:, 1:3])

# GroupBy of DataFrame test
# dfGroup = df.groupby('Purchased')
# for Purchased in dfGroup:
#     print(Purchased)

