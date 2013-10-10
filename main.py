# Author: Henrique Silvestre Souza

import cv2
import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy import ndimage

# 255 white
# 0 black

img = cv2.imread('images/image.jpg',0)

x,y = img.shape

filtered_img = scipy.misc.imfilter(img,'blur')

i = 0
while i < int(x * 0.01):
	filtered_img = scipy.misc.imfilter(filtered_img,'blur')
	i += 1

ret,thresh2 = cv2.threshold(filtered_img,127,255,cv2.THRESH_BINARY_INV)

label, qtd = ndimage.label(thresh2)

print "(X:%i,Y:%i)" % ndimage.measurements.center_of_mass(thresh2, label)
print qtd

i = 0
while i < x:
	for b in thresh2[i]:
		if b == 0:
			break
		thresh2[i][np.where(thresh2[i] == b)[0][0]] = 0
	i += 1

i = 0
while i < len(thresh2):
	for b in thresh2[i][::-1]:
		if b == 0:
			break
		thresh2[i][::-1][np.where(thresh2[i][::-1] == b)[0][0]] = 0
	i += 1		

plt.imshow(thresh2, cmap=plt.cm.gray)
plt.show()
