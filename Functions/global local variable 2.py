def func1():
    a=10
    global b     #here global function act as default and can be used n nymber of times
    b=20
    print(a)
    print(b)
def func2():
    #print(a)     #here a is local variable so it is getting error while printing
    print(b)      #using global key we can get value of b
func1()
func2()
    
