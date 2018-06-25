#!/usr/bin/python

import os, sys, urllib2

if len(sys.argv) < 2:
    print( "\n\tUsage:   %s <query>\n\n" % sys.argv[0] )
    exit()

if len(sys.argv) > 2:
    q = sys.argv[1:]

else:
    q = [sys.argv[1]]

os.system('clear')

print("""
          _                     _    
      ___| | ___ __   ___  _ __| |_  
     / __| |/ / '_ \ / _ \| '__| __| 
    | (__|   <| |_) | (_) | |  | |_  
     \___|_|\_\ .__/ \___/|_|   \__| 
              |_|                    
""")

SERVICES_FILE = os.path.dirname(os.path.realpath(__file__)) + "/services"

if not os.path.exists(SERVICES_FILE):
    print("\n\tDownloading service/port list...")
    open(SERVICES_FILE,'w').write( urllib2.urlopen("https://isc.sans.edu/services.html").read() )
    print("\n\tDone.\n\n")

with open(SERVICES_FILE) as ofile:
    for l in ofile:
        if not l.startswith("#"):
            line = l.strip('\n').lower().split('\t')
            line = [ line[0], line[1].split('/')[0], " ".join(line[1].split('/')[1:]), line[2] ]

            f = 0
            for x in q:
                if (x.isdigit() and x == line[1]) or ((not x.isdigit()) and x in (line[0]+line[2]+line[3])):
                    f += 1

            if f == len(q):
                print( '      ' + ( line[0] + (" " * (25 - len(line[0]))) ) + ( line[1] + (" " * (5 - len(line[1]))) ) + "   " + line[2] + "   " + (line[3] + (" " * (30 - len(line[3])))) )

print('\n')

