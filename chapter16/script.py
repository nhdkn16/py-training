# Function
# def name(arg1, arg2, ...):
#     statements
#     return value

def add(a, b):
    return a + b

result = add(3, 4)
print(result)

def f():
    pass

print(f())  # None

# Parameters: names in the definition
# Arguments: values ​​when calling
def square(x):
    return x * x

square(5)

def f():
    return "hi"

g = f
print(g())

# Local Variables
def test():
    x = 10

test()
# print(x)  -> lỗi

# Global Variables
x = 5

def f():
    global x
    x = 10

# lambda
# lambda arg1, arg2, ..., argN: expression
add = lambda x, y: x + y
print(add(3, 4))
