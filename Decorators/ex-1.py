def special(func):
    def inner(name):
        if name=="Modi":
            print("Hello, PM Good Morning!")
        else:
            func(name)
        return inner
@special
#This is original function in which we added the above decorator
def employee(name):
    print("Hello!,",name,"Good Morning")
employee("Raghul")
employee("Priyanka")
employee("Sonia")
employee("Modi")