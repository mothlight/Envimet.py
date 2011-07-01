'''
Created on Jun 28, 2011

@author: nice
'''

#import array
#import Numeric 
#import Gnuplot, Gnuplot.PlotItems, Gnuplot.funcutils
#import os, time, math, tempfile
#import numpy
#import subprocess
from GnuplotCmd import GnuplotCmd
from sys import stdout, stderr

class PlotEnergyPlot:
    """Plot grey plot."""

    def __init__(self):
        '''initialize ediFile class'''
        

        
    def plot(self, dataList):
        """read file and store values"""
        
        gnuplotcmd = GnuplotCmd()
        commands = [\
        "set style line 1 linecolor rgbcolor \"#0000AA\" lw 2 ps 1",\
        "set datafile separator ','",\
        "set terminal png size   2048,1200 enhanced font Vera 14 ",\
        "set output '/home/nice/python/out.png'",\
        "plot '-' using 1:2 with linespoints, '' using 1:2 ls 1 with linespoints",\
        ]
        
        commands = [\
        "set datafile separator ','",\
        "set style line 1 linecolor rgbcolor \"#0000AA\" lw 4 ps 4",\
        "set style line 2 linecolor rgbcolor \"#990000\" lw 2 ps 1",\
        "set style line 3 linecolor rgbcolor \"#52015b\" lw 2 ps 1",\
        "set style line 4 linecolor rgbcolor \"#988f03\" lw 2 ps 1",\
        "set style line 5 linecolor rgbcolor \"#be7400\" lw 2 ps 1",\
        "set style line 6 linecolor rgbcolor \"#00AA00\" lw 2 ps 1",\
        "set style line 7 linecolor rgbcolor \"#00b7be\" lw 2 ps 1",\
        "set style line 8 linecolor rgbcolor \"#808080\" lw 2 ps 1",\
        "set style line 9 linecolor rgbcolor \"#d26584\" lw 2 ps 1",\
        "set title \"Daily energy balance of validation run of flat bare grass surface in Melbourne, v3.1\"",\
        "set grid",\
        "set key right box",\
        "unset parametric",\
        "unset polar",\
        "set xlabel \"Date/Time\"",\
        "set ylabel \"W/m^2\"",\
        "set terminal png size 2048,1200 enhanced font Vera 14",\
        "set timefmt '%Y-%m-%d-%H:%M'",\
        "set format x '%H'",\
        "set xdata time",\
        #"set autoscale",\
        "set format x '%d %b %Y %H:00'",\
        #"set xtics 3600*24",\
        "unset logscale",\
        "set output '/home/nice/python/out.png'",\
        "plot '-' using 1:2 title \"sw in\" ls 1 with lines, '' using 1:2 ls 1 with lines",\
        #"plot '-' using 1:2 with linespoints, '' using 1:2 ls 1 with linespoints",\
        ]
        
        data = dataList
        data.append("e")
        
        
        
        
        data2 = [\
        "2011-01-26-06:00,0",\
        "2011-01-26-07:00,401",\
        "2011-01-26-08:00,627",\
        "2011-01-26-09:00,746",\
        "2011-01-26-10:00,815",\
        "2011-01-26-13:00,868",\
        "2011-01-26-14:00,851",\
        "2011-01-26-15:00,815",\
        "2011-01-26-16:00,749",\
        "2011-01-26-18:00,414",\
        
        #"2010-03-03-12:00,1",\
        #"2010-03-04-12:00,2",\
        #"2010-03-05-12:00,5",\
        #"2010-03-06-12:00,2",\
        #"2010-03-07-12:00,1",\
        "e",\
        #"2010-03-08-12:00,5",\
        #"2010-03-09-12:00,4",\
        #"2010-03-10-12:00,1",\
        #"2010-03-11-12:00,4",\
        #"2010-03-12-12:00,5",\
        #"e",\
        ]
        
        print (data)
        print (data2)
        plotProg = gnuplotcmd.gnuplot_ExecuteCommands(commands, data)
        (out, err) = (plotProg.stdout, plotProg.stderr)
        #stdout.write(out.read())
        #print (err.read())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #proc = subprocess.Popen(['gnuplot','-p'], 
        #                shell=True,
        #                stdin=subprocess.PIPE,
        #                )
        #proc.stdin.write('set xrange [0:10]; set yrange [-2:2]\n')
        #proc.stdin.write('plot sin(x)\n')
        #raw_input('Please press return to continue...\n')
        #proc.stdin.write('quit\n') #close the gnuplot window

        
        
        
        
        
        
        
        
        #g = Gnuplot.Gnuplot(debug=1)

        ##g('set style line 1 linecolor rgbcolor "#0000AA" lw 2 ps 1')
        ##g('set style line 2 linecolor rgbcolor "#990000" lw 2 ps 1')
        ##g('set style line 3 linecolor rgbcolor "#52015b" lw 2 ps 1')
        ##g('set style line 4 linecolor rgbcolor "#988f03" lw 2 ps 1')
        ##g('set style line 5 linecolor rgbcolor "#be7400" lw 2 ps 1')
        ##g('set style line 6 linecolor rgbcolor "#00AA00" lw 2 ps 1') 
        ##g('set style line 7 linecolor rgbcolor "#00b7be" lw 2 ps 1') 
        ##g('set style line 8 linecolor rgbcolor "#808080" lw 2 ps 1') 
        ##g('set style line 9 linecolor rgbcolor "#d26584" lw 2 ps 1') 

        ##g('set title "Daily energy balance of validation run of flat bare grass surface in Melbourne, v3.1"')
        ##g('set grid')
        ##g('set key right box')
        ##g('unset parametric')
        ##g('unset polar')
        ##g('set xlabel "Date/Time"')
        ##g('set ylabel "W/m^2"')
        ##g('set timefmt \'%Y-%m-%d-%H:%M\'')
        #g('set terminal png size   2048,1200 enhanced font Vera 14') 
        #g('set output "/mnt/Samsung2TB/EnvimetRuns-5days/BareGrassMelb2/output/surface/../graphs/FlatBareGrassMelbourne-3days_.png"')
        ##g('#set format x \'%H\'')
        ##g('set xdata time')
        ##g('set format x \'%d %b %Y %H:00\'')
        ##g('set xtics 3600*24')
        
        
        # Make two temporary files:
        #if hasattr(tempfile, 'mkstemp'):
        #    (fd, filename1,) = tempfile.mkstemp(text=1)
        #    f = os.fdopen(fd, 'w')
        #    (fd, filename2,) = tempfile.mkstemp(text=1)
        #else:
        #    filename1 = tempfile.mktemp()
        #    f = open(filename1, 'w')
        #    filename2 = tempfile.mktemp()
        #try:
        #    for x in numpy.arange(100.)/5. - 10.:
        #        f.write('%s %s %s\n' % (x, math.cos(x), math.sin(x)))
        #    f.close()
        #    
        #    raw_input('Please press return to continue...\n')
        #
        #    g.plot(dataList, using=1, with_='lines')
        #    
        #    f.close()   
        #finally:
        #    os.unlink(filename1)
        #    os.unlink(filename2)
        
        #g.plot(dataList, using_=1, with_='lines')
        

        ##g.plot(dataList, using = (1,2))
        #g.plot(dataList)
        #raw_input('Please press return to continue...\n')