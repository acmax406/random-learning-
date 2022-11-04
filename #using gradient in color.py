#using gradient in color
from PIL import Image
from images_fcp import *

w,h =500,500
b=[[(0,0,0)for col in range(w)]for row in range(h)]

for row in range(h):
    for col in range(w):
        red=int(255*row/499)
        green=(1024+row-col)%256
        blue=(row+col)%256
        b[row][col]=(red, green, blue)

writeImage(b,"blah.jpg")
