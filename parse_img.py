import json

def get_tag(data) :
	#data = json.loads(str)
	pred = data["Predictions"]
	return pred[0]["Tag"]

def get_prob(data):
	#data = json.loads(str)
	pred = data["Predictions"]
	return float(pred[0]["Probability"])
	

#with open('img_train.json', 'r') as myfile:
#	res = myfile.read().replace("\n","")
#	print get_tag(res)
#	print get_prob(res)
