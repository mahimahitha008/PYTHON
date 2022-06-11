n=int(input("Please Enter Number of Employees:"))
m={}
i=1
while i<=n:
    ename=input('Enter Employee Name:')
    salary=int(input('Enter Salary:'))
    m[ename]=salary
    i=i+1
print(m)
for x in m:
    print(x,':',m[x])
