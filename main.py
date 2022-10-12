#Proof of con JSON capable
import random
import json



with open('sample.json') as json_file:
   data = json.load(json_file) #loads JSON, use data as rep
  
sentSet = [(f"I think " + random.choice(data["topics"]) + ' is ' + random.choice(data["adj"]) ), 
f"I love " + random.choice(data["topics"])
          ]


speak = random.choice(sentSet)
print(speak)

#with open("list.json", "w") as outfile:
 #  json.dump(sentSet, outfile)
  #opening a dictionary and dumping is best for JSON in format
