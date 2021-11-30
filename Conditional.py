from typing import Callable

from StateController import StateController as state  

from BaseNode import BaseNode


class BaseConditionalFunction(object):
    def Check(self) -> bool:
        pass


class ComparisonConditionalFunction(object):
    def __init__(self, var1: str, var2: str, comparisonSign: str):
        self.kVar1 = var1
        self.kVar2 = var2
        self.kComparisonSign = comparisonSign
    
    def __str__(self) -> str:
        return "state.Get('" + str(self.kVar1) + "') " + self.kComparisonSign + " state.Get('" + str(self.kVar2) + "')"

    def Stringify(self) -> str:
        return str(self)

    def Execute(self) -> bool:
        return eval(self.Stringify())




class BaseConditional(BaseNode):
    def __init__(self, nodeName: str, conditionalFunction: BaseConditionalFunction, falseNode: BaseNode, trueNode: BaseNode):
        super().__init__(nodeName)
        self.kConditionalFunction = conditionalFunction
        self.kFalseNode = falseNode
        self.kTrueNode = trueNode

    def Execute(self):
        if self.kConditionalFunction.Execute():
            return self.kTrueNode
        else:
            return self.kFalseNode



from TextSegment import SingleTextNode

state.Set("a", 4)
state.Set("b", 3)

cond = ComparisonConditionalFunction("a", "b", ">")
nodeConditional = BaseConditional("", cond, SingleTextNode("", "henlo", None), SingleTextNode("", "henlololo", None))


#commandsConditional = ComparisonConditionalFunction("command", "allowed_commands", "in")


"""
state.Set("allowed_commands", ["banana", "phone"])
while True:
    state.Set("command", input(""))
    if (commandsConditional.Execute()):
        break        
    
"""





