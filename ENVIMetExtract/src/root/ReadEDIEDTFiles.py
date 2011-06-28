import array
import Numeric 

ediFile = file(r"/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/surface/MonashCampusValidationNW_FX_00.00.00 24.03.2011.EDI")
titleOfSim = ediFile.readline()
numOfXGrids = ediFile.readline()
numOfYGrids = ediFile.readline()
numOfZGrids = ediFile.readline()
numOfVariablesInFile = ediFile.readline()

fileVariables=[]
for i in range(0,long(numOfVariablesInFile)):
    fileVariables.append(ediFile.readline())
    print fileVariables[i:]

#use up label line
gridSpacingLabel = ediFile.readline()
                
gridSpacingX=[]
for i in range(0,long(numOfXGrids)):
    gridSpacingX.append(ediFile.readline())
    #print gridSpacingX[i:]
    
gridSpacingY=[]
for i in range(0,long(numOfYGrids)):
    gridSpacingY.append(ediFile.readline())
    #print gridSpacingY[i:]

gridSpacingZ=[]
for i in range(0,long(numOfZGrids)):
    gridSpacingZ.append(ediFile.readline())
    #print gridSpacingZ[i:] 

ediFile.close()

startingX = 2.5
startingY = 2.5
startingZ = 0.0

currentGridX = startingX
currentGridY = startingY
currentGridZ = startingZ

edtFile = open("/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/surface/MonashCampusValidationNW_FX_00.00.00 24.03.2011.EDT", mode='rb')

#variableData=[]
for i in range(0,long(numOfVariablesInFile)):
    #print i
    #print fileVariables[i]
    
    for z in range(0,long(numOfZGrids)):
        for y in range(0,long(numOfYGrids)):
            for x in range(0,long(numOfXGrids)):                
                
                binvalues = array.array('f')
                binvalues.read(edtFile, 1)
                data = Numeric.array(binvalues, typecode=Numeric.Float)
                data = Numeric.reshape(data, (1, 1))
                
                print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " value=" + str(data)
                     
                #print gridSpacingX[x]                
                nextGridX = float(gridSpacingX[x])                            
                currentGridX = currentGridX + nextGridX
            
            nextGridY = float(gridSpacingY[y])
            currentGridY = currentGridY + nextGridY                        
            currentGridX = startingX
        
        currentGridY = startingY;

edtFile.close()