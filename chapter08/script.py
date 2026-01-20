# List
L = [1, 2, 3]
L = list("abc")
L = []

L = [1, "hello", 3.14, [10, 20]]

L[0]      # first index
L[-1]     # last index
L[1:3]    # slice index 1 to 2

L[0] = 100
L[1:3] = [7, 8]

L1 = 'code'
L2 = 'python'

L1 + L2 # concatenate list
L * 3 # loop
for x in (L): # check element
    print(x)
len(L)

[x**2 for x in range(5)]

# Dictionary
D = {"name": "An", "age": 20}
D = dict(name="An", age=20)
D = {}

D["name"]
D["age"] = 21

{x: x*x for x in range(5)}

# Copy và aliasing
A = [1,2,3]
B = A        # same object
C = A[:]     # shallow copy

D2 = D.copy()
