# Tuple
T = (1, 2, 3)
T = 1, 2, 3

print(T[0])
print(T[1:])
print(len(T))

# unpacking
a, b, c = (1, 2, 3)
a, b = b, a

# File Object
f = open("data.txt", "r")
f.read()
f.readline()
f.readlines()

for line in f:
    print(line)

f.write("Hello\n")

f.close()
with open("data.txt") as f:
    data = f.read()

open("a.txt", encoding="utf-8")

# Set
S = {1, 2, 3}

# Boolean
True, False
True == 1
False == 0

# None
x = None

# Bytes & Bytearray
b = b"abc"

# Data types and references
A = [1,2]
B = A
B[0] = 9
