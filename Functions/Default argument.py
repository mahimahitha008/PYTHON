def add(a,b=20):
    return a+b
a=add(10,20)
print(a)
b=add(10)
print(b)


def add(b,a=100):
    return a+b
a=add(100,50)
print(a)
b=add(50)
print(b)
#here in case if we not provide any of the value it takes default value as the original value 
