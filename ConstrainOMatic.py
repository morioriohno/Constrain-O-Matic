### (C) Copyright Michal Zadok, 2022

### Find my portfolio at www.zadoks.org/~michal
### Email: morioriohno@gmail.com

### Constrain-O-Matic V1.0 (Date: 12/13/2022)
### Created for Maya 2023, run on macOS Monterey (12.6.1)

### This script is meant for riggers or animators who want a faster way to constrain multiple objects, rather than repeating the same command over and over until their hands cramp.
### One For All takes one object as a parent and repeats the constraints you want with as many children as you want it to control.
### One By One alphabetizes your selections and then pairs up objects with matching names (i.e., hand_GEO and hand_JNT) for constraining.

from maya import cmds

class ConstrainOMatic:
    
#############################################################################
###                               UI SETUP                                ###
#############################################################################
    
    def __init__(self):

        ### SECTION 1: INITIALIZE WINDOW ###
        
        self.wind = "Constrain-O-Matic (V1.0)"
        if cmds.window(self.wind, exists=1) == 1 :
            cmds.deleteUI(self.wind)
        self.win = cmds.window("Constrain-O-Matic (V1.0)", widthHeight=(400,490), s=0)
        cmds.columnLayout(cal='center')
        cmds.separator(height=10, width=400, style='none')
        
        ### SECTION 2: USER INSTRUCTIONS ###
        
        cmds.rowLayout(numberOfColumns=3)
        cmds.separator(width=30, hr=0, style='none')
        cmds.text(label="Select all objects you want to connect. Input a string to mark parents and a string to mark children. Choose which constraints you want to run and then press the button for your selected mode.", w=330, ww=1, align='center')
        cmds.setParent("..")
        
        cmds.separator(height=10, width=400, style='none')
        
        cmds.rowLayout(numberOfColumns=3)
        cmds.separator(width=25, hr=0, style='none')
        cmds.text(label="Make sure objects that you want to constrain are numbered or named to match. The script alphabetizes your selection to match parents to children.", w=340, ww=1, align='center', fn="boldLabelFont")
        cmds.setParent("..")
        
        # double-lined separator
        cmds.separator(height=10, width=400, style='none')
        cmds.separator(height=5, width=400, style='in')
        cmds.separator(height=5, width=400, style='in')
        cmds.separator(height=10, width=400, style='none')
  
        ### SECTION 3: FILTER STRING SETUP ###
        
        cmds.rowLayout(numberOfColumns=3)
        cmds.separator(width=15, hr=0, style='none')
        cmds.text(label="Parent String:",align='left', w=80)
        self.pInput = cmds.textField(w=280)
        cmds.setParent("..")

        cmds.rowLayout(numberOfColumns=3)
        cmds.separator(width=15, hr=0, style='none')
        cmds.text(label="Child String:",align='left', w=80)
        self.cInput = cmds.textField(w=280)
        cmds.setParent("..")
        
        # double-lined separator
        cmds.separator(height=10, width=400, style='none')
        cmds.separator(height=5, width=400, style='in')
        cmds.separator(height=5, width=400, style='in')
        cmds.separator(height=2, width=400, style='none')
        
        ### SECTION 4: ENABLE AND OPTION CHECKBOX SETUP ###
        
        # parent setup
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        self.paEn = cmds.checkBox(label='Parent', w=85, v=0, cc=self.paToggle)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        self.paTraX = cmds.checkBox(label='TraX', w=50, v=1, en=0)
        self.paTraY = cmds.checkBox(label='TraY', w=50, v=1, en=0)
        self.paTraZ = cmds.checkBox(label='TraZ', w=70, v=1, en=0)
        self.paMo = cmds.checkBox(label='Maintain Offset', v=1, en=0)
        cmds.setParent("..")
        
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        cmds.checkBox(label='Parent', w=85, vis=0)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        self.paRotX = cmds.checkBox(label='RotX', w=50, v=1, en=0)
        self.paRotY = cmds.checkBox(label='RotY', w=50, v=1, en=0)
        self.paRotZ = cmds.checkBox(label='RotZ', w=70, v=1, en=0)
        cmds.setParent("..")
        
        cmds.separator(height=10, width=400, style='in')

        # point setup
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        self.ptEn = cmds.checkBox(label='Point', w=85, v=0, cc=self.ptToggle)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        self.ptX = cmds.checkBox(label='X', w=50, v=1, en=0)
        self.ptY = cmds.checkBox(label='Y', w=50, v=1, en=0)
        self.ptZ = cmds.checkBox(label='Z', w=70, v=1, en=0)
        self.ptMo = cmds.checkBox(label='Maintain Offset', v=1, en=0)
        cmds.setParent("..")

        cmds.separator(height=10, width=400, style='in')

        # orient setup
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        self.orEn = cmds.checkBox(label='Orient', w=85, v=0, cc=self.orToggle)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        self.orX = cmds.checkBox(label='X', w=50, v=1, en=0)
        self.orY = cmds.checkBox(label='Y', w=50, v=1, en=0)
        self.orZ = cmds.checkBox(label='Z', w=70, v=1, en=0)
        self.orMo = cmds.checkBox(label='Maintain Offset', v=1, en=0)
        cmds.setParent("..")

        cmds.separator(height=10, width=400, style='in')

        # scale setup
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        self.scEn = cmds.checkBox(label='Scale', w=85, v=0, cc=self.scToggle)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        self.scX = cmds.checkBox(label='X', w=50, v=1, en=0)
        self.scY = cmds.checkBox(label='Y', w=50, v=1, en=0)
        self.scZ = cmds.checkBox(label='Z', w=70, v=1, en=0)
        self.scMo = cmds.checkBox(label='Maintain Offset', v=1, en=0)
        cmds.setParent("..")

        cmds.separator(height=10, width=400, style='in')

        # aim setup
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        self.aiEn = cmds.checkBox(label='Aim', w=85, v=0, cc=self.aiToggle)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        self.aiX = cmds.checkBox(label='X', w=50, v=1, en=0)
        self.aiY = cmds.checkBox(label='Y', w=50, v=1, en=0)
        self.aiZ = cmds.checkBox(label='Z', w=70, v=1, en=0)
        self.aiMo = cmds.checkBox(label='Maintain Offset', v=1, en=0)
        cmds.setParent("..")

        cmds.separator(height=10, width=400, style='in')

        # pole vector setup
        cmds.rowLayout(numberOfColumns=9)
        cmds.separator(width=10, hr=0, style='none')
        self.pvEn = cmds.checkBox(label='Pole Vector', w=85, v=0, cc=self.pvToggle)
        cmds.separator(height=13, hr=0, style='shelf')
        cmds.separator(width=4, hr=0, style='none')
        cmds.checkBox(label='X', w=50, v=1, vis=0)
        cmds.checkBox(label='Y', w=50, v=1, vis=0)
        cmds.checkBox(label='Z', w=70, v=1, vis=0)
        cmds.checkBox(label='Maintain Offset', v=1, vis=0)
        cmds.setParent("..")
           
        # double-lined separator
        cmds.separator(height=5, width=400, style='none')
        cmds.separator(height=5, width=400, style='in')
        cmds.separator(height=5, width=400, style='in')
        
        ### SECTION 5: EXECUTE BUTTON SETUP ###

        cmds.button(label="One For All: A to B, A to C, A to D, etc.", w=400, h=40, command=self.OneForAll)
        cmds.button(label="One By One: 1A to 1B, 2A to 2B, 3A to 3B, etc.", w=400, h=40, command=self.OneByOne)

        # shows window
        cmds.showWindow(self.win)
        
        
