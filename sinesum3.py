import sys
from sinesum2 import table

n_values = eval(sys.argv[1])
print '\nn     =', n_values
alpha_values = eval(sys.argv[2])
print 'alpha =', alpha_values
T = float(sys.argv[3])
print 'T     =', T, '\n'
table(n_values, alpha_values, T)