# while Loop
# Used when you don't know how many times the loop should run.
# It keeps running until the condition becomes False.
i = 1
while i <= 5:
    print(i)
    i += 1

password = ""

while password != "python":
    password = input("Enter Password: ")

print("Access Granted")