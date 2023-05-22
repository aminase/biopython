import numpy as np
import pandas as pd
# %matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import preprocessing
label_encode = preprocessing.LabelEncoder()
breast_cancer_data = pd.read_csv("./data/data.csv")



                                #  Visualizing benign and malign cases from data.csv  
 
'''labels = label_encode.fit_transform(breast_cancer_data['diagnosis'])
breast_cancer_data['target'] = labels                                       # benign = 0; malign = 1
breast_cancer_data.drop(columns = 'diagnosis', axis =1, inplace=True)

coutOfDiagnosisMB = breast_cancer_data['target'].value_counts()             # counts how much are benign and malign cases
print(coutOfDiagnosisMB)

sns.countplot( x="target", data = breast_cancer_data)
plt.show()'''



mainInfo = breast_cancer_data.describe()     # info on count, mean, median(50%), std, min, max throughout columns
# print(mainInfo)





for item in range (2, 10, 2):
    item += 1
    print(item)

