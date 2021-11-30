from typing import List

from StateController import StateController as state

from UUID import ProviderUUID

from NodesRecorder import NodesRecorder


class BaseNode(object):
    def __init__(self, nodeName: str):
        self.mNodeName = ProviderUUID.GetUUID(nodeName)
        NodesRecorder.Set(self.mNodeName, self)
        self.kDestinationNode = None

    def Execute(self):
        pass
    
    def SetDestinationNode(self, destinationNode: 'BaseNode'):
        self.kDestinationNode = destinationNode

