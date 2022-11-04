#creating a donught chart
from matplotlib import pyplot as plt
fruit=['apple','orange','mango','guavava']
quantity=[25,67,34,78]
plt.pie(quantity,labels=fruit,radius=1)
plt.pie([1],colors=['w'],radius=0.5)
print(plt.show())