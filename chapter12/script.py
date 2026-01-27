# if statement
if x > 0:
    print("Positive")

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
    
# and, or, not
if age >= 18 and age < 65:
    print("Working age")
    
# Short-circuit:
x != 0 and y/x > 2

# Conditional expression (ternary)
result = "Pass" if score >= 5 else "Fail"

# match / case
# match value:
#     case pattern1:
#         ...
#     case pattern2:
#         ...
#     case _:
#         ...
