'''
Created on Jun 28, 2011

@author: nice
'''

titleOfSim =''
numOfXGrids =''
numOfYGrids =''
numOfZGrids =''
numOfVariablesInFile =''
fileVariables=[]
gridSpacingZ=[]
gridSpacingY=[]
gridSpacingX=[]
ediFileName=''

class EDIFile:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    def __init__(self, ediFile):
        '''initialize ediFile class'''
        self.ediFileName = ediFile

        
    def read(self):
        """read file and store values"""
        ediFile = file(self.ediFileName)
        
        self.titleOfSim = ediFile.readline()
        self.numOfXGrids = ediFile.readline()
        self.numOfYGrids = ediFile.readline()
        self.numOfZGrids = ediFile.readline()
        self.numOfVariablesInFile = ediFile.readline()
        
        
        for i in range(0,long(self.numOfVariablesInFile)):
            fileVariables.append(ediFile.readline().replace('\r\n', ''))
            #print fileVariables[i:]
            #if fileVariables[i] == variableToFind:
                #skipValues = i
                #print("found value")
        
        
        #use up label line
        gridSpacingLabel = ediFile.readline()              
        
        for i in range(0,long(self.numOfXGrids)):
            gridSpacingX.append(ediFile.readline())
            #print gridSpacingX[i:]    
        self.gridSpacingX = gridSpacingX
        
        for i in range(0,long(self.numOfYGrids)):
            gridSpacingY.append(ediFile.readline())
            #print gridSpacingY[i:]
        self.gridSpacingY = gridSpacingY
        
        for i in range(0,long(self.numOfZGrids)):
            gridSpacingZ.append(ediFile.readline())
            #print gridSpacingZ[i:] 
        self.gridSpacingZ = gridSpacingZ            

        ediFile.close()
        
    def variableNumber(self, variableToFind):
        """locate the variable position in the edi file variable list"""
        for i in range(0,long(self.numOfVariablesInFile)):              
            #print fileVariables[i:]            
            if fileVariables[i] == variableToFind:
                return i
                
