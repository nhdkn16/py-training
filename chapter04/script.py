import math
import random

# Number
print(123 + 456)
print(2 ** 10)

print(math.pi)
print(math.sqrt(49))

print(random.choice([1, 2, 3, 4, 5]))

# Strings
s = 'code'
print(len(s))
print(s[0])
print(s[-2])
print(s[1:3])
print(s + 'xyz')
print(s.find('od'))
print(s.replace('od', 'abc'))

line = 'aaa, bbb, ccc, ddd'
print(line.split(','))

# Lists
l = [123, 'text', 1.23]
print(len(l))
l.append('Py')
l.pop(2)

m = ['bb', 'aa', 'cc']
m.sort()
m.reverse()

M = [[1,2,3],[4,5,6,],[7,8,9]]
col2 = [row[1] for row in M]
print(col2)

diag = [M[i][i] for i in [0,1,2]]
print(diag)

# Dictionary
D = {'name': 'Pat', 'job': 'dev', 'age': 40}

E = {}
E['name'] = 'Pat'
E['job'] = 'dev'
E['age'] = 40

pat1 = dict(name='Pat', job='dev', age=40)
pat2 = dict(zip(['name', 'job', 'age'], ['Pat', 'dev', 40]))

rec = {
    'name': {'first': 'Pat', 'last': 'Smith'},
    'jobs': ['dev', 'mgr'],
    'age': 40.5
}

# Tuples
T = (1, 2, 3, 4)
T = 1, 2, 3, 4
T = (2,)

len(T)
T + (5, 6)
T[0] # index
T[1:] # slice

T.index(4)
T.count(4)

T.index(4)   # index of '4'
T.count(4)   # Number appearance

T = ('hack', 3.0, [11, 22, 33])

# Files
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world!\n')
f.close()

f = open('data.txt', 'r')
text = f.read()
text.split()
print(text)

for line in open('data.txt'):
    print(line.rstrip())
