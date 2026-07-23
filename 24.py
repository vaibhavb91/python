# strip()
# Removes spaces from both sides.
text = "    Python    "
print(text.strip())

# Remove specific character
text1 = "*****Hello*****"
print(text1.strip("*"))

# Only Left Side
text = "     Python"
print(text.lstrip())

# Only Right Side
text = "Python      "
print(text.rstrip())