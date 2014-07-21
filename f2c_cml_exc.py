import sys

if len(sys.argv) < 2:
    print 'Provide an argument on the command line!'
    sys.exit(1)
F = float(sys.argv[1])
C = (F-32)*5/9
print 'C =', C