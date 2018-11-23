#!/usr/bin/env python
from pprint import pprint
from RI_precision import *
from LogSig import *
import gc
import numpy as np

result = np.zeros((5,9))

for i in range(1,6,1):

	dataset = i
	dataPath = '../../data/'

	if dataset == 1:
		dataName = '2kBGL'
		groupNum = 100
		removeCol = [0,1,2,3,4,5,6,7,8,9]
		regL = ['core\.[0-9]*']
		# regL = []
	elif dataset == 2:
		dataName = '2kHPC'
		groupNum = 51
		removeCol = [0,1]
		regL = ['([0-9]+\.){3}[0-9]']
		# regL = []
	elif dataset == 3:
		dataName = '2kHDFS'
		groupNum = 14
		removeCol = [0,1,2,3,4,5]
		regL = ['blk_(|-)[0-9]+','(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']
		# regL = []
	elif dataset == 4:
		dataName = '2kZookeeper'
		groupNum = 46
		removeCol = [0,1,2,3,4,5,6]
		regL = ['(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']
		# regL = []
	elif dataset == 5:
		dataName = '2kProxifier'
		groupNum = 6
		removeCol = [0,1,2,4,5]
		regL = []

	print ('the ', i, 'th experiment starts here!')
	parserPara = Para(path=dataPath+dataName+'/', groupNum=groupNum, removeCol=removeCol, rex=regL, savePath='./results/'+dataName+'/')
	myParser = LogSig(parserPara, dataset=i)
	runningTime = myParser.mainProcess()

	parameters=prePara(groundTruthDataPath=dataPath+dataName+'/', geneDataPath='./results/'+dataName+'/')

	TP,FP,TN,FN,p,r,f,RI=process(parameters)
	result[i-1,:]=TP,FP,TN,FN,p,r,f,RI,runningTime

	gc.collect()

pprint(result)
np.savetxt("LogSig.out", result, fmt="%10.10f")
