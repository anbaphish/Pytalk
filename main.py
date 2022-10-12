#Proof of con JSON capable
import random
import json

with open('sample.json') as json_file:
   data = json.load(json_file) #loads JSON, use data as rep

speak = (f"I think " + random.choice(data["topics"]) + ' is ' + random.choice(data["adj"]) )   
print(speak)

#with open("sample.json", "w") as outfile:
#    json.dump(words, outfile)
  #opening a dictionary and dumping is best for JSON in format