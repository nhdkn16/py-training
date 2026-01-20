# String Actions
len('abc')
'abc' + 'def'
'Py!' * 4

for c in "hacker":
    print(c)

'k' in "hacker"
'z' in "hacker"
'HACK' in 'abcHACKdef'

# Indexing và Slicing
S = "python"
S[0]
S[1:4]

# “Modifying” Strings
S = "spam"
S = S[:1] + "l" + S[2:]   # 'slam'
S = S.replace("s", "h")   # 'hpam'

# String Methods
S.replace("od", "ood")
S.split(",")

# Parsing text
S = "c,od,e"
S[2:4]            # 'od'
S.split(',')[1]   # 'od'

# String Formatting
age = 18

"%s = %d" % ("age", 20)
"{} = {}".format("age", 20)
f"{age = }"
