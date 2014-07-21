import sys, argparse
from sinesum2 import table
from math import pi

parser = argparse.ArgumentParser()
parser.add_argument('--n', '--number of iterations', type=str, default='[99]', help='number of iterations', metavar='n')
parser.add_argument('--alpha', '--phase', type=str, default='[0.1]', help='phase', metavar='alpha')
parser.add_argument('--T', '--period', type=float, default=2*pi, help='period', metavar='T')
args = parser.parse_args()

n_values = eval(args.n)
print '\nn     =', n_values
alpha_values = eval(args.alpha)
print 'alpha =', alpha_values
T = args.T
print 'T     =', T, '\n'
table(n_values, alpha_values, T)