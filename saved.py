import cPickle
import sys

matchType = raw_input("Enter the format. T20 or ODI?")
if matchType == "T20":
	with open('dump/T20_classifier.pkl', 'rb') as fid:
	    clf = cPickle.load(fid)
	with open('dump/T20_regression.pkl', 'rb') as fid:
	    reg = cPickle.load(fid)
elif matchType == "ODI":
	with open('dump/ODI_classifier.pkl', 'rb') as fid:
	    clf = cPickle.load(fid)
	with open('dump/ODI_regression.pkl', 'rb') as fid:
	    reg = cPickle.load(fid)
else:
	print "Invalid format" 
	sys.exit(0)

overs = input("Enter no. of overs:")
runs = input("Enter no. of runs:")
wkts = input("Enter no. of wickets:")
overs = str(overs).split(".")
if len(overs) > 1:
	balls = int(overs[0])*6 + overs[1]
else:
	balls = int(overs[0])*6
test = [balls, runs, wkts]
pred = reg.predict(test)
if pred - int(pred) >= 0.5:
	pred = int(pred)+1
else:
	pred =  int(pred)

print str(pred) + " runs for " + str(clf.predict(test)[0]) + " wickets!"