import termcolor
import random
key = 0
challenge = 0
locker = 0
pool = 0
validInput = False
intro = "Today you and your dad decided to go to a swimming pool. From seeing reviews online, you are excited to jump off the diving board. \n You and your father rush out to the pool after changing and you start climbing. Nearing the top, you start feeling sick and tell \n your dad that you have to go to the bathroom. You then rush into the building hoping to buy some time."
help = "The only valid commands are north, east, south, west, help, yes and no."
falseDirection = "I don't recognize that command."
challengeVerified = "You have moved to the next stage and completed the challenge successfully!"
center = "You are standing in the center of the building"
lockerRoom = "You find yourself in a locker room with no exit except where you came from"
directionDenied = "You can not go this way."
directionDeniedColor = (directionDenied,'red')
lockerRoomColor = termcolor.colored(lockerRoom,'green')
challengeVerifiedColor = termcolor.colored(challengeVerified, 'green')
helpColor = termcolor.colored(help,'yellow')
introColor = termcolor.colored(intro, 'green')
falseDirectionColor = termcolor.colored(falseDirection, 'red')
centerColor = termcolor.colored(center, "green")


print (introColor)
while validInput == False:
    command = input("Type a direction to move. \n Valid directions are north, south, east and west: ")
    if "help" in command.lower():
        helpColor = termcolor.colored(help,'yellow')
        print (helpColor)
    if "north" in command.lower():
        Exit = input("You are at an exit. Do you want to leave to the next stage? Remember that your dad will be disappointed if you did not conquer your fear and jump from the diving board [yes]/[no]: ")
        if "yes" in Exit.lower():
            if challenge == 1:
                print (challengeVerifiedColor)
                validInput = True
            else: 
                print ("You cannot move on without completing the challenge")
        else: 
            print (center)
    elif "south" in command.lower():
        pool = 0
        while pool < 1:
            if "north" in command.lower():
                print (center)
            elif "south" in command.lower(): 
                if key >= 1:
                    jump = input("You are standing in front of the diving board. Would you like to jump? [yes]/[no]")
                    if "yes" in jump.lower():
                        print ("Congrats you have successfully jumped from the diving board!")
                        challenge += 1
                        pool += 1
                if key == 0:
                    print ("Hmm... This door seems to be locked, maybe try looking in another direction for a key")
                    pool += 1
            elif "help" in command.lower():
                print (help)
            else:
                print (falseDirectionColor)

    elif "east" in command.lower():
        prepared = input("Welcome to the key machine! In order to acquire the key you need to get to the pool, you must guess the number from 1 to 3 that I am thinking of! Ready? [yes]/[no]: ")
        if "yes" in prepared.lower():
            while key == 0:
                keyguess = int(input("Guess a number from 1 to 3: "))
                number = random.randint(1,3)
                if number == keyguess:
                    print ("nice work! you got the key!")
                    key += 1
                elif number != keyguess:
                    print ("try again!")
                else:
                    print (falseDirectionColor)
        if "no" in prepared.lower():
            print (center)
    elif "west" in command.lower():
        locker == 0
        print (lockerRoom)
        while locker == 0:
            command = input("Type a direction to move. \n Valid directions are north, south, east and west: ")
            if "north" in command.lower():
                print (directionDeniedColor)
            elif "south" in command.lower():
                print (directionDeniedColor)
            elif "east" in command.lower():
                print (center)
                locker +=1
            elif "west" in command.lower():
                print (directionDeniedColor)
            elif "help" in command.lower():
                print (help)
            else:
                print (falseDirectionColor)