#uuusing gradient in color
from PIL import Image
from images_fcp import *

image=Image.open("xi.jpg")
w,h =700,500
b=[[(0,0,0)for col in range(w)]for row in range(h)]
#creating the color which is use for blending to the image
for row in range(h):
    for col in range(w):
        red=(2*col-row)%256
        green=int((col/(w-1))*255)
        blue=(col*col + row*row)%256
        b[row][col]=(red, green, blue)

writeImage(b,"x.jpg")
alpha= x.resize(image.size)
image.putalpha(alpha)
image.save("blue.jpg")