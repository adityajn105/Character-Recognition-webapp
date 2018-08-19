from flask import Flask, render_template, request, jsonify
import base64
import numpy as np
import cv2
from convnet import predict as predictor
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('app.html',data = {'status':False} ) 

@app.route('/predict', methods = ['POST'])
def predict():
	if request.method == 'POST':
		data = request.get_json()
		imagebase64 = data['image']
		imgbytes = base64.b64decode(imagebase64)
		with open("temp.jpg","wb") as temp:
			temp.write(imgbytes)
		_,img = cv2.threshold(cv2.imread('temp.jpg',0),127,255,0)
		img = cv2.resize(img, (28, 28))
		return jsonify({
        	'prediction': int(predictor(img)),
        	'status': True
    	});