#creation of pie-chart
from matplotlib import pyplot as plt
fruit=['orange','mango','apple','guavava']
quantity=[56,78,89,100]
plt.pie(quantity,labels=fruit,autopct='%0.1f%%',
colors=['orange','yellow','red','green'])
#autopct='%0.1f%% is used to show the
# percentage of each slices
#color attribute use to assign the color to each of the
#slices
print(plt.show())