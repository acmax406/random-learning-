#violin plot
#box plot
from matplotlib import pyplot as plt
one=[2,3,4,5,6,6,7,3,4,6]
two=[34,5,6,44,56,34,75,34,5,6]
three=[4,34,22,24,64,65,34,34,6,9]
data=list([one,two,three])
plt.violinplot(data)
print(plt.show())