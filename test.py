import sys

try:
    F = float(sys.argv[1])
except IndexError:
    print 'F must be provided as command-line argument'
    sys.exit(1)
except ValueError:
    print 'F must be pure number'
    sys.exit(1)
C = (F-32)*5/9
print 'C =', C