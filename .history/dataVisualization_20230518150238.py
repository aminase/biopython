import numpy as np
import pandas as pd
# %matplotlib inline

import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import preprocessing
label_encode = preprocessing.LabelEncoder()

breast_cancer_data = pd.read_csv("./content/data.csv")


labels = label_encode.fit_transform(breast_cancer_data['diagnosis'])
breast_cancer_data['diagnosis'] = labels




head = breast_cancer_data.keys()
coutOfDiagnosisMB = breast_cancer_data['diagnosis'].value_counts() # counts how much are benign and malign cases
print(coutOfDiagnosisMB)


'''x =[1,2,3]
y=[5,8,9]
plot = plt.plot(x,y)
plt.show()
'''


'''sns.countplot( data = coutOfDiagnosisMB)
plt.show()'''



# print(plot.show())
