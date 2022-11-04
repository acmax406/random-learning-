#importing pokemon file
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
pokemon=pd.read_csv('pokemon.csv')
print(pokemon.head())