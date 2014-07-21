import sys, random

A = -100
B = 100
n = eval(sys.argv[1])

fail1 = 0; eq1 = 0
fail2 = 0; eq2 = 0

for i in range(n):
    a = random.uniform(A, B)
    b = random.uniform(A, B)
    if (a*b)**3 == a**3*b**3:
        eq1 += 1
    else:
        fail1 += 1
    if a/b == 1/(b/a):
        eq2 += 1
    else:
        fail2 += 1

print 'Equivalences:', eq1*100/float(n), '%'
print 'Failures:    ', fail1*100/float(n), '%\n'
print 'Equivalences:', eq2*100/float(n), '%'
print 'Failures:    ', fail2*100/float(n), '%'