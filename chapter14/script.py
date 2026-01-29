# Iterator
# __iter__()
# __next__()

L = [1,2,3]
I = iter(L)
next(I)

for line in open("file.txt"):
    print(line.upper(), end='')
    
# List Comprehension
[x**2 for x in range(5)]
    # Conditional
[x for x in range(10) if x % 2 == 0]
    # Nested comprehensions
[(x,y) for x in range(3) for y in range(2)]
    # Set & Dict comprehensions
{x*x for x in range(5)}
{x: x*x for x in range(5)}
    # Generator expressions
(x*x for x in range(5))
