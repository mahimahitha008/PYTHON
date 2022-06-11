def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    return inner
a=outer()
a()
print(a)
print(a())