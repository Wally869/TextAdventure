

from BaseNode import BaseNode
from TextSegment import TextSegment
from InteractiveSegment import InteractiveNode
from Conditional import ComparisonConditionalFunction, BaseConditional

from StateController import StateController as state



end = [
    "This is it, this is the end.\n\n",
    "TO BE CONTINUED"

]

end = TextSegment("end", end, None)





t0_raw = [
    "...What's going on?",
    "As you come back to your senses, you realise something's not right.",
    "Prodding your memories, you distinctly remember going for a stroll along the river, enjoying the warm rays of a late summer afternoon.",
    "But now... Somehow, someway, it looks you just woke up sprawled on the floor inside a cold, dark room.",
    "You carefully get up and take a look at your surroundings.",
    "With the lack of light, you can barely see the outlines of a door and a switch. What's going on? What should I do?"

]

intro = TextSegment("intro", t0_raw, end)


currNode = intro
while currNode != None:
    currNode = currNode.Execute()






