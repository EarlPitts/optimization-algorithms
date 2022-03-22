from numpy import sqrt

# Sample 1
f1 = lambda x: x**3-3*x**2+4
df1 = lambda x: 3*x**2-6*x
ddf1 = lambda x: 6*x-6

# Sample 2
f2 = lambda x: x**4
df2 = lambda x: 4*x**3
ddf2 = lambda x: 12*x**2

# Sample 3
f3 = lambda x: sqrt(1+x**2)
df3 = lambda x: x/sqrt(1+x**2)
ddf3 = lambda x: (1/sqrt(1+x**2))**3
