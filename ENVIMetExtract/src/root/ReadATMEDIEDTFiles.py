import array
import Numeric 
import Gnuplot, Gnuplot.funcutils 

Z_CUT='Z'
Y_CUT='Y'
X_CUT='X'
ediFile = file(r"/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/atmosphere/MonashCampusValidationNW_AT_00.00.00 23.03.2011.EDI")
variableToFind = 'Pot. Temperature (K)\r\n'
#variableToFind = 'Wind Speed (m/s)\r\n'
#variableToFind = 'Spec. Humidity (g/kg)\r\n'
skipValues = 0
cutType = Z_CUT
cutPoint = 1

titleOfSim = ediFile.readline()
numOfXGrids = ediFile.readline()
numOfYGrids = ediFile.readline()
numOfZGrids = ediFile.readline()
numOfVariablesInFile = ediFile.readline()

fileVariables=[]
for i in range(0,long(numOfVariablesInFile)):
    fileVariables.append(ediFile.readline())
    print fileVariables[i:]
    if fileVariables[i] == variableToFind:
        skipValues = i
        print("found value")

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
    print gridSpacingZ[i:] 

ediFile.close()

startingX = 2.5
startingY = 2.5
startingZ = 0.0

currentGridX = startingX
currentGridY = startingY
currentGridZ = startingZ

edtFile = open("/mnt/Samsung2TB/EnvimetRuns-5days/Monash/MonashCampusValidationNW/output/atmosphere/MonashCampusValidationNW_AT_00.00.00 23.03.2011.EDT", mode='rb')

print str("Before reading") 

binvalues = array.array('f')
skipOneValue = long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)

numOfItems = long(numOfVariablesInFile) * long(numOfZGrids) * long(numOfYGrids) * long(numOfXGrids)
binvalues.read(edtFile, numOfItems)
print str("After read")
data = Numeric.array(binvalues, typecode=Numeric.Float)
print str("After data")

count = 0 + (skipOneValue * skipValues)
variableStart = skipValues

dataList = []

#for i in range(variableStart,long(numOfVariablesInFile)):
for i in range(variableStart,variableStart+1):
    #print i
    #print fileVariables[i]
    
    for z in range(0,long(numOfZGrids)):
        for y in range(0,long(numOfYGrids)):
            #for x in range(0,long(numOfXGrids)):                
            for x in range(0,long(numOfXGrids)):
                
                #binvalues = array.array('f')
                #binvalues.read(edtFile, long(numOfXGrids) * long(numOfYGrids)  )
                #data = Numeric.array(binvalues, typecode=Numeric.Float)
                #data = Numeric.reshape(data, (1, long(numOfXGrids) * long(numOfYGrids) ))
                                
                if cutType == Z_CUT:
                    if z == cutPoint:
                        #print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " z=" + str(currentGridZ)+ " value=" + str(data[count])
                        #itemData = [currentGridX, currentGridY, data[count]]
                        itemData = [currentGridX, currentGridY, data[count]]
                        dataList.append(itemData)

                
                #print str(fileVariables[i]) +  " x=" + str(currentGridX) + " y=" + str(currentGridY) + " z=" + str(currentGridZ)+ " value=" + str(data[count])
                count = count + 1
                     
                #print gridSpacingX[x]                
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


print (dataList)


# A straightforward use of gnuplot.  The `debug=1' switch is used
# in these examples so that the commands that are sent to gnuplot
# are also output on stderr.
g = Gnuplot.Gnuplot(debug=1)
#title = 'Plotting ' + variableToFind + ' at cut ' + cutType + '=' + cutPoint
title = 'Plotting ' + str(variableToFind.replace('\r\n', '')) + ' at cut ' + str(cutType) + '=' + str(cutPoint)
print (title)
g.title(title) # (optional)
#g('set data style linespoints') # give gnuplot an arbitrary command
# Plot a list of (x, y) pairs (tuples or a numpy array would
# also be OK):
#g.plot([[0,1.1], [1,5.8], [2,3.3], [3,4.2]])

g('set style line 1 lt rgb "red" lw 3')   
g('set style line 2 lt rgb "black" lw 3')   
g('set style line 3 lt rgb "violet" lw 3')   
g('set style line 4 lt rgb "green" lw 3')   
g('set style line 5 lt rgb "cyan" lw 3')   
g('set style line 6 lt rgb "blue" lw 3')   
g('set style line 7 lt rgb "yellow" lw 3')   
g('set macros')   
g('set grid')   
g('unset key')   
g('set parametric')   
g('unset polar')   
#g('set terminal png size  2048,1200  medium')
g('unset hidden3d')   
g('set ticslevel 0.5')   
g('set view 60,30')   
g('set autoscale')   
g('set parametric')   
g('set style data points')   
g('set dgrid3d 100,100,1')   
g('set xlabel "x (m)"')   
g('set ylabel "y (m)"')   
g('set zlabel "temp C"')   
g('set style data lines')   
g('set size square')   
g('set pm3d map')   
g('set palette rgbformulae 22,13,10')   
g('set autoscale')   
g('set palette gray')   
g('set samples 100; set isosamples 100')   
g('unset logscale')   
g('set key box')   
g('set key right bottom')   
g('set key bmargin')   

g.splot(dataList)
raw_input('Please press return to continue...\n')



