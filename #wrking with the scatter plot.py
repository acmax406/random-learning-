#wrking with the scatter plot
import pandas as pd 
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt 
ac=pd.read_csv('covid.csv')
print(ac.head())
x=np.arange(1,152866)
sns.lineplot(x,y='New_deaths',data=ac,hue='Country')
print(plt.show())