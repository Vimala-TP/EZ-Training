a=4
b=5
l1=list(range(a-1,-1,-1))
print(l1)
l2=list(range(b-1,-1,-1))
print(l2)
for x in zip(l1,l2):
    print(x)