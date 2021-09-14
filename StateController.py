from typing import Dict

from StringifyDriver import BaseStringifyDriver

class StateController(object):
    State: Dict = {}
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
