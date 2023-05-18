import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()




breast_cancer_data = pd.read_csv("./content/data.csv")
head = breast_cancer_data.keys()
coutOfDiagnosis = breast_cancer_data['diagnosis'].value_counts()
coutOfDiagnosisM     = breast_cancer_data['diagnosis'].value_counts()

info = breast_cancer_data.shape





# sns.countplot(x="target", data = breast_cancer_data)

print(info)
