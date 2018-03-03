import json

def extract_path(response) :
	#data = json.load(open('response.json'))
	#n = json.dumps(m)
	data = json.loads(response)
	re = data["resourceSets"]
	re1 = re[0]["resources"]
	re2 = re1[0]["routeLegs"]
	re3 = re2[0]["itineraryItems"]
	path = ""
	for i,item in enumerate(re3):
		path += (str(i) +"."+ item["instruction"]["text"]+ "\n")

	return path

with open('response.json', 'r') as myfile:
	res = myfile.read().replace("\n","")
	print extract_path(res)
