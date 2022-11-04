#uusing gradient in color
from PIL import Image
from images_fcp import *

a=readImage("udon.jpg")
w,h =len(a[0]),len(a)

kernel1= [[0,0,0],
          [0,1,0],
          [0,0,0]
          ]

b = convolve(a,kernel1)

writeImage(b,"xi2.jpg")