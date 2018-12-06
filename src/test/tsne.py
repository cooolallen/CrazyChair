import numpy as np
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from os.path import join
import os

DATA_DIR = '../../data'

# def loadData(class_id):
# 	filepath = join(DATA_DIR, 'class' + str(class_id) + '.txt')

# 	with open(filepath, 'r') as file:
# 		data = np.asarray([list(map(float,row.strip().split('\t')[1:])) for row in file.readlines()])
	
# 	return data

def loadCompleteData(isBinary=False):
	x, y = [], []
	for filename in os.listdir(DATA_DIR):
		if filename.startswith('class'):
			label = int(filename.split('.')[0][-1])
			with open(join(DATA_DIR, filename), 'r') as file:
				data = [list(map(float,row.strip().split('\t')[1:])) for row in file.readlines()]
				
			x.extend(data)
			y.extend([label] * len(data))

	x = np.asarray(x)
	y = np.asarray(y)

	return x, y

def tsne(x):
	pca = PCA(n_components=2)
	return pca.fit(x).transform(x)
	# return TSNE(n_components=2).fit_transform(x)
	


def main():
	# dic = {}
	colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
	target_names = ['empty', 'normal', 'normal back', 'lay', 'leg on left', 'left on right']
	# for class_id in range(6):
	# 	x = loadData(class_id)
	# 	dic[class_id] = tsne(x)

	# for class_id in range(6):
	# 	data = dic[class_id]
	# 	print(data.shape)
	# 	plt.scatter(data[:, 0], data[:, 1], c=color[class_id], label=str(class_id))

	# plt.legend(loc='best')
	# plt.show()


	X, y = loadCompleteData()
	lda = LinearDiscriminantAnalysis(n_components=2)
	X_r2 = lda.fit(X, y).transform(X)

	for color, i, target_name in zip(colors, list(range(6)), target_names):
		plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=.8, color=color, label=target_name)

	plt.legend(loc='best')
	plt.show()

if __name__ == '__main__':
	main()