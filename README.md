# Constrain-O-Matic
### Constrain an unlimited number of objects with the push of a button
This is a tool made for Maya Python that allows you to execute multiple constraints on unlimited objects with just a few clicks. This is most useful for riggers or animators who want a faster way to constrain multiple objects, rather than repeating the same command over and over until their hands cramp.

## Installation
To install, drop the Constrain-O-Matic python script into your script folder:
  - Linux:     *$HOME/maya/scripts*
  - Mac OS:    *$HOME/Library/Preferences/Autodesk/maya/scripts*
  - Windows:   *\Users\<username>\Documents\maya\scripts*
  
Then run this python code in Maya:
```
import ConstrainOMatic as COM
COM.ConstrainOMatic()
```
You can create a button from this code to bring up the Constrain-O-Matic UI quickly.

## How It Works
Constrain-O-Matic uses a set of filter strings to take objects in a selection and separate them into two lists: a parent list and a child list. Using those lists, the tool then checks which types of constraints you've selected, checks that nothing is getting double-constrained, and executes one of two functions.

### One For All
***One For All*** takes a single parent object and repeats a constraint with as many child objects as you want. For example, maybe you want one FK control to rotate all the joints of a tail at once. By running One For All with an Orient constraint, you attach each joint to the control in the exact same way, saving an annoying process of manually iterating each constraint. If you were to select all the objects at once and run a regular constraint command instead of running it through the Constrain-O-Matic, you would instead create a single constraint with multiple parents.

```
If the parent filter string is "_CTL" and the child filter string is "_JNT",
selecting these 5 objects will yield this result.

PARENT         CHILDREN
tail_CTL ----> tail01_JNT
         ----> tail02_JNT
         ----> tail03_JNT
         ----> tail04_JNT
```

This function doesn't require any sort of matching naming scheme, so long as the filter strings are still retrieving the proper objects.

### One By One
***One By One*** allows you to connect objects that "match" in name. Rather than only using a single parent object, the tool makes sure that an equal number of objects populate both lists, and then alphabetises the lists. Once alphabetized, the Constrain-O-Matic grabs one object from each list and constrains them, then moves to the next object in each list, and continues until all matching objects are paired. For example, say you want to rig a robot's mechanical hand through constraints. With all the separate fingers, it would be a lot of work to replicate a parent and scale constraint for each joint of each finger. With the Constrain-O-Matic, it can be done in a few short steps.

```
If the parent filter string is "_JNT" and the child filter string is "_GEO",
selecting these 14 objects will yield this result, regardless of selection order.

PARENT              CHILD
index_01_JNT  ----> index_01_GEO
index_02_JNT  ----> index_02_GEO
index_03_JNT  ----> index_03_GEO
middle_01_JNT ----> middle_01_GEO
middle_02_JNT ----> middle_02_GEO
middle_03_JNT ----> middle_03_GEO
wrist_JNT     ----> wrist_GEO
```
The same function can then be repeated on the same joints and their matching controls.

```
If the parent filter string is "_CTL" and the child filter string is "_JNT",
selecting these 14 objects will yield this result, regardless of selection order.

PARENT              CHILD
index_01_CTL  ----> index_01_JNT
index_02_CTL  ----> index_02_JNT
index_03_CTL  ----> index_03_JNT
middle_01_CTL ----> middle_01_JNT
middle_02_CTL ----> middle_02_JNT
middle_03_CTL ----> middle_03_JNT
wrist_CTL     ----> wrist_JNT
```
A consistent naming scheme is crucial for One By One to work. Without it, objects can be connected in unpredictable ways that will make a rigger's job harder, not easier.

## 
