# Variables, Objects, References
a = 3
a = "text"

# Shared references
a = [1, 2]
b = a

b[0] = 99
b = [3, 4]

# Copy vs Reference
b = a[:]   # copy list

# Type hinting
a: int = 5
