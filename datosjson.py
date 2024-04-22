import json
with open("parsing/myfile.json","r") as files:
	ourjson = json.load(file)
print (ourjson)
