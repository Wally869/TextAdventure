

from BaseNode import BaseNode

from StateController import StateController as state


class BaseInstruction(object):
    pass



class TextInstruction(BaseInstruction):
    pass


class NavigationInstruction(BaseInstruction):
    def __init__(self, targetNode: BaseNode):
        targetNode.Run()


class AddAllowedCommand(BaseInstruction):
    def __init__(self, command: str, target: BaseNode):
        state.AddAllowedCommand(command, target)
