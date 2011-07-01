'''
Created on Jun 28, 2011

@author: nice
'''

import array
import Numeric 
import Gnuplot, Gnuplot.funcutils


class PlotGreyPlot:
    """Plot grey plot. Call with dataset to plot a 2d grey scale plot."""

    def __init__(self):
        '''initialize PlotGreyPlot class'''
        

        
    def plot(self, dataList, title):
        """read file and store values"""
        # A straightforward use of gnuplot.  The `debug=1' switch is used
        # in these examples so that the commands that are sent to gnuplot
        # are also output on stderr.
        g = Gnuplot.Gnuplot(debug=0)
        #title = 'Plotting ' + variableToFind + ' at cut ' + cutType + '=' + cutPoint
        
        #print (title)
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