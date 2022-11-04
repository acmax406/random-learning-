#pairplot===drawing
import pandas as pd 
import seaborn as sns 
from matplotlib import pyplot as plt

ac=sns.load_dataset('iris')
sns.pairplot(ac,hue='species')
plt.show()