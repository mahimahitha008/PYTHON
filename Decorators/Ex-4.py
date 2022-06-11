def to_lower(func):
    def inner():
        return func().lower()
    return inner
@to_lower
def to_Upper():
    return "HELLO,RAGHUL!"
print(to_Upper())