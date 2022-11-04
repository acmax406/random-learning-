#image resizer
from PIL import Image
import numpy as np
#importing the file
img=Image.open("xi.jpg")
img1=img.copy()
#printing the value of A*B
print(img1.size)
#tanking input from the user
C=int(input("C-->"))
D=int(input("D-->"))
#resizing the image
img2=img1.resize((C,D))
print(img2.size)