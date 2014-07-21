def c2f(C):
    return 1.8*C + 32

def f2c(F):
    return (F - 32)/1.8

def c2k(C):
    return C + 273.15

def k2c(K):
    return K - 273.15

def f2k(F):
    return (F - 32)/1.8 + 273.15

def k2f(K):
    return 1.8*(K - 273.15) + 32

if __name__ == '__main__':
    import sys
    T = float(sys.argv[1])
    scale = sys.argv[2]
    if scale == 'C':
        print c2f(T), 'F', c2k(T), 'K'
    elif scale == 'F':
        print f2c(T), 'C', f2k(T), 'K'
    elif scale == 'K':
        print k2f(T), 'F', k2c(T), 'C'
    else:
        print 'Scale must be C, F or K only.'