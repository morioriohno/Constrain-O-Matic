# Constrain-O-Matic
### Constrain an unlimited number of objects with the push of a button
This is a tool made for Maya Python that allows you to execute multiple constraints on unlimited objects with just a few clicks. This is most useful for riggers or animators who want a faster way to constrain multiple objects, rather than repeating the same command over and over until their hands cramp. I got the idea for this tool when I was working on rigging a spaceship: the exhaust flaps each required a separate control and joint to move them. By making a rough first draft of this script, I was able to attach roughly 60 pieces of geometry to corresponding joints and controls with just a few clicks.

## Installation
To install, drop the Constrain-O-Matic python script into your script folder:
  - Linux:     *$HOME/maya/scripts*
  - Mac OS:    *$HOME/Library/Preferences/Autodesk/maya/scripts*
  - Windows:   *\Users\<username>\Documents\maya\scripts*
  
Then run this python code in Maya by dragging it into the script editor:
```
import ConstrainOMatic as COM
COM.ConstrainOMatic()
```
You can create a button from this code by to bring up the Constrain-O-Matic UI quickly. To do so, select the code in the script editor and middle-mouse-button drag it to your rigging shelf.

## Demo
You can find a demo video with simple examples [here](https://youtu.be/i1Z3zXnMAiM). There is also a transcript file within the download folder, titled "Demo Transcript.md". 

## How It Works
The Constrain-O-Matic uses a set of filter strings to take objects in a selection and separate them into two lists: a parent list and a child list. Using those lists, the tool then checks which types of constraints you've selected, does an extensive error check, and executes one of two functions: ***One For All*** and ***One By One***.

### One For All
***One For All*** takes a single parent object and repeats a constraint with as many child objects as you want. For example, maybe you want one FK control to rotate all the joints of a tail at once. By running ***One For All*** with an Orient constraint, you attach each joint to the control in the exact same way, saving yourself the annoying process of manually creating each constraint. If you were to select all the objects at once and run a regular constraint command instead of running it through the Constrain-O-Matic, you would instead create a single constraint with multiple parents. Below is an example of how this would work:

```
If the parent filter string is "_CTL" and the child filter string is "_JNT",
selecting these 5 objects will yield this result.

PARENT         CHILDREN
--------       ----------
tail_CTL ----> tail01_JNT
         ----> tail02_JNT
         ----> tail03_JNT
         ----> tail04_JNT
```

This function doesn't require any sort of matching naming scheme, so long as the filter strings are still retrieving the proper objects.

### One By One
***One By One*** allows you to connect objects that "match" in name. Rather than only using a single parent object, the tool makes sure that an equal number of objects populate both lists, and then alphabetizes the lists. Once alphabetized, the Constrain-O-Matic grabs one object from each list and constrains them, then moves to the next object in each list, and continues until all matching objects are paired. For example, say you want to rig a robot's mechanical hand through constraints. With all the separate fingers, it would be a lot of work to replicate a parent and scale constraint for each joint of each finger. With the Constrain-O-Matic, it can be done in a few short steps, as detailed below:

```
If the parent filter string is "_JNT" and the child filter string is "_GEO",
selecting these 14 objects will yield this result, regardless of selection order.

PARENT              CHILD
------------        ------------
index_01_JNT  ----> index_01_GEO
index_02_JNT  ----> index_02_GEO
index_03_JNT  ----> index_03_GEO
middle_01_JNT ----> middle_01_GEO
middle_02_JNT ----> middle_02_GEO
middle_03_JNT ----> middle_03_GEO
wrist_JNT     ----> wrist_GEO
```
The same function can then be repeated on the same joints and their matching controls:

```
If the parent filter string is "_CTL" and the child filter string is "_JNT",
selecting these 14 objects will yield this result, regardless of selection order.

PARENT              CHILD
------------        ------------
index_01_CTL  ----> index_01_JNT
index_02_CTL  ----> index_02_JNT
index_03_CTL  ----> index_03_JNT
middle_01_CTL ----> middle_01_JNT
middle_02_CTL ----> middle_02_JNT
middle_03_CTL ----> middle_03_JNT
wrist_CTL     ----> wrist_JNT
```
A consistent naming scheme is crucial for ***One By One*** to work. Without it, objects can be connected in unpredictable ways that will make a rigger's job harder, not easier. However, you can rest easy if you make a mistake. All Constrain-O-Matic commands are undoable. 

Happy rigging to all! Please don't hesitate to reach out with any feedback or questions.
## 
