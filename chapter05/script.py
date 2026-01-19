import math
import cmath

# formatting
num = 1.1 + 2.2

print('%e' % num)
print('%.1f' % num)

print(f'{num:e}')
print(f'{num:.2f}')

# comparison
A = 'code'
B = 'lemon'
C = 'python'
A < B < C

1 == 2 < 3 # (1 == 2) and (2 < 3)

# Correct way to handle real number comparisons
#1
int(1.1 + 2.2) == int(3.3)
#2
round(1.1 + 2.2, 1) == round(3.3, 1)
#3
math.isclose(1.1 + 2.2, 3.3)

# Division Operators
a = 10 / 4
b = 10 / 4.0

divmod(10, 3) # → (3, 1) similar to (10 // 3, 10 % 3)

math.floor(2.5) # → 2
math.floor(-2.5) # → -3

math.trunc(2.5) # → 2
math.trunc(-2.5) # → -2

# Complex numbers
z = 2 + -3j
print(z.real) # real part
print(z.imag) # imaginary part

cmath.sqrt(-1)
cmath.exp(1j)
cmath.sin(2+3j)
