
from typing import Union

from NodesRecorder import NodesRecorder

from BaseNode import BaseNode


class BaseNavigationNode(BaseNode):
    def __init__(self, nodeName: str = ""):
        super().__init__(nodeName)


class NavigationNode(BaseNavigationNode):
    def __init__(self, nodeName: str = "", targetNode: Union[str, BaseNode] = ""):
        super().__init__(nodeName)
        
        if (isInstance(targetNode, BaseNavigationNode):
            self.kTargetNode = targetNode
        else:
            self.kTargetNode = NodesRecorder.Get(targetNode)

    
