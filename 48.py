# Reduce Function
# reduce() applies a function cumulatively (step by step)
# It reduces list → single value
# from functools import reduce
from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result) 



nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)  

# How reduce works:
# For [1,2,3,4]
# Step 1 → 1+2 = 3
# Step 2 → 3+3 = 6
# Step 3 → 6+4 = 10