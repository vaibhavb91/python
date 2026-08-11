# *args allows you to pass multiple values (any number) to a function.
# It stores values as a tuple
# Useful when you don’t know how many arguments will come
def add_number(*args):
    total=0
    for num in args:
        total += num
    return total

# args = (2, 4, 6) → tuple
print(add_number(2,2,2,2,2)) 