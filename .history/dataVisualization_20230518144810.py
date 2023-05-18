import numpy as np
import pandas as pd
# %matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import preprocessing
matplotlib.use("QtAgg")


label_encoder = preprocessing.LabelEncoder()




breast_cancer_data = pd.read_csv("./content/data.csv")
head = breast_cancer_data.keys()
coutOfDiagnosisMB = breast_cancer_data['diagnosis'].value_counts() # counts how much are benign and malign cases

info = breast_cancer_data.shape



x=[1,2,3]
y=[5,8,9]
plot = plt.plot(x,y)

# sns.countplot(x="target", data = breast_cancer_data)

# print(plot.show())
