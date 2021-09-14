from typing import List

from dataclasses import dataclass, field 

from BaseNode import BaseNode


class SingleTextNode(BaseNode):
    def __init__(self, nodeName: str == "", text: str, destinationNode: BaseNode):
        super().__init__(nodeName)
        self.mTextElement = text
        self.mDestinationNode = destinationNode

    def Execute(self) -> BaseNode:
        input(self.mTextElement)
        #destinationNode.Run()
        return self.mDestinationNode


class TextSegment(BaseNode):
    def __init__(self, segmentName: str, texts: List[SingleTextNode], destinationNode: BaseNode):
        super().__init__(segmentName)
        self.mSegmentName = segmentName
        self.mTextElements = []
        for i in range(len(texts) - 1, -1, -1):
            if i == len(texts) - 1:
                destination = destinationNode
            else:
                destination = self.mTextElements[-1]
            self.mTextElements.append(SingleTextNode("", texts[i], destination))
        self.mTextElements = self.mTextElements[::-1]
        self.mDestinationNode = destinationNode

    def Execute(self) -> BaseNode:
        """
        for elem in self.mTextElements:
            input(elem)
        return self.mDestinationNode
        """
        for node in self.mTextElements[:-1]:
            node.Execute()
        return self.mTextElements[-1].Execute()


