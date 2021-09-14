# TextAdventure   
Simple Text Adventure Engine in Python   

This is a learning experiment. For now, only a basic story has been written in a functional fashion, engine development hasn't been started yet.    


## Development  
We start by creating a demo story in a naive way, to get a first feel as to what problems we'll face in developing our 

Demo Story:  
You wake in room, is dark. Only see door and a switch. Door is locked, can use switch. Switch turns on light. There is locker in the room and a steel bar on the ground. Steel bar is pickable. Can open locker. Inside: key, which opens the door. When you open the door, the game ends.    

Run "python naive.py" to try the demo story.  


## Improvements on naive.py  
- Create a static class for state management.  
We'll be splitting code between files so we need something cleaner than global variable declarations.  
- Create a class for consecutive text segments.   
Impractical and very error prone to set text like this. Better to potentially use an external data source of something  
 


