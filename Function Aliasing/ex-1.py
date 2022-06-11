def add():
    print("Good Morning")
a=add
a()
add()
print(id(a))
print(id(add))   #same id or memory adress as here aliasing takes place
