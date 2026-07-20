# A Data Type tells Python what kind of value is stored in a variable.
# int , float , complex , str , bool , list , tuple , set , dict , NoneType
age = 25
print(age)
print(type(age))

# float 
b = 10.0
print(type(b))

# String (str)
name = "Vaibhav"
print(type(name))

# Boolean
is_student = True
print(type(is_student))

# Complex Number -> used in mathematics
a = 5 + 4j

print(type(a))

# List -> Stores multiple values.
# Lists are mutable, meaning you can change them.
fruits = ["Apple", "Banana", "Orange"]
fruits[0] = "Mango"
print(fruits)
print(type(fruits))

# Tuple -> Looks like list Uses parentheses ()
numbers = (10,20,30)
# Tuple is immutable.
# TypeError: 'tuple' object does not support item assignment
# numbers[0] = 100
print(type(numbers))

# Set -> Stores unique values.{}
numbers = {10,20,30,10,20}

print(numbers)

# Dictionary
# Stores data as key : value pairs.
student = {
    "name":"Vaibhav",
    "age":25,
    "city":"Nashik"
}

print(student)
print(student["name"])

# None Type
# Useful when a variable doesn't have a value yet.
a = None

print(type(a))