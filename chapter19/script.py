## Recursion
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
## Short and generalized versions
# first, *rest = L
# return first if not rest else first + mysum(rest)

## Direct and indirect recursion
def mysum(L):
    return nonempty(L)

def nonempty(L):
    return L[0] + mysum(L[1:])

## When recursion is necessary: ​​nested structures
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

# Function Introspection
def func(a):
    b = 'Hack'
    return b * a

# Function Attributes
def func(): pass
func.count = 0
func.count += 1

# Function Annotations
# def func(a: 'hack', b: (1, 10), c: float) -> int:
#     ...

# Decorators
# @decorator
# def func(...):
#     ...
# or:
# def func(...):
#     ...
# func = decorator(func)

## lambda
# Syntax: lambda arg1, arg2, ..., argN : expression
func = lambda x, y, z: x + y + z

x = lambda a='hack', b='python', c='code': a + b + c
x('write')   # 'writepythoncode'

# List
L = [
    lambda x: x * 2,
    lambda x: x ** 2,
    lambda x: x // 2
]

for f in L:
    print(f(5))

# Dictionary
key = 'loop'

{
    'hack': lambda s: s.upper(),
    'code': lambda s: s.lower(),
    'loop': lambda s: f'{s * 4}!'
}[key]('Py')

# Multiple actions
lambda a, b: (print(a), print(b))

# if / else
lambda x, y: x if x < y else y

# List comprehension
lambda x: [print(i) for i in x]

# map
lambda x: list(map(print, x))

# Assignment with :=
lambda x: (res := x + 1) + res
