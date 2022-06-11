def a():
    print("GM")
    def b():
        print("GN")
    return b
add=a()
add()
print(a)
print(a())
print(add())
