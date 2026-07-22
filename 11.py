# Strings are Immutable
# Once a string is created, you cannot change individual characters.
# name = "Python"

# name[0] = "J"

# output
# TypeError: 'str' object does not support item assignment
name = "Python"

name = "J" + name[1:]

print(name)

