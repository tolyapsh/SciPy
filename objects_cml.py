import sys

if len(sys.argv) < 2:
    print 'Provide an argument on the command line!'
    sys.exit(1)
a = eval(sys.argv[1])
print a, 'is a', type(a)