import yaml
import os

def parseScorecard(file):
	os.chdir("/home/maulik/Desktop/projects/Score Predictor/all")
	with open(file, 'r') as f:
		doc = yaml.load(f)
	f.close()
	inn1 = doc["innings"][0]["1st innings"]["deliveries"]
	scorecard = {}
	cumRuns = cumWkts = cumBalls = 0
	for i in inn1:
		for j in i:
			total = i[j]["runs"]["total"]
			extras = i[j]["runs"]["extras"]
			cumRuns += total
			try:
				if i[j]["wicket"] is not None:
					cumWkts += 1
			except:
				pass
			if extras > 0:
				extra = i[j]["extras"]
				flag=0
				for extraType in extra:
					if extraType == "wides" or extraType == "noballs":
						flag=1
						break
				if flag:
					continue
			cumBalls += 1
			scorecard[cumBalls] = [cumRuns, cumWkts]

	return scorecard, cumRuns, cumWkts

def getMatchesOfType(matchType):
	with open('all/matches.txt', 'r') as f:
		data = f.readlines()
	f.close()
	matchList = []
	for i in data:
		x = i.split("-")[3]
		if x.lstrip().rstrip() == matchType:
			matchList.append(i.split("-")[4].lstrip().rstrip() + ".yaml")
	return matchList

def matchType(file):
	with open(file, 'r') as f:
		doc = yaml.load(f)
	f.close()
	info = doc["info"]["match_type"]
	return info
