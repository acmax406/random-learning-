#convert to numpy format
from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np

image=Image.open("img1.jpg")

#to show only the image
#image.show()
#to show the image with ruler
plt.imshow(image)
print(plt.show())
#convertin to the numpy array
numpy_array=np.array(image)
print(numpy_array.shape)
#coverting numpy array to image
numpy_image=Image.fromarray(numpy_array)
plt.imshow(numpy_array)