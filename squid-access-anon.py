import sys
import re

if len(sys.argv) != 3:
    print >>sys.stderr, """Usage: %s INPUTFILE OUTPUTFILE""" % sys.argv[0]
    sys.exit()

sourcefile = open(sys.argv[1],'r').read().splitlines()
desfile = open(sys.argv[2], 'w')

for i in sourcefile:
    url = re.sub('(https|http|ftp)\:\/\/|([a-z0-9A-Z]+\.[a-z0-9A-Z]+\.[a-zA-Z]{2,4})|([a-z0-9A-Z]+\.[a-zA-Z]{2,4})|\?([a-zA-Z0-9]+[\&\=\#a-z]+)', 'ANONYMIZED', i)
    desfile.write(url+'\n')
