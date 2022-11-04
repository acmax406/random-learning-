#creating subplots of scatter
#creation of a scatter plot
from matplotlib import pyplot as plt
x=[10,20,30,40,50,60]
y=[1,2,4,6,7,6]
y1=[3,5,6,3,7,1]
plt.subplot(1,2,1)#row,column,first
plt.scatter(x,y, marker="+",c='r',s=100)
plt.subplot(1,2,2)#ow,column,second
plt.scatter(x,y1, marker="+",c='b',s=100)
print(plt.show())  