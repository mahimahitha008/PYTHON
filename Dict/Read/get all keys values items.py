emp= {'id':101, 'name':"Rahul", 'Sal':45000}
print(emp.get('id'))    
print(emp.get('name'))
print(emp.get('Sal'))
print(emp.get('noida'))     # if key is not available it will give none
print(emp.get('yaari'))
print(emp.get('save'))


print(emp.keys())
for x in emp.keys():
    print(x)
    
print(emp.values())
for v in emp.values():
    print(v)
print(emp.items())
for y in emp.items():
    print(y)
