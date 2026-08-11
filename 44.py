# Combined Example (Real Interview Style)
def demo(a, b=10, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

demo(5, 20, 30, 40, name="Vaibhav", city="Nashik")