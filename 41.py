# **kwargs (Variable Keyword Arguments)
# **kwargs allows passing multiple named arguments
# Stored as a dictionary
# Key = parameter name, Value = value

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key, ":", value)

student_info(name="Vaibhav", age=25, city="Nashik")