from typing import Dict



class NodesRecorder(object):
    Records: Dict = {}

    @classmethod
    def Set(cls, uuid: str, node: "BaseNode"):
        cls.Records[uuid] = node

    @classmethod
    def Get(cls, uuid: str) -> "BaseNode":
        return cls.Records[uuid]

