#basic proof of concept
import random
words = { 
    "adj": ["good", "sad", "boring", "loud", "fun"],
    "topics": ["school", "math", "sciene", "work", "exercise", "music"]
}



#adj = words["adj"]
#topics = words["topics"]

def main():
    speak = "I think" + randchoice(adj) + " is " + randchoice(topics)
    print(speak)
    
def randchoice(topic) : 
    random.choice(list(words.topic()))
    return
  
  #needs more work
