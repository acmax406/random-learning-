#implementing the style in seaborn linechart
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
ac=sns.load_dataset('fmri')
print(ac.head())
sns.lineplot(x="timepoint",y="signal",data=ac,hue='event',style='event')
print(plt.show())
sns.lineplot(x='timepoint',y='signal',data=ac,style='event',markers=True)
print(plt.show())