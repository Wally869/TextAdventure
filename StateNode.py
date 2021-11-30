from typing import List

from dataclasses import dataclass, field 

from StateController import StateController 

from BaseNode import BaseNode


class StateNode(BaseNode):
    def __init__(self, nodeName: str, targetField: str, value: any):
        super().__init__(nodeName)
        self.kTargetField: str = targetField
        self.kTargetValue: any = value

    def Execute(self):
        StateController.Set(self.kTargetField, self.kTargetValue)

