## Comprehensions
# From maps/filters to comprehensions
res = []
for x in 'text':
    res.append(ord(x))
    print(res)
    
list(map(ord, 'text'))

[ord(x) for x in 'text']

# The power of list comprehensions
# Apply any expression
[x ** 2 for x in range(10)]

list(map(lambda x: x ** 2, range(10)))

# Combine map and filter in one expression
[x ** 2 for x in range(10) if x % 2 == 0]

list(
    map(lambda x: x**2,
        filter(lambda x: x % 2 == 0, range(10)))
)

# The official syntax of comprehension
# Basic form
# [expression for target in iterable]

# General form
# [
#   expression
#   for target1 in iterable1 if condition1
#   for target2 in iterable2 if condition2
#   ...
# ]

## Generator Functions and Expressions
# Generator Functions
def gensquares(n):
    for i in range(n):
        yield i ** 2
        
# Generator and iteration protocol
x = gensquares(3)
next(x)  # 0
next(x)  # 1
next(x)  # 4
next(x)  # StopIteration

# Generator extension protocol
def both(n):
    yield from range(n)
    yield from (i*i for i in range(n))
    
# Generator Expressions
(x ** 2 for x in range(5))
[x ** 2 for x in range(5)]

# Generator vs map / filter
# map
map(lambda x: x*2, data)
# Generator expression
(x*2 for x in data)

## Asynchronous Functions (async / await)
async def f():
    await asyncio.sleep(2)

asyncio.run(main())

# Tasks
task = asyncio.create_task(producer())
