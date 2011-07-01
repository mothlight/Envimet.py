'''
Created on Jun 29, 2011

@author: nice
'''


from EDIFile import EDIFile  
from EDTFile import EDTFile
from PlotEnergyPlot import PlotEnergyPlot

import array
import Numeric 
#import Gnuplot, Gnuplot.funcutils 

Z_CUT='Z'
Y_CUT='Y'
X_CUT='X'
POT_TEMP_K = 'Pot. Temperature (K)'
WIND_SPEED_MS= 'Wind Speed (m/s)'
SPEC_HUMIDITY='Spec. Humidity (g/kg)'
x=50
y=50
z=1
#ediFile = file(r"/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/atmosphere/MonashCampusValidationNW_AT_00.00.00 23.03.2011.EDI")
variableToFind = POT_TEMP_K
#variableToFind = 
#variableToFind = 
skipValues = 0
cutType = Z_CUT
cutPoint = 1

if __name__ == '__main__':
    pass

ediFile = EDIFile("/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/atmosphere/MonashCampusValidationNW_AT_00.00.00 23.03.2011.EDI")
ediFile.read()
#print(ediFile.numOfVariablesInFile)
#print(ediFile.variableNumber(variableToFind))

edtFile = EDTFile("/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/atmosphere/MonashCampusValidationNW_AT_00.00.00 23.03.2011.EDT")

edtFile.readDataFile(ediFile.variableNumber(variableToFind), cutType, cutPoint, ediFile.numOfXGrids, ediFile.numOfYGrids, ediFile.numOfZGrids, ediFile.numOfVariablesInFile, ediFile.gridSpacingX, ediFile.gridSpacingY, ediFile.gridSpacingZ)

dataList = edtFile.readOneVariableAtXYZ(ediFile.variableNumber(POT_TEMP_K), cutType, cutPoint, ediFile.numOfXGrids, ediFile.numOfYGrids, ediFile.numOfZGrids, ediFile.numOfVariablesInFile, ediFile.gridSpacingX, ediFile.gridSpacingY, ediFile.gridSpacingZ, x, y, z)
print (dataList)
dataList = edtFile.readOneVariableAtXYZ(ediFile.variableNumber(WIND_SPEED_MS), cutType, cutPoint, ediFile.numOfXGrids, ediFile.numOfYGrids, ediFile.numOfZGrids, ediFile.numOfVariablesInFile, ediFile.gridSpacingX, ediFile.gridSpacingY, ediFile.gridSpacingZ, x, y, z)
print (dataList)
dataList = edtFile.readOneVariableAtXYZ(ediFile.variableNumber(SPEC_HUMIDITY), cutType, cutPoint, ediFile.numOfXGrids, ediFile.numOfYGrids, ediFile.numOfZGrids, ediFile.numOfVariablesInFile, ediFile.gridSpacingX, ediFile.gridSpacingY, ediFile.gridSpacingZ, x, y, z)
print (dataList)

print (dataList[0][3])

## TODO - read all variables needed for energy balance in all files in the data directory and do calculations 

#title = 'Plotting ' + str(variableToFind.replace('\r\n', '')) + ' at cut ' + str(cutType) + '=' + str(cutPoint)
energyPlot = PlotEnergyPlot()

dataItem = ediFile.fileTime + "," + str(dataList[0][3])
plotData = [dataItem]
energyPlot.plot(plotData)