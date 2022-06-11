def a(**n):
    print(type(a))
    print(a)
    for x in n.values():
        print(x)
a(a=10,b=20,c=30)
a(a=10,b=20)
a(a=10)
#if we use type n we get dict as class
