import sys
s = 0
print 'The sum of',
for arg in sys.argv[1:]:
    s += float(arg)
    print arg,
print 'is', s

s = sum([float(x) for x in sys.argv[1:]])
print 'The sum of %s is %s' % (', '.join(sys.argv[1:]), s)