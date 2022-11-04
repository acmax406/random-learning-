#creating subolot of x^3 and x^2
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(-1000,1000)
y1=x*x
y2=x*x*x
plt.subplot(1,2,1)
plt.plot(x,y1, color= 'r', linewidth='2')
plt.title("mathematical graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(x,y2, color='b',linewidth='2')
#attributes
plt.title("mathematical graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
print(plt.show())