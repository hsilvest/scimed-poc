# Author: Henrique Silvestre Souza

import cv2
import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy import ndimage

# 255 white
# 0 black

img = cv2.imread('images/14572213-x-ray-image-of-human-healthy-chest-mri.jpg',0)

x,y = img.shape

filtered_img = scipy.misc.imfilter(img,'blur')

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

y = 0
while y < len(thresh2):
	for b in thresh2[y][::-1]:
		if b == 0:
			break
		thresh2[y][::-1][np.where(thresh2[y][::-1] == b)[0][0]] = 0
	y += 1		

plt.imshow(thresh2, cmap=plt.cm.gray)
plt.show()


# for (x,y), value in np.ndenumerate(thresh2):
# 	print '({0},{1}) = {2}'.format(x,y,value)

def center_of_mass(input, labels=None, index=None):
    normalizer = sum(input, labels, index)
    grids = numpy.ogrid[[slice(0, i) for i in input.shape]]

    results = [sum(input * grids[dir].astype(float), labels, index) / normalizer for dir in range(input.ndim)]

    if numpy.isscalar(results[0]):
        return tuple(results)

    return [tuple(v) for v in numpy.array(results).T]
