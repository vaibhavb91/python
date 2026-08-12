# Map Function
# map() apply a function to each item in a list
# map(function, iterable)

num = [10,20,30,40,50]

result = map(lambda x:x * 2,num)
print(list(result))

# Example 2 (without lambda)
def square(x):
    return x * x

nums = [1, 2, 3]

result = map(square, nums)
print(list(result))