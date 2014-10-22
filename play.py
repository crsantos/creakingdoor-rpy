#!/usr/bin/env python

import subprocess, sys, getopt

PLAY_COMMAND        = "mpg123"
HELP_TEXT           = 'play.py -f <filename>'
DEFAULT_FILENAME    = "./media/creakingdoor.mp3"

def play(filename = None):
    """ Play a filename using the mpg123 system lib """

    if not filename:
        print "You should provide a valid filename"
        sys.exit(2)

    try:
        retcode = subprocess.call(PLAY_COMMAND +" " + filename, shell=True)
        if retcode < 0:
            print >> sys.stderr, "Process was terminated by signal", -retcode
        else:
            print >> sys.stderr, "Done!", retcode
    except OSError as e:
        print >> sys.stderr, "Execution failed:", e

def main(argv):
    
    inputfile = DEFAULT_FILENAME

    try:
        opts, args = getopt.getopt(argv,"hf:",["filename=",])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print HELP_TEXT
            sys.exit(2)
        elif opt in ("-f", "--filename"):
            inputfile = arg

    play(inputfile)

if __name__ == '__main__':
    main(sys.argv[1:])