# TextAdventure   
Simple Text Adventure Engine in Python   

This is a learning experiment. For now, only a basic story has been written in a purely declarative fashion, I'm creating dataclasses and a state manager for a cleaner approach to the problem and to allow transpiling to common interactive adventure formats (such as Inky).  

## Thoughts  

Need to make a distinction on what to handle:  
- seperate rooms interconnected, explore, get items. More actions become available with time, so it's closer to puzzle solving      
- seperate scenes with a story flow, more novel than exploration  

The two aspects can go together, but there are some differences. Try to keep in mind, think can manage both.  

## Development  
We start by creating a demo story in a naive way, to get a first feel as to what problems we'll face in developing our 

Demo Story:  
You wake in room, is dark. Only see door and a switch. Door is locked, can use switch. Switch turns on light. There is locker in the room and a steel bar on the ground. Steel bar is pickable. Can open locker. Inside: key, which opens the door. When you open the door, the game ends.    

Run "python naive.py" to try the demo story.  

The file "dev.py" contains the rewritten story. It's a work in progress using dataclasses for ease of serialization and to handle logic more cleanly. Still very messy, I'm not working on this very actively.  


## Improvements on naive.py  
- Create a static class for state management.  
We'll be splitting code between files so we need something cleaner than global variable declarations.  
- Create a class for consecutive text segments.   
Impractical and very error prone to set text like this. Better to potentially use an external data source of something  
 


