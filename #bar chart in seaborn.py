#bar chart in seaborn
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
ac=pd.read_csv("gh.csv")
print(ac.head())
sns.set(style='whitegrid')
sns.barplot(x='stunum',y='avg',data=ac,hue='gen',palette='Blues_d')
#hue=takes the values of a array for the color encoding
#palette=gives the different shades of color for the bars
print(plt.show())