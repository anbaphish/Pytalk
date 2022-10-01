#basic proof of concept
import random
words = { 
    "adj": ["good", "sad", "boring", "loud", "fun"],
    "topics": ["school", "math", "sciene", "work", "exercise", "music"]
}



#adj = words["adj"]
#topics = words["topics"]


speak = "I think", random.choice(words["topics"]), " is ", random.choice(words["adj"])
print(speak)
    
def randchoice(topic) : 
    random.choice(list(words.topic()))
    return
  
  #needs more work
