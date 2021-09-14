from typing import List, Tuple


from BaseNode import BaseNode
from StateController import StateController as state



class InteractiveNode(object):
    def __init__(self, commandMappings: List[Tuple[str, BaseNode]]):  # tuple of command and node
        self.kCommandMappings = commandMappings

    def Run(self):
        state.Set("allowed_commands", {mapping[0]: mapping[1] for mapping in self.kCommandMappings})
        while True:
            print(list(state.Get("allowed_commands").keys()))
            state.Set("command", input())
            if state.Get("command") in state.Get("allowed_commands").keys():
                state.Get("allowed_commands")[state.Get("command")].Execute()


            


