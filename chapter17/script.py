# import module
# module.variable

# Nested
def outer():
    x = 10
    def inner():
        print(x)

# Closures and Factory Functions
def maker(n):
    return lambda x: x + n

# The nonlocal Statement
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1

def f():
    f.count += 1
f.count = 0
