#WAP to print minimun number among 3 numbers
a = int(input("Please Enter the Value:"));
b = int(input("Please Enter the Value:"));
c = int(input("Please Enter the Value:"));
min= a if a<b and a<c else b if b<c else c
print("Minimum Nuber:" , min)