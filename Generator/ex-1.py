def gen_mon():
    print("Generating Months:")
    yield "January"
    yield "February"
    yield "March"
    yield "April"
    yield "May"
    yield "June"
    yield "July"
    yield "August"
    yield "September"
    yield "October"
    yield "November"
    yield "December"
g= gen_mon()
print(type(g))
print(g)
for x in g:
    print(x)