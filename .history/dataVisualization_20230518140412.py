import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


breast_cancer_data = pd.read_csv("data.csv")
head = breast_cancer_data.keys()


# sns.countplot(x="target", data = breast_cancer_data)

print(breast_cancer_data)
