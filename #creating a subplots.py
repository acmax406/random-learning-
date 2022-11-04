#creating a subplots
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y1=2*x
y2=3*x
plt.subplot(1,2,1)
plt.plot(x,y1, color='r', linestyle=':',linewidth='3')
plt.subplot(1,2,2)
plt.plot(x,y2, color='g',linewidth='3')
plt.grid(True)
print(plt.show())
