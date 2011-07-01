'''
Created on Jun 28, 2011

@author: nice
'''

from EDIFile import EDIFile  
from EDTFile import EDTFile
from PlotGreyPlot import PlotGreyPlot

import array
import Numeric 
#import Gnuplot, Gnuplot.funcutils 

Z_CUT='Z'
Y_CUT='Y'
X_CUT='X'
#ediFile = file(r"/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/atmosphere/MonashCampusValidationNW_AT_00.00.00 23.03.2011.EDI")
variableToFind = 'Pot. Temperature (K)'
#variableToFind = 'Wind Speed (m/s)'
#variableToFind = 'Spec. Humidity (g/kg)'
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
dataList = edtFile.readOneVariable(ediFile.variableNumber(variableToFind), cutType, cutPoint, ediFile.numOfXGrids, ediFile.numOfYGrids, ediFile.numOfZGrids, ediFile.numOfVariablesInFile, ediFile.gridSpacingX, ediFile.gridSpacingY, ediFile.gridSpacingZ)
#print (dataList)

title = 'Plotting ' + str(variableToFind.replace('\r\n', '')) + ' at cut ' + str(cutType) + '=' + str(cutPoint)
greyPlot = PlotGreyPlot()
greyPlot.plot(dataList, title)