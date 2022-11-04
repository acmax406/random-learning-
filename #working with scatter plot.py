#working with scatter plot
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
print(df.head())
sns.scatterplot(x='AAPL_x',y="AAPL_y",data=df,hue='AAPL_x')
print(plt.show())