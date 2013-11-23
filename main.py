# Author: Henrique Silvestre Souza
import sys
import cv2
import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy import ndimage
import os
from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	url_for('static', filename='style.css')
	return render_template('index.html', name="teste")


if __name__ == '__main__':
	app.debug = True
	app.run()

def image_detect(file):
	# 255 white
	# 0 black

	# for filename in os.listdir('images'):
	# img = cv2.imread('images/'+filename,0)
	img = file
	new_img = cv2.resize(img,(600,700))

	x,y = img.shape

	filtered_img = scipy.misc.imfilter(img,'blur')


	i = 0
	while i < int(x * 0.01):
		filtered_img = scipy.misc.imfilter(filtered_img,'blur')
		i += 1

	equalizated_img = cv2.equalizeHist(filtered_img)

	ret,thresh2 = cv2.threshold(equalizated_img,127,255,cv2.THRESH_BINARY_INV)

	label, qtd = ndimage.label(thresh2)

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

	# print filename + "- (X:%i,Y:%i)" % ndimage.measurements.center_of_mass(thresh2, label)
	# print qtd

	# plt.imshow(thresh2, cmap=plt.cm.gray)
	# plt.show()


