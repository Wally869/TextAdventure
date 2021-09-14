

from BaseNode import BaseNode


class BaseInstruction(object):
    pass



class TextInstruction(BaseInstruction):
    pass


class NavigationInstruction(BaseInstruction):
    def __init__(self, targetNode: BaseNode):
        targetNode.Run()