#############################################################################
###                       CHECKBOX TOGGLE FUNCTIONS                       ###
#############################################################################

        # function called by toggling the enable checkboxes for each constraint.
        # sets the enable value of other attributes based on the initial checkbox.

    def paToggle(self, *args):
        self.paVal = cmds.checkBox(self.paEn, q=1, v=1)
        cmds.checkBox(self.paTraX, e=1, en=self.paVal)
        cmds.checkBox(self.paTraY, e=1, en=self.paVal)
        cmds.checkBox(self.paTraZ, e=1, en=self.paVal)
        cmds.checkBox(self.paRotX, e=1, en=self.paVal)
        cmds.checkBox(self.paRotY, e=1, en=self.paVal)
        cmds.checkBox(self.paRotZ, e=1, en=self.paVal)
        cmds.checkBox(self.paMo, e=1, en=self.paVal)
        return self.paVal
        
    def ptToggle(self, *args):
        self.ptVal = cmds.checkBox(self.ptEn, q=1, v=1)
        cmds.checkBox(self.ptX, e=1, en=self.ptVal)
        cmds.checkBox(self.ptY, e=1, en=self.ptVal)
        cmds.checkBox(self.ptZ, e=1, en=self.ptVal)
        cmds.checkBox(self.ptMo, e=1, en=self.ptVal)
        return self.ptVal
    
    def orToggle(self, *args):
        self.orVal = cmds.checkBox(self.orEn, q=1, v=1)
        cmds.checkBox(self.orX, e=1, en=self.orVal)
        cmds.checkBox(self.orY, e=1, en=self.orVal)
        cmds.checkBox(self.orZ, e=1, en=self.orVal)
        cmds.checkBox(self.orMo, e=1, en=self.orVal)
        return self.orVal
        
    def scToggle(self, *args):
        self.scVal = cmds.checkBox(self.scEn, q=1, v=1)
        cmds.checkBox(self.scX, e=1, en=self.scVal)
        cmds.checkBox(self.scY, e=1, en=self.scVal)
        cmds.checkBox(self.scZ, e=1, en=self.scVal)
        cmds.checkBox(self.scMo, e=1, en=self.scVal)
        return self.scVal

    def aiToggle(self, *args):
        self.aiVal = cmds.checkBox(self.aiEn, q=1, v=1)
        cmds.checkBox(self.aiX, e=1, en=self.aiVal)
        cmds.checkBox(self.aiY, e=1, en=self.aiVal)
        cmds.checkBox(self.aiZ, e=1, en=self.aiVal)
        cmds.checkBox(self.aiMo, e=1, en=self.aiVal)
        return self.aiVal
        
    def pvToggle(self, *args):
        self.pvVal = cmds.checkBox(self.pvEn, q=1, v=1)
        return self.pvVal

