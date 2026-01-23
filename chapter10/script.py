# Assignment statements
x = 10
a, b = 1, 2
x += 1

# Selection statements
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Loop statements
for i in range(5):
    print(i)

while x > 0:
    x -= 1
    
# Loop control
for i in range(5):
    if i == 3:
        break
else:
    print("No break")
    
# Function statements
def add(a, b):
    return a + b

# Module statements
import math
from math import sqrt

# Exception handling
try:
    x = int(input())
except ValueError:
    print("error")
finally:
    print("done")
    
# Context manager
with open("a.txt") as f:
    data = f.read()

# Class statements
class Person:
    pass

# Program termination
# return
# raise
# exit()

# Block and indentation
if x > 0:
    print(x)
    print("done")

# Compound vs Simple statements
# Simple
x = 1
print(x)
# Compound
if x > 0:
    print(x)
    
# Nested statements
if x > 0:
    for i in range(x):
        if i % 2 == 0:
            print(i)
