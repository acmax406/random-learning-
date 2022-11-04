#jointPlot
import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt 
ac=pd.read_csv("ddata.csv")
print(ac.head())
sns.jointplot(x='sepal.length',y='petal.length',data=ac,)
print(plt.show())