#############################################################################
###                         SKIP TRANSFORMS SETUP                         ###
#############################################################################

        # set of functions to enable and disable transformation axes.
        # each function creates a list of axes to skip, then plugs that list into the skip functions for each constraint.

    def parentSkipTranslate(self, *args):
        self.paSkipT = []
        if cmds.checkBox(self.paTraX, q=1, v=1) == 0:  #EZ unnecesary set of () around cmds... (many places)
            self.paSkipT.append("x")
        if cmds.checkBox(self.paTraY, q=1, v=1) == 0:
            self.paSkipT.append("y")
        if cmds.checkBox(self.paTraZ, q=1, v=1) == 0:
            self.paSkipT.append("z")
        if len(self.paSkipT) == 3:
            cmds.error("No translation axes were enabled. Please select at least one axis to constrain or use the Orient constraint instead.")
        return self.paSkipT
        
    def parentSkipRotate(self, *args):
        self.paSkipR = []
        if cmds.checkBox(self.paRotX, q=1, v=1) == 0:
            self.paSkipR.append("x")
        if cmds.checkBox(self.paRotY, q=1, v=1) == 0:
            self.paSkipR.append("y")
        if cmds.checkBox(self.paRotZ, q=1, v=1) == 0:
            self.paSkipR.append("z")
        if len(self.paSkipR) == 3:
            cmds.error("No rotation axes were enabled. Please select at least one axis to constrain or use the Point constraint instead.")
        return self.paSkipR
                
    def pointSkip(self, *args):
        self.ptSkip = []
        if cmds.checkBox(self.ptX, q=1, v=1) == 0:
            self.ptSkip.append("x")
        if cmds.checkBox(self.ptY, q=1, v=1) == 0:
            self.ptSkip.append("y")
        if cmds.checkBox(self.ptZ, q=1, v=1) == 0:
            self.ptSkip.append("z")
        if len(self.ptSkip) == 3:
            cmds.error("No axes were enabled. Please select at least one axis to constrain.")
        return self.ptSkip

    def orientSkip(self, *args):
        self.orSkip = []
        if cmds.checkBox(self.orX, q=1, v=1) == 0:
            self.orSkip.append("x")
        if cmds.checkBox(self.orY, q=1, v=1) == 0:
            self.orSkip.append("y")
        if cmds.checkBox(self.orZ, q=1, v=1) == 0:
            self.orSkip.append("z")
        if len(self.orSkip) == 3:
            cmds.error("No axes were enabled. Please select at least one axis to constrain.")
        return self.orSkip

    def scaleSkip(self, *args):
        self.scSkip = []
        if cmds.checkBox(self.scX, q=1, v=1) == 0:
            self.scSkip.append("x")
        if cmds.checkBox(self.scY, q=1, v=1) == 0:
            self.scSkip.append("y")
        if cmds.checkBox(self.scZ, q=1, v=1) == 0:
            self.scSkip.append("z")
        if len(self.scSkip) == 3:
            cmds.error("No axes were enabled. Please select at least one axis to constrain.")
        return self.scSkip

    def aimSkip(self, *args):
        self.aiSkip = []
        if cmds.checkBox(self.aiX, q=1, v=1) == 0:
            self.aiSkip.append("x")
        if cmds.checkBox(self.aiY, q=1, v=1) == 0:
            self.scSkip.append("y")
        if cmds.checkBox(self.scZ, q=1, v=1) == 0:
            self.scSkip.append("z")
        if len(self.aiSkip) == 3:
            cmds.error("No axes were enabled. Please select at least one axis to constrain.")
        return self.scSkip
        
