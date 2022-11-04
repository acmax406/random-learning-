#blurImage
from PIL import Image, ImageFilter
import os

image1= Image.open("img1.jfif")
image1.filter(ImageFilter.GaussianBlur()).save('imgblur.jpg')
#to increase the blurness we haave to  increase in value GaussianBlur() 