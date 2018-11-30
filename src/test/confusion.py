
# import sys
# sys.path.append('..')
# print(sys.path)

from SVM import Judge
# from ..SVM import Judge
import os
from os.path import join
from sklearn.metrics import confusion_matrix

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
TRAIN_DIR = join(CURR_DIR, 'pure_training')
TEST_DIR = join(CURR_DIR, 'testing_data')

def loadData(judge, path):
	# borrow function from judge
	tmp = judge.DATA_DIR
	judge.DATA_DIR = path
	x, y = judge.loadData()
	judge.DATA_DIR = tmp

	return x, y



def main():
	judge = Judge(TRAIN_DIR)
	x_test, y_test = loadData(judge, TEST_DIR)
	y_pred = judge.clf.predict(x_test)

	print(confusion_matrix(y_test, y_pred))



if __name__ == '__main__':
	main()