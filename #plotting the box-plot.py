#plotting the box-plot
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt 

ac=pd.read_csv("churn.csv")
print(ac.head())