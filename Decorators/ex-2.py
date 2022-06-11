def to_UPPER(func):
    def inner():
        return func().upper()
    return inner
    
@to_UPPER
def to_lower():
    return "Hello, Raghul!"
print(to_lower())