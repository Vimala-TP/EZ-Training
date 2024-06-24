#Insertion sort
l=[9,7,5,8,10,26,44,3,1]
for i in range(0,len(l)):
    curr=l[i]
    for j in range(i-1,-1,-1):
        if l[j]>curr:
            l[j],l[j+1]=l[j+1],l[j]
        else:
            l[j+1]=curr
            break
print(l)            