#############################################################################
###                   PARENT AND CHILD SELECTION LISTS                    ###
#############################################################################
    
        # creates parent and children lists from input strings using filters and sorting functions
    
    def createParentList(self, pInput):
        self.parString = "*" + cmds.textField(self.pInput, q=1, text=1) + "*"
        self.parFilter = cmds.itemFilter(byName=self.parString)
        self.parListDirty = cmds.lsThroughFilter(self.parFilter, sl=1)
        self.parList = cmds.sortCaseInsensitive(self.parListDirty)
        return self.parList

    def createChildList(self, cInput):
        self.chiString = "*" + cmds.textField(self.cInput, q=1, text=1) + "*"
        self.chiFilter = cmds.itemFilter(byName=self.chiString)
        self.chiListDirty = cmds.lsThroughFilter(self.chiFilter, sl=1)
        self.chiList = cmds.sortCaseInsensitive(self.chiListDirty)
        return self.chiList
        
        # creates a zip for matching parents and children
    def createMultiPairs(self, parList, chiList):
        self.pairs = zip(self.parList,self.chiList)
        return self.pairs
        
#############################################################################
###                          CONSTRAINT CREATION                          ###
#############################################################################

    def createParentConstraint(self, *args):
        if cmds.checkBox(self.paEn, q=1, v=1) == 0:
            return 0
        self.parentSkipTranslate()
        self.parentSkipRotate()
        if len(self.parList) == 1:
            self.parentObject = self.parList[0]
            for each in self.chiList:
                cmds.parentConstraint(self.parentObject, each, st=self.paSkipT, sr=self.paSkipR, mo=cmds.checkBox(self.paMo, q=1, v=1))
        if len(self.parList) == len(self.chiList):
            self.createMultiPairs(self.parList, self.chiList)
            for eachA, eachB in self.pairs:
                cmds.parentConstraint(eachA, eachB, st=self.paSkipT, sr=self.paSkipR, mo=cmds.checkBox(self.paMo, q=1, v=1))

    def createPointConstraint(self, *args):
        if cmds.checkBox(self.ptEn, q=1, v=1) == 0:
            return 0
        self.pointSkip()
        if len(self.parList) == 1:
            self.parentObject = self.parList[0]
            for each in self.chiList:
                cmds.pointConstraint(self.parentObject, each, sk=self.ptSkip, mo=cmds.checkBox(self.ptMo, q=1, v=1))
        if len(self.parList) == len(self.chiList):
            self.createMultiPairs(self.parList, self.chiList)
            for eachA, eachB in self.pairs:
                cmds.pointConstraint(eachA, eachB, sk=self.ptSkip, mo=cmds.checkBox(self.ptMo, q=1, v=1))

    def createOrientConstraint(self, *args):
        if cmds.checkBox(self.orEn, q=1, v=1) == 0:
            return 0
        self.orientSkip()
        if len(self.parList) == 1:
            self.parentObject = self.parList[0]
            for each in self.chiList:
                cmds.orientConstraint(self.parentObject, each, sk=self.orSkip, mo=cmds.checkBox(self.orMo, q=1, v=1))
        if len(self.parList) == len(self.chiList):
            self.createMultiPairs(self.parList, self.chiList)
            for eachA, eachB in self.pairs:
                cmds.orientConstraint(eachA, eachB, sk=self.orSkip, mo=cmds.checkBox(self.orMo, q=1, v=1))

    def createScaleConstraint(self, *args):
        if cmds.checkBox(self.scEn, q=1, v=1) == 0:
            return 0
        self.scaleSkip()
        if len(self.parList) == 1:
            self.parentObject = self.parList[0]
            for each in self.chiList:
                cmds.scaleConstraint(self.parentObject, each, sk=self.scSkip, mo=cmds.checkBox(self.scMo, q=1, v=1))
        if len(self.parList) == len(self.chiList):
            self.createMultiPairs(self.parList, self.chiList)
            for eachA, eachB in self.pairs:
                cmds.scaleConstraint(eachA, eachB, sk=self.scSkip, mo=cmds.checkBox(self.scMo, q=1, v=1))

    def createAimConstraint(self, *args):
        if cmds.checkBox(self.aiEn, q=1, v=1) == 0:
            return 0
        self.aimSkip()
        if len(self.parList) == 1:
            self.parentObject = self.parList[0]
            for each in self.chiList:
                cmds.aimConstraint(self.parentObject, each, sk=self.aiSkip, mo=cmds.checkBox(self.aiMo, q=1, v=1))
        if len(self.parList) == len(self.chiList):
            self.createMultiPairs(self.parList, self.chiList)
            for eachA, eachB in self.pairs:
                cmds.aimConstraint(eachA, eachB, sk=self.aiSkip, mo=cmds.checkBox(self.aiMo, q=1, v=1))

    def createPoleVectorConstraint(self, *args):
        if cmds.checkBox(self.pvEn, q=1, v=1) == 0:
            return 0
        if len(self.parList) == 1:
            self.parentObject = self.parList[0]
            for each in self.chiList:
                cmds.poleVectorConstraint(self.parentObject, each)
        if len(self.parList) == len(self.chiList):
            self.createMultiPairs(self.parList, self.chiList)
            for eachA, eachB in self.pairs:
                cmds.poleVectorConstraint(eachA, eachB)

