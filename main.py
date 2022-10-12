#basic proof of concept
import random
words = { 
    "adj": ["good","sad","boring","loud","fun"],
    "topics": ["school","math","sciene","work","exercise","music"]
}



#adj = words["adj"]
#topics = words["topics"]


speak = (f"I think " + random.choice(words["topics"]) + ' is ' + random.choice(words["adj"]))
print(speak)
    

  
  #needs more work
