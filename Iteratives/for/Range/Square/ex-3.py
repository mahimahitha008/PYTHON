n=int(input("Please Enter number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j), end=" ")
    print()