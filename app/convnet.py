from keras.models import load_model
from keras import backend
import numpy as np

def getModel():
	return load_model('saved_model/model_cnn_1.h5')

def predict(img):
	test = (255-img.reshape(1,28,28,1).astype('float32'))/255
	onehot = getModel().predict(test)
	backend.clear_session()
	return np.argmax(onehot)
