# Assignment Statements
x = 10
x = 5
a = b = c = 0

a, b = 1, 2
x, y, z = [10, 20, 30]

a, b = b, a

a, *b, c = [1, 2, 3, 4, 5]
# a=1, b=[2,3,4], c=5

x += 1
x *= 2
x -= 3

if (n := len(data)) > 10:
    print(n)

x = 5
x += 1   # tạo object mới

a = [1,2]
b = a
b.append(3)   # a cũng thay đổi

2 + 3
func()

# Print structure
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout)

print(1, 2, 3)                 # 1 2 3
print(1, 2, 3, sep=',')        # 1,2,3
print("Hello", end='')         
print("World")                # HelloWorld

# Redirect output
f = open("out.txt", "w")
print("Hello", file=f)
f.close()
