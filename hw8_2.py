import pandas as pd
from numpy.random import randint
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('diabetes_data.csv')
corr = df.corr()
sns.heatmap(corr.abs(), annot=True, annot_kws={"size": 8})
plt.show()
