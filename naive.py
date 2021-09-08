

HAS_KEY = False
HAS_STEEL_BAR = False

IS_LOCKER_OPEN = False

input("...What's going on?")

input("As you come back to your senses, you realise something's not right.")

input("Prodding your memories, you distinctly remember going for a stroll along the river, enjoying the warm rays of a late summer afternoon.")


input("But now... Somehow, someway, it looks you just woke up sprawled on the floor inside a cold, dark room.")
input("You carefully get up and take a look at your surroundings.")
input("With the lack of light, you can barely see the outlines of a door and a switch. What's going on? What should I do?")
#print("[Door], [Switch]\n")

print("\n")

allowedCommands = ["door", "switch"]
command = ""
while True:  #command not in allowedCommands:
    print(allowedCommands)
    command = input("").lower()
    if command not in allowedCommands:
        continue
    if command == "door":
        input("You try to turn the handle to no avail: the door is locked...")
    elif command == "switch":
        input("The lights turn on and blind you temporarily.")
        break  
    print("\n")


input("The details of the room are now visible: apart from the door, you can see a boarded window, a few school tables and a locker.")
print("\n")  

allowedCommands = ["look", "door", "window", "locker"]
command = ""
while True:  #command not in allowedCommands:
    print(allowedCommands)
    command = input("").lower()
    if command not in allowedCommands:
        continue
    if command == "look":
        if not HAS_STEEL_BAR:
            input("It seems you are in some sort of classroom. You can see a locker as well as a few school tables. Looking closely, you can see a steel bar under one of the tables.")
            if "steelbar" not in allowedCommands:
                allowedCommands.append("steelbar")
        else:
            input("It seems you are in some sort of classroom. You can see a locker as well as a few school tables.")
    elif command == "door":
        if HAS_KEY:
            input("The door unlocks. You open it and step outside the room...")
            print("\n\nTO BE CONTINUED\n")
            break
        else:
            input("You try to turn the handle to no avail: the door is locked...")
    elif command == "window":
        input("The window is all boarded up.")
    elif command == "locker":
        if IS_LOCKER_OPEN:
            input("There's nothing left in the locker.")
        else:
            input("You approach the locker and try to turn the handle. It creaks a little, but the door opens just fine.")
            input("Inside the locker, you find a key which you promptly pick up.")
            HAS_KEY = True
    elif command == "steelbar":
        input("You pick up the steelbar.")
        HAS_STEEL_BAR = True
        allowedCommands.remove("steelbar")
    print("\n")




