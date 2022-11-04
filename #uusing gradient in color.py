#uusing gradient in color
from PIL import Image
from images_fcp import *

w,h =700,500
b=[[(0,0,0)for col in range(w)]for row in range(h)]

for row in range(h):
    for col in range(w):
        red=0
        green=0
        blue=int((col/(w-1))*255)
        b[row][col]=(red, green, blue)

writeImage(b,"blah1.jpg")
