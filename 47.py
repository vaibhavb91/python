# Filter Function
# What is filter?
# filter() selects items based on a condition (True/False)

# filter(function, iterable)
nums = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))


nums = [10, 15, 20, 25]
result = filter(lambda x: x > 15, nums)
print(list(result))  