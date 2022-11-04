#blending two images together
from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np

#alpha blending
#formula--> \
#out=image1*(1.0-alpha)+imge2*alpha
#requirements=>>> 1.image of same size and 2. have alpha channel

imagem=Image.open("facem.png")
imagew=Image.open("facew.png")

img1=imagem.copy()
img2=imagew.copy()

#resizing both of equal size

img2=img2.resize(img1.size)
print(img1.size)
print(img2.size)

#blending
image_blend=Image.blend(img1,img2,0.5)
plt.imshow(image_blend)
plt.show()
 