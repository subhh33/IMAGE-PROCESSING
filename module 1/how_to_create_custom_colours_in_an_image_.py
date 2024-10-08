# -*- coding: utf-8 -*-
"""How to create custom colours in an Image?.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RrbjaydZWme7ANRv2qlBAhQFoSZJZ7FX
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

"""# Creating Custom Colour"""

arr = np.array([[[ 249  , 220 , 104 ] , [ 55  , 126 , 34 ] ,[ 90  , 0 , 0 ]],
                [[ 139  , 206 , 247 ] , [ 239 , 134 , 59 ] ,[ 180 , 0 , 0 ]],
                [[ 113  , 178 , 229 ] , [ 240 , 0 , 0 ] ,[ 255 , 0 , 0 ]]])

plt.imshow(arr)

"""# Creating Dense Image"""

img = []

for i in range(720):
    t = []
    for j in range(1080):
        t.append([ 239 , 134 , 59])
    img.append(t)

img = np.array(img)

plt.imshow(img)

"""# **bold text**"""

cv.imwrite('Orange.png',img)

img = []

for i in range(720):
    t = []
    for j in range(1080):
        t.append([ 59 , 134 , 239])
    img.append(t)

img = np.array(img)

plt.imshow(img)

cv.imwrite('Orange_1.png',img)

