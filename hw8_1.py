import pandas as pd
from numpy.random import randint
import matplotlib.pyplot as plt
df = pd.read_csv('diabetes_data.csv')

for x in df.columns: 
    plt.scatter(df[x], df.BMI)
    plt.ylabel('BMI', size=15)
    plt.xlabel(x, size=15)
    plt.show()
