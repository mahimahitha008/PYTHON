def outer():
    print("Outer Function")
    def inner():
        print("Inner Function")
    inner()
    inner()    
outer()
#inner()        ##we cant call iner function outside