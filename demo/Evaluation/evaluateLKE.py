#!/usr/bin/env python
from pprint import pprint
from RI_precision import *
from LKE import *
import gc
import numpy as np

result = np.zeros((5,9))

#LKE
#**********************PARAMETERS SETTING**************************************************
# Replace the parameters of def __init__ with the following ones according to the dataset.
# Please be noted that part of the codes in function termpairGene need to be altered according to the dataset
#******************************************************************************************
# =====For BGL=====
# (self,path='../Sca/',dataName='Sca_BGL600',logname='rawlog.log',removable=True,removeCol=[0,1,2,3,4,5,6,7,8,9],threshold2=5,regular=True,
# rex=['core\.[0-9]*'],savePath='./results/',saveFileName='template'):# line 67,change the regular expression replacement code
# =====For Proxifier=====
# (self,path='../Sca/',dataName='Sca_Proxifier600',logname='rawlog.log',removable=True,removeCol=[0,1,2,4,5],regular=True,threshold2=2,
# rex=[''],savePath='./results/',saveFileName='template'):
# =====For Zookeeper=====
# (self,path='../Sca/',dataName='Sca_Zookeeper600',logname='rawlog.log',removable=True,removeCol=[0,1,2,3,4,5,6],threshold2=2,regular=True,
# rex=['(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)'],savePath='./results/',saveFileName='template'):
# =====For HDFS=====
# (self,path='../Sca/',dataName='Sca_SOSP600',logname='rawlog.log',removable=True,removeCol=[0,1,2,3,4,5],threshold2=3,regular=True,
# rex=['blk_(|-)[0-9]+','(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)'],savePath='./results/',saveFileName='template'):
# =====For HPC=====
# (self,path='../Sca/',dataName='Sca_HPC600',logname='rawlog.log',removable=True,removeCol=[0,1],threshold2=4,regular=True,
# rex=['([0-9]+\.){3}[0-9]'],savePath='./results/',saveFileName='template'):# line 67,change the regular expression replacement code
#******************************************************************************************
for i in range(1,6,1):

	dataset = i
	dataPath = '../../data/'

	if dataset == 1:
		dataName = '2kBGL'
		removeCol = [0,1,2,3,4,5,6,7,8,9]
		threshold2=5
		regL = ['core\.[0-9]*']
		# regL = []
	elif dataset == 2:
		dataName = '2kHPC'
		removeCol = [0,1]
		threshold2=4
		regL = ['([0-9]+\.){3}[0-9]']
		# regL = []
	elif dataset == 3:
		dataName = '2kHDFS'
		removeCol = [0,1,2,3,4,5]
		threshold2=3
		regL = ['blk_(|-)[0-9]+','(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']
		# regL = []
	elif dataset == 4:
		dataName = '2kZookeeper'
		removeCol = [0,1,2,3,4,5,6]
		threshold2=2
		regL = ['(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)']
		# regL = []
	elif dataset == 5:
		dataName = '2kProxifier'
		removeCol = [0,1,2,4,5]
		threshold2=2
		regL = []

	print ('the ', i, 'th experiment starts here!')
	parserPara = Para(path=dataPath, dataName=dataName, threshold2=threshold2, removeCol=removeCol, rex=regL, savePath='./results/')
	myParser = LKE(parserPara, dataset=i)
	runningTime = myParser.mainProcess()

	parameters=prePara(groundTruthDataPath=dataPath+dataName+'/', geneDataPath='./results/')

	TP,FP,TN,FN,p,r,f,RI=process(parameters)
	result[i-1,:]=TP,FP,TN,FN,p,r,f,RI,runningTime

	gc.collect()

pprint(result)
np.savetxt("LKE.out", result, fmt="%10.10f")
