#uuuusing gradient in color
from PIL import Image
from images_fcp import *

w,h =700,500
b=[[(0,0,0)for col in range(w)]for row in range(h)]

for row in range(h):
    for col in range(w):
        red=(col*col +2*col*row+row)%256
        green=int((col/(w-1))*255)
        blue=0
        b[row][col]=(red, green, blue)

writeImage(b,"blah3.jpg")
