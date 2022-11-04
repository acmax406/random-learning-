import pandas as pd
import seaborn as sns 
from matplotlib import pyplot as plt 

ac=pd.read_csv("churn.csv")
sns.boxplot(x='InternetService',y='tenure',data=ac,palette='Set1',hue='PaymentMethod')
plt.show()