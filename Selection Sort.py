#Selection sort
l=[9,7,5,8,10,26,44,3,1]
for i in range(0,len(l)):
    pos=i
    min=l[pos]
    for j in range(i,len(l)):
        if min>l[j]:
            min=l[j]
            pos=j
    l[i],l[pos]=l[pos],l[i]
print(l)