#############################################################################
###                             ERROR TESTING                             ###
#############################################################################

    def constraintErrorTest(self, *args):
        # print error if constraints would conflict with each other
        self.paToggle()
        self.ptToggle()
        self.orToggle()
        self.scToggle()
        self.aiToggle()
        self.pvToggle()
        if self.paVal == 1 and self.ptVal == 1:
            cmds.error("Parent and Point constraints both constrain translation. Please select only one of them.")
        if self.paVal == 1 and self.orVal == 1:
            cmds.error("Parent and Orient constraints both constrain rotation. Please select only one of them.")
        if self.paVal == 1 and self.aiVal == 1:
            cmds.error("Parent and Aim constraints both constrain rotation. Please select only one of them.")
        if self.orVal == 1 and self.aiVal == 1:
            cmds.error("Orient and Aim constraints both constrain rotation. Please select only one of them.")
        if (self.pvVal == 1 and self.paVal == 1) or (self.pvVal == 1 and self.ptVal == 1) or (self.pvVal == 1 and self.orVal == 1) or (self.pvVal == 1 and self.scVal == 1) or (self.pvVal == 1 and self.aiVal == 1):
            cmds.error("If you are trying to constrain a Pole Vector, deselect all other constraints. Otherwise, deselect the Pole Vector option.")
            
        # print error if one or both lists are empty
        if not self.chiList and not self.parList:
            cmds.error("Parent and child lists are both empty. You must provide a parent and child string to filter and must select at least two objects: one with the parent string in its name and one with the child string in its name.")
        if not self.parList and len(self.chiList) != 0:
            cmds.error("Parent list is empty. You must provide a parent string to filter and must select at least one object with the parent string in its name.")
        if len(self.parList) != 0 and not self.chiList:
            cmds.error("Child list is empty. You must provide a child string to filter and must select at least one object with the child string in its name.")
        
        # print error if same object in both lists
        for each in self.parList:
            if each in self.chiList:
                cmds.error("Object '" + each + "' is present in both parent and child lists. Either deselect the object or modify the parent or child strings.")

