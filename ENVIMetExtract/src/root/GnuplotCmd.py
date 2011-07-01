'''
Created on Jun 29, 2011

@author: nice
'''
import subprocess
from sys import stdout, stderr
from os import linesep as nl

class GnuplotCmd:
    """Gnuplot command"""
    
    def __init__(self):
        '''initialize ediFile class'''
        

    def gnuplot_ExecuteCommands(self, commands, data):
        args = ["gnuplot", "-e", (";".join([str(c) for c in commands]))]
        program = subprocess.Popen(\
                                   args, \
                                   stdin=subprocess.PIPE, \
                                   stdout=subprocess.PIPE, \
                                   stderr=subprocess.PIPE, \
                                   )
        for line in data:
            program.stdin.write(str(line)+nl)
            return program

    def gnuplot_GifTest(self):
        commands = [\
                    "set datafile separator ','",\
                    "set terminal png size   2048,1200 enhanced font Vera 14 ",\
                    "set output '/home/nice/python/out.png'",\
                    "plot '-' using 1:2 with linespoints, '' using 1:2 with linespoints",\
                    ]
        data = [\
                "1,1",\
                "2,2",\
                "3,5",\
                "4,2",\
                "5,1",\
                "e",\
                "1,5",\
                "2,4",\
                "3,1",\
                "4,4",\
                "5,5",\
                "e",\
                ]
        return (commands, data)

    if __name__=="__main__":
        (commands, data) = gnuplot_GifTest()
        plotProg = gnuplot_ExecuteCommands(commands, data)
        (out, err) = (plotProg.stdout, plotProg.stderr)
        stdout.write(out.read())
