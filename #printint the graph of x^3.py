#printint the graph of x^3
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(-100,100)
y=x*x*x
plt.plot(x,y, color='r', linestyle=':', linewidth="2")
plt.plot(-x,y, color='y', linestyle=':', linewidth="2")
plt.plot(-x,-y, color='g', linestyle=':', linewidth="2")
plt.grid(True)
plt.xlabel="x-axis"
plt.ylabel="y-axis"
print(plt.show())