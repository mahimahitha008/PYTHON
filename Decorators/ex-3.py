def simple_div(func):
    def inner(a,b):
        if b==0:
            return "Cannot Divide by Zero"
        else:
            return func(a,b)
    return inner
@simple_div

def div(a,b):
    return a/b
print(div(10,5))
print(div(10,0))    #actually here we get erroer can be modified by decorator as our own statement