min_bal=5000     #global variable
def savings_account():
    min_bal=500       #local variable
    print(min_bal)
def current_account():      #here global variable act as local variable
    print(min_bal)     
savings_account()
current_account()
