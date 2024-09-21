# -*- coding: utf-8 -*-
"""extract frames from an Image.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rTWQ8gmzM5H_5GBamrThN4IQc_tUYCYL
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



img = cv.imread('Transition.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)

img.shape

"""# R G B"""

img[:1000,:,:].shape

plt.imshow(img[:1000,:,:])

plt.imshow(img[:500,:,:])

plt.imshow(img[:500,:1000,:])

img = cv.imread('rgb.jpeg')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

img[:,:,:].shape

plt.imshow(img)

plt.imshow(img[200:,:,:])

plt.imshow(img[:,100:,:])

img = cv.imread('Transition.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)

r = img[ :  , : , 0 ]  # - Red
g = img[ :  , : , 1 ]  # - Green
b = img[ :  , : , 2 ]  # - Blue

plt.imshow(r)

plt.imshow(b)

plt.imshow(g)

cv.imwrite('Blue_t.jpg',b)
cv.imwrite('Red_t.jpg',r)
cv.imwrite('Green_t.jpg',g)





