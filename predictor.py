from sklearn.linear_model import LinearRegression
from sklearn import svm
from tools import parseScorecard, getMatchesOfType
import os
import numpy as np
import cPickle

T20List = getMatchesOfType("T20")
ODIList = getMatchesOfType("ODI")
T20_data = []
T20_final_score = []
T20_final_wkts = []
ODI_data = []
ODI_final_score = []
ODI_final_wkts = []

for file in T20List:
	scorecard, total, wkts = parseScorecard(file)
	print "Looking into " + file
	for i in scorecard:
		T20_data.append([i, scorecard[i][0], scorecard[i][1]])
		T20_final_score.append(total)
		T20_final_wkts.append(wkts)


X = np.array(T20_data)
y = np.array(T20_final_score)
z = np.array(T20_final_wkts)
reg = LinearRegression()
reg.fit(X,y)

clf = svm.SVC()
clf.fit(X,z)

os.chdir("/home/maulik/Desktop/projects/Score Predictor/dump")
with open('T20_classifier.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)    

with open('T20_regression.pkl', 'wb') as fid:
    cPickle.dump(reg, fid)

for file in ODIList:
	scorecard, total, wkts = parseScorecard(file)
	print "Looking into " + file
	for i in scorecard:
		ODI_data.append([i, scorecard[i][0], scorecard[i][1]])
		ODI_final_score.append(total)
		ODI_final_wkts.append(wkts)

X = np.array(ODI_data)
y = np.array(ODI_final_score)
z = np.array(ODI_final_wkts)

reg = LinearRegression()
reg.fit(X,y)

clf = svm.SVC()
clf.fit(X,z)

with open('ODI_classifier.pkl', 'wb') as fid:
    cPickle.dump(clf, fid)    

with open('ODI_regression.pkl', 'wb') as fid:
    cPickle.dump(reg, fid)


