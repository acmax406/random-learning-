#image inhancement
from PIL import ImageEnhance
from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np

image=Image.open("img1.jpg")

#copying the image
imgcopy=image.copy()
#enhancement(increasing color)
img1=ImageEnhance.Color(imgcopy).enhance(10)
plt.imshow(img1)
plt.show()
#enhancement(increasing contrst)
img2=ImageEnhance.Contrast(imgcopy).enhance(5)
plt.imshow(img2)
plt.show()
#enhancement (incresing brightness)
img3=ImageEnhance.Brightness(imgcopy).enhance(5)
plt.imshow(img2)
plt.show()
#enhancement of the sharpness of he image
img4=ImageEnhance.Sharpness(imgcopy).enhance(5)
plt.imshow(img4)
plt.show()