#creating histogram
from matplotlib import pyplot as plt
data=[1,2,3,4,4,3,6,8,3,8,9,4]
plt.hist(data,color='g',bins=3)
print(plt.show())