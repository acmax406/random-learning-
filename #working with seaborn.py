#working with seaborn
import seaborn as sns
from matplotlib import pyplot as plt
ac=sns.load_dataset('fmri')
print(ac.head())
sns.lineplot(x="timepoint", y="signal",data=ac,hue='event' )
print(plt.show())