# -*- coding: utf-8 -*-
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

def compare_values(num1,num2):
	if num1 >= num2:
		return num1 - num2
	else:
		return num2 - num1

def image_detect(file):
	# 255 white
	# 0 black
	img = cv2.imread(file, 0)
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

	val_x,val_y = ndimage.measurements.center_of_mass(thresh2, label)

	resultado = int(compare_values(val_x,val_y))

	print resultado

	if resultado >= 100:
		return render_template('index.html', diag = 'Patologia Detectada'.decode('utf8'))
	else:
		return render_template('index.html', diag = 'Patologia Não Detectada'.decode('utf8'))

	#return "(X:%i,Y:%i)" % ndimage.measurements.center_of_mass(thresh2, label)
	# print qtd

	# plt.imshow(thresh2, cmap=plt.cm.gray)
	# plt.show()

@app.route('/')
def hello_world():
	return render_template('index.html', name="teste")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
       	f.save(app.root_path + '/db/' + f.filename)
       	return image_detect(app.root_path + '/db/' + f.filename)

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)


