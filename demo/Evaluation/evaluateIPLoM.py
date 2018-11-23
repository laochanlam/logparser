#!/usr/bin/env python
from pprint import pprint
from RI_precision import *
from IPLoM import *
import gc
import numpy as np

result = np.zeros((5,9))

for i in range(1,6,1):

	dataset = i
	dataPath = '../../data/'

	if dataset == 1:
		dataName = '2kBGL'
		ct = 0.4
		lowerBound = 0.01
		removeCol = [0,1,2,3,4,5,6,7,8]
  		regL = ['core\.[0-9]*']

	elif dataset == 2:
		dataName = '2kHPC'
		ct = 0.175
		lowerBound = 0.25
		removeCol = [0]
		regL = ['([0-9]+\.){3}[0-9]']

	elif dataset == 3:
		dataName = '2kHDFS'
		ct = 0.35
		lowerBound = 0.25
		removeCol = [0, 1, 2, 3, 4]
		regL = ['blk_(|-)[0-9]+','(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']

	elif dataset == 4:
		dataName = '2kZookeeper'
		ct = 0.4
		lowerBound = 0.7
		removeCol = [0, 1, 2, 3, 4, 5]
		regL = ['(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']

	elif dataset == 5:
		dataName = '2kProxifier'
		ct = 0.6
		lowerBound = 0.25
		removeCol = [0, 1, 3, 4]
  		regL = []

	print ('the ', i, 'th experiment starts here!')
	parserPara = Para(path=dataPath+dataName+'/', CT=ct, lowerBound=lowerBound,
	                  removeCol=removeCol, rex=regL, savePath='./results/')
	myParser = IPLoM(parserPara, dataset=i)
	runningTime = myParser.mainProcess() 

	parameters=prePara(groundTruthDataPath=dataPath+dataName+'/', geneDataPath='./results/')

	TP,FP,TN,FN,p,r,f,RI=process(parameters)
	result[i-1,:]=TP,FP,TN,FN,p,r,f,RI,runningTime

	gc.collect()

pprint(result)
np.savetxt("IPLoM.out", result, fmt="%10.10f")
