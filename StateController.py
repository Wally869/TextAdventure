from typing import Dict, List

from StringifyDriver import BaseStringifyDriver

class StateController(object):
    State: List = {"allowed_commands": []}
    Stringifier: BaseStringifyDriver

    @classmethod
    def GetState(cls) -> Dict:
        return cls.State

    @classmethod
    def Set(cls, key, value):
        cls.State[key] = value
    
    @classmethod
    def Get(cls, key):
        return cls.State[key]

    @classmethod
    def IsIn(cls, key):
        return key in cls.State.keys()

    @classmethod
    def Append(cls, key, value):
        cls.State[key].append(value)

    @classmethod
    def AddAllowedCommand(cls, value):
        if (value not in cls.State["allowed_commands"]):
            cls.State["allowed_commands"].append(value)
    
    @classmethod
    def RemoveAllowedCommand(cls, value):
        if (value in cls.State["allowed_commands"]):
            cls.State["allowed_commands"].remove(value)
