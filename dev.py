

from TextSegment import TextSegment
from StateNode import StateNode


from StateController import StateController as state



state.Set("has_key", False)
state.Set("has_steel_bar", False)
state.Set("is_locker_open", False)
state.Set("is_light_lit", False)
state.Set('is_locker_open', False)


t0_raw = [
    "...What's going on?",
    "As you come back to your senses, you realise something's not right.",
    "Prodding your memories, you distinctly remember going for a stroll along the river, enjoying the warm rays of a late summer afternoon.",
    "But now... Somehow, someway, it looks you just woke up sprawled on the floor inside a cold, dark room.",
    "You carefully get up and take a look at your surroundings.",
    "With the lack of light, you can barely see the outlines of a door and a switch. What's going on? What should I do?"

]

t0 = TextSegment("t0", t0_raw, None)
t0.Execute()

print("\n")

#allowedCommands = ["door", "switch"]
StateNode("cmds", "allowed_commands", ["door", "switch"]).Execute()
command = ""
while True:  #command not in allowedCommands:
    print(state.Get("allowed_commands"))
    command = input("").lower()
    if command not in state.Get("allowed_commands"):
        continue
    if command == "door":
        input("You try to turn the handle to no avail: the door is locked...")
    elif command == "switch":
        input("The lights turn on and blind you temporarily.")
        #state.Set("is_light_lit", True)
        StateNode("light", "is_light_lit", True).Execute()
        break  
    print("\n")


input("The details of the room are now visible: apart from the door, you can see a boarded window, a few school tables and a locker.")
print("\n")  

StateNode("cmds", "allowed_commands", ["look", "door", "window", "locker"]).Execute()
command = ""
while True:  #command not in allowedCommands:
    print(state.Get("allowed_commands"))
    command = input("").lower()
    if command not in state.Get("allowed_commands"):
        continue
    if command == "look":
        if not state.Get("has_steel_bar"):
            input("It seems you are in some sort of classroom. You can see a locker as well as a few school tables. Looking closely, you can see a steel bar under one of the tables.")
            state.AddAllowedCommand("steelbar")
        else:
            input("It seems you are in some sort of classroom. You can see a locker as well as a few school tables.")
    elif command == "door":
        if state.Get("has_key"):
            input("Using the key you picked up, you manage to unlock the door. The door opens and you take a step outside the room...")
            print("\n\nTO BE CONTINUED\n")
            break
        else:
            input("You try to turn the handle to no avail: the door is locked...")
    elif command == "window":
        input("The window is all boarded up.")
    elif command == "locker":
        if state.Get("is_locker_open"):
            input("There's nothing left in the locker.")
        else:
            input("You approach the locker and try to turn the handle. It creaks a little, but the door opens just fine.")
            input("Inside the locker, you find a key which you promptly pick up.")
            state.Set("has_key", True)
            state.Set("is_locker_open", True)
    elif command == "steelbar":
        input("You pick up the steelbar.")
        state.Set("has_steel_bar", True)
        state.RemoveAllowedCommand("steelbar")
    print("\n")




