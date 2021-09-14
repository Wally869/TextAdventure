
from typing import Dict
from dataclasses import field

from shortuuid import uuid


class ProviderUUID(object):
    Register: Dict = {}  #field(default_factory=dict)

    @classmethod
    def GetUUID(cls, nodeName: str) -> str:
        if nodeName == "":
            return uuid()
        else:
            if nodeName not in cls.Register.keys():
                cls.Register[nodeName] = 0
            identifier = nodeName + str(cls.Register[nodeName])
            cls.Register[nodeName] = cls.Register[nodeName] + 1
            return identifier


