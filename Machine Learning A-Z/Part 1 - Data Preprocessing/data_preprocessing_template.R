# Data Preprocessing Template

# You can Set any folder you want as working directory
#   as long as the directory has the data (.csv)

# Importing the dataset
dataset = read.csv('Data.csv')

# In R, index starts at 1 instead of 0

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$DependentVariable, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

# Feature Scaling 
# training_set = scale(training_set)
# test_set = scale(test_set) 