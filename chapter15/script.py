# Python Documentation Sources
help(print)
help(list.append)

dir(str)
dir([])

# Docstring
def add(a, b):
    """Return sum of a and b"""
    return a + b

print(add.__doc__)
help(add)

add.__doc__ = "new doc"

def func(x):
    """
    Parameters:
        x (int): input
    Returns:
        int: output
    """
