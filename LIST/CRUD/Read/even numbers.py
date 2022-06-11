l=list(range(100))
print(l)
'''
for x in range(0,100,2):
  print(x)
'''
'''
for x in l:
    if x%2==0:
        print(x)
'''
'''i=0
while i<=len(l)-1:
    print(l[i])
    i=i+2
'''

i=0
while i<=len(l)-1:
    if len(l)%2==0:
        print(l[i])
        i=i+2
