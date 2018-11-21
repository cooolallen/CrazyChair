from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
import Constants

import numpy as np
from os.path import join
import os



class Judge(object):
	def __init__(self):
		self.clf = None
		self.initialize()

	def loadData(self):
		x, y = [], []
		for filename in os.listdir(Constants.DATA_DIR):
			if filename.startswith('class'):
				label = int(filename.split('.')[0][-1])
				with open(join(Constants.DATA_DIR, filename), 'r') as file:
					data = [list(map(float,row.strip().split('\t')[1:])) for row in file.readlines()]
					
				x.extend(data)
				y.extend([label] * len(data))

		return np.asarray(x), np.asarray(y)

	def initialize(self):
		x, y = self.loadData()
		# check is there any data for training
		if x.size == 0:
			print('no data detect, please record data point')
			return

		clf = OneVsRestClassifier(LinearSVC(random_state=42, max_iter=3000))
		clf.fit(x, y)
		self.clf = clf

	def predict(self, measure):
		# return 0 if clf is not ready
		if self.clf is None:
			return 0

		x = np.asarray([list(map(float, measure.split('\t')))])
		return self.clf.predict(x)[0]
		