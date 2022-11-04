from sklearn import datasets
import pandas as pd
iris =datasets.load_iris()
df=pd.DataFrame(iris.data)
print(df) 