# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:41:26 2017

@author: BALASUBRAMANIAM
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
#from scipy.misc import imread, imsave
#from scipy import ndimage
from scipy import misc
sys.path.append("C:/Users/BALASUBRAMANIAM/Pictures/")
#image_data = imread('C:/Users/BALASUBRAMANIAM/Pictures/carrot.jpg')
image_data  = misc.face(gray=True)
import matplotlib.pyplot as plt

plt.imshow(image_data, cmap=plt.cm.gray)   
plt.imshow(image_data, cmap=plt.cm.gray, vmin=30, vmax=200)
print(image_data)
#from skimage.color import rgb2gray
#gray_image = rgb2gray(image_data)

#show_images(images=[image_data,gray_image],titles=["Color","Grayscale"])
print ("Colored image shape:", image_data.shape)
#print ("Grayscale image shape:", gray_image.shape)

print ('Size: ', image_data.size)
print ('Shape: ', image_data.shape)
scaled_image_data = image_data / 255
blurred_face = ndimage.gaussian_filter(scaled_image_data, sigma=3)
very_blurred = ndimage.gaussian_filter(scaled_image_data, sigma=5)
#Save the modified image if you want to

plt.imshow(ndimage.rotate(scaled_image_data, 45))
imsave('tiltedimage.png', ndimage.rotate(scaled_image_data, 45))
plt.show()


scaled_image_data.clip(50,10)
#Save the modified image if you want to


imsave('test_out.png', scaled_image_data)
plt.imshow(scaled_image_data[100:])
plt.show()
imsave('test_out.png', scaled_image_data)
