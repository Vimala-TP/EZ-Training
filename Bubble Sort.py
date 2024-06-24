#Bubble Sort
l=[5,7,10,15,23]
for i in range(0,len(l)):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)