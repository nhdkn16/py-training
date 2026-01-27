# while loop
# while condition:
#     statements
# else:
#     statements

x = 3
while x > 0:
    print(x)
    x -= 1
print("Done")

while x > 0:
    if x == 2:
        break
    x -= 1
else:
    print("Loop finished")
    
# for loop
# for var in iterable:
#     statements
# else:
#     statements

for c in "python":
    print(c)

for x in [1, 2, 3]:
    print(x)

for x in [1, 3, 5]:
    if x % 2 == 0:
        break
else:
    print("No even number")

# range()
# for i in range(5):       # 0 → 4
# for i in range(1, 5):    # 1 → 4
# for i in range(0, 10, 2) # bước 2

# enumerate()
# for index, value in enumerate(["a", "b", "c"]):

# zip()
# for a, b in zip([1,2], [3,4]):

# reversed() and sorted()
# for x in reversed(list):
# for x in sorted(list):

# Dictionary loops
# for k in dict:
# for v in dict.values():
# for k, v in dict.items():

nums = [1, 3, 5, 7]

for n in nums:
    if n % 2 == 0:
        print("Even found")
        break
else:
    print("All odd")
