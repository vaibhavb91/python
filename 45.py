# What is Lambda?
# A lambda function is a small anonymous (no name) function.
# Instead of writing full def, we write in one line.
# lambda arguments : expression

# normal function 
def add(a,b):
    return a + b

print(add(10,10))

add = lambda a,b: a + b
print(add(2,5))