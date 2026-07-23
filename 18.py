# String operation or method
# Note: Strings are immutable, meaning methods do not change the original string. 
# They return a new string.

name = "vaibhav"
print(name.upper())
print(name.lower())
# Original string remains unchanged.

name = "vaibhav"
new_name = name.upper()

print(name)
print(new_name)

username = input("Enter username: ")

print(username.upper())