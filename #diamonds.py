#diamonds
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt
ac=pd.read_csv('ddata.csv')
print(ac.head())
plt.subplot(1,3,1)
sns.scatterplot(x='sepal.length',y='petal.length',data=ac)
plt.subplot(1,3,2)
sns.scatterplot(x='sepal.length',y='petal.length',data=ac,hue='variety')
plt.subplot(1,3,3)
sns.scatterplot(x='sepal.length',y='petal.length',data=ac,hue='petal.length')
print(plt.show())