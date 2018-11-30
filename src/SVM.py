from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
# from sklearn.preprocessing import normalize
import Constants

import numpy as np
from os.path import join
import os

class Judge(object):
	def __init__(self, DATA_DIR):
		self.clf = None
		self.DATA_DIR = DATA_DIR
		self.initialize()

	def loadData(self):
		def normalize(data):
			# to prevent the dvide by zeros
			up = (data - np.expand_dims(data.mean(axis=1), axis=1))
			down = np.expand_dims(data.std(axis=1), axis=1)

			return np.divide(up, down, out=np.zeros_like(up), where=down!=0)

		x, y = [], []
		for filename in os.listdir(self.DATA_DIR):
			if filename.startswith('class'):
				label = int(filename.split('.')[0][-1])
				with open(join(self.DATA_DIR, filename), 'r') as file:
					data = [list(map(float,row.strip().split('\t')[1:])) for row in file.readlines()]
					
				x.extend(data)
				y.extend([label] * len(data))

		return normalize(np.asarray(x)), np.asarray(y)

	def initialize(self):
		x, y = self.loadData()
		# check is there any data for training
		if x.size == 0:
			print('no data detect, please record data point')
			return

		clf = OneVsRestClassifier(LinearSVC(random_state=42, max_iter=3000, dual=False))
		clf.fit(x, y)
		self.clf = clf

	def predict(self, measure):
		# return 0 if clf is not ready
		if self.clf is None:
			return 0

		x = np.asarray([measure])
		return self.clf.predict(x)[0]
		