#############################################################################
###                         EXECUTE MAIN FUNCTION                         ###
#############################################################################
        
    def OneForAll(self, *args):
        self.createParentList(self.pInput)
        self.createChildList(self.cInput)
        self.constraintErrorTest()
        # print error if no parents
        if len(self.parList) > 1:
            cmds.error("Multiple parents selected. You must select only ONE parent object and specify a filter string that includes that object. Type out the full name of the parent object in the filter to be sure you're only selecting one object.")
            
        # move on to actual constraint functions
        self.createParentConstraint(self.parList, self.chiList)
        self.createPointConstraint(self.parList, self.chiList)
        self.createOrientConstraint(self.parList, self.chiList)
        self.createScaleConstraint(self.parList, self.chiList)
        self.createAimConstraint(self.parList, self.chiList)
        self.createPoleVectorConstraint(self.parList, self.chiList)
        
    def OneByOne(self, pInput):
        self.createParentList(self.pInput)
        self.createChildList(self.cInput)
        self.constraintErrorTest()
        # print error if selection lengths dont match
        if len(self.parList) != len(self.chiList):
            self.parLen = str(len(self.parList))
            self.chiLen = str(len(self.chiList))
            cmds.error("Number of parents (" + self.parLen + ") and children (" + self.chiLen + ") don't match. Make sure to have an equal number of parents and children selected.")
        
        # move on to actual constraint functions
        self.createParentConstraint(self.parList, self.chiList)
        self.createPointConstraint(self.parList, self.chiList)
        self.createOrientConstraint(self.parList, self.chiList)
        self.createScaleConstraint(self.parList, self.chiList)
        self.createAimConstraint(self.parList, self.chiList)
        self.createPoleVectorConstraint(self.parList, self.chiList)
         
