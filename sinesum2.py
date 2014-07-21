from math import sin, pi

def f(t, T):
    if t<T/2.:
        return 1
    elif t==T/2.:
        return 0
    else:
        return -1
    
def S(t, n, T):
    sum = 0
    for i in range(1, n+1):
        ii = 2*i - 1
        sum += sin(2*ii*t*pi/T)/ii
    return sum*4/pi

def table(n_values = [1, 3, 5, 10, 30, 99], alpha_values = [0.01, 0.25, 0.49, 0.75, 0.99], T = 2*pi):
    for alpha in alpha_values:
        t = alpha*T
        print 'alpha =', alpha
        print ' n |   f  |  approx | error'
        print '---|------|---------|------'
        for n in n_values:
            fi = f(t, T)
            si = S(t, n, T)
            print '%2d | %4.1f | %7.4f | %.3f' % (n, fi, si, abs(fi-si))
        print
        
if __name__ == '__main__':
    table()