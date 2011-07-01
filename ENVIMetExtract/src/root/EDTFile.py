'''
Created on Jun 28, 2011

@author: nice
'''

import array
import Numeric 

titleOfSim =''
numOfXGrids =''
numOfYGrids =''
numOfZGrids =''
numOfVariablesInFile =''
fileVariables=[]

edtFileName=''
Z_CUT='Z'
Y_CUT='Y'
X_CUT='X'
fileData=[]

class EDTFile:
    """Read EDT file."""

    def __init__(self, edtFileName):
        '''initialize ediFile class'''
        self.edtFileName = edtFileName

    def readDataFile(self, skipValues, cutType, cutPoint, numOfXGrids, numOfYGrids, numOfZGrids, numOfVariablesInFile, gridSpacingX, gridSpacingY, gridSpacingZ):
        '''initialize ediFile class'''
        startingX = 2.5
        startingY = 2.5
        startingZ = 0.0

        currentGridX = startingX
        currentGridY = startingY
        currentGridZ = startingZ
        
        edtFile = open(self.edtFileName, mode='rb')
        
        binvalues = array.array('f')
        skipOneValue = long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)

        numOfItems = long(numOfVariablesInFile) * long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)
        binvalues.read(edtFile, numOfItems)
        
        data = Numeric.array(binvalues, typecode=Numeric.Float)
        self.fileData = data
        edtFile.close()
        
    def readOneVariable(self, skipValues, cutType, cutPoint, numOfXGrids, numOfYGrids, numOfZGrids, numOfVariablesInFile, gridSpacingX, gridSpacingY, gridSpacingZ):
        """read file and return values"""
        
        startingX = 2.5
        startingY = 2.5
        startingZ = 0.0

        currentGridX = startingX
        currentGridY = startingY
        currentGridZ = startingZ
        
        edtFile = open(self.edtFileName, mode='rb')
        
        binvalues = array.array('f')
        skipOneValue = long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)

        numOfItems = long(numOfVariablesInFile) * long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)
        binvalues.read(edtFile, numOfItems)
        
        data = Numeric.array(binvalues, typecode=Numeric.Float)
        
        count = 0 + (skipOneValue * skipValues)
        
        variableStart = skipValues
        
        dataList = []
        
        for i in range(variableStart,variableStart+1):                
            for z in range(0,long(numOfZGrids)):                
                for y in range(0,long(numOfYGrids)):                                
                    for x in range(0,long(numOfXGrids)):                        
                                
                        if cutType == Z_CUT:                            
                            if z == cutPoint:                                
                                #print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " z=" + str(currentGridZ)+ " value=" + str(data[count])                                
                                itemData = [currentGridX, currentGridY, data[count]]
                                dataList.append(itemData)                                
                                        
                        #print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " z=" + str(currentGridZ)+ " value=" + str(data[count])
                        count = count + 1                                        
                        nextGridX = float(gridSpacingX[x])                            
                        currentGridX = currentGridX + nextGridX                        
                    
                    nextGridY = float(gridSpacingY[y])
                    currentGridY = currentGridY + nextGridY                        
                    currentGridX = startingX                    
    
                nextGridZ = float(gridSpacingZ[z])
                currentGridZ = currentGridZ + nextGridZ      
                currentGridY = startingY;                
        
            currentGridZ = startingZ;            

        edtFile.close()
        return dataList
        
    def variableNumber(self, variableToFind):
        """locate the variable position in the edi file variable list"""
        for i in range(0,long(self.numOfVariablesInFile)):              
            #print fileVariables[i:]            
            if fileVariables[i] == variableToFind:
                return i
            
    def readOneVariableAtXYZ(self, skipValues, cutType, cutPoint, numOfXGrids, numOfYGrids, numOfZGrids, numOfVariablesInFile, gridSpacingX, gridSpacingY, gridSpacingZ, xPoint, yPoint, zPoint):
        """read file and return values"""
        
        startingX = 2.5
        startingY = 2.5
        startingZ = 0.0

        currentGridX = startingX
        currentGridY = startingY
        currentGridZ = startingZ
        
        #edtFile = open(self.edtFileName, mode='rb')
        
        #binvalues = array.array('f')
        skipOneValue = long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)

        numOfItems = long(numOfVariablesInFile) * long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)
        #binvalues.read(edtFile, numOfItems)
        
        #data = Numeric.array(binvalues, typecode=Numeric.Float)
        
        count = 0 + (skipOneValue * skipValues)
        
        variableStart = skipValues
        
        dataList = []
        
        for i in range(variableStart,variableStart+1):                
            for z in range(0,long(zPoint+1)):                
                for y in range(0,long(yPoint+1)):                                
                    for x in range(0,long(xPoint+1)):   
                           
                        if xPoint == x: 
                            if yPoint == y: 
                                if zPoint == z:
                                    itemData = [currentGridX, currentGridY, currentGridZ, self.fileData[count]]   
                                    dataList.append(itemData)             
                                
                        #if cutType == Z_CUT:                            
                        #    if z == cutPoint:                                
                        #        #print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " z=" + str(currentGridZ)+ " value=" + str(data[count])                                
                        #        itemData = [currentGridX, currentGridY, data[count]]
                        #        dataList.append(itemData)                                
                                        
                        #print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " z=" + str(currentGridZ)+ " value=" + str(data[count])
                        count = count + 1                                        
                        nextGridX = float(gridSpacingX[x])                            
                        currentGridX = currentGridX + nextGridX                        
                    
                    nextGridY = float(gridSpacingY[y])
                    currentGridY = currentGridY + nextGridY                        
                    currentGridX = startingX                    
    
                nextGridZ = float(gridSpacingZ[z])
                currentGridZ = currentGridZ + nextGridZ      
                currentGridY = startingY;                
        
            currentGridZ = startingZ;            

        #edtFile.close()
        return dataList            
                
