## Argument-Passing Basics
# parameter
def f(x):
    return x*2

# argument
f(10)

# Assignment Model for Arguments
def f(L):
    L.append(4)

x = [1,2,3]
f(x)           # x has changed

## Argument Matching Rules
# Positional Arguments
def f(a, b, c):
    print(a, b, c)
    
f(1, 2, "Python")

# Keyword Arguments
f(c = "Python", a = 1, b = 2)

# Default Arguments
def f(a, b=2, c=3):
    print(a, b, c)
    
## Arbitrary Argument Lists
# *args — Collects positional arguments
def f(*args):
    print(args)

# **kwargs — Collects keyword arguments
def f(**kwargs):
    print(kwargs)

# Mixing Argument Types
def f(a, b, *args, c=10, **kwargs):
    ...

## Keyword-Only Arguments (Python 3)
# Keyword-Only with * 
def f(a, *, b, c):
    ...

f(1, b = 2, c = 3)

# Keyword-Only with *args
def f(*args, x, y):
    ...
    
## Argument Unpacking
# Unpacking when calling a function
args = (1, 2)
kwargs = {'c': 3}

f(*args, **kwargs)

# Unpacking in assignment
a, *b = [1,2,3,4]