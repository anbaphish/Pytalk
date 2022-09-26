# Pytalk
The goal is to allow a user to practice speaking and responding in a timely manner to questions or statements.

Reason: I often look back on my converstaions and realize I could have said things in a much better or humorus way and get left with some regret. 

------Design plan ----

A user runs the python program and can set a maximum time. Then once set the program will spit a out a random sentence and the user has to verbally make a response within the time. It's to help people who're bad at speaking or coming up with responses to practice such things. 

The random sentences are generated with prebuilt sentence structues, and with keywords being replaced with a type such as a noun or verb, and when stating the sentence it simply grabs a random word from a list of them and puts it into that. An example output:

"I've been practicing {hobby}, it's pretty {adjective} but can be {adjective}"


hobby could be something like bass, computers, running, photography, lifting, ect

adjective could be bad, good, loud, ect


Further broken down specific lists can be used as well if the usecase is large enough. 

The user is meant to verbally respond as they're practicing but they aren't forced into doing stuff as it's simply just text and whatnot.


-----------  goals ------------

[] Use random system to generate and output text with timer
[] Setup GUI to allow a user to add stuff
[] Universal formatting to allow custom wordlists and sentences
[] Set up app version so people can practice on phone
[] App version feature allows the user to make a commitment to actually speaking aloud with microphone incase they feel they might cheat
