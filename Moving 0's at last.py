#Moving all 0's at last
l=[4,0,5,0,1,9,0,0]
j=0
for i in range(0,len(l)):
    if l[i]!=0:
        l[j]=l[i]
        j+=1
while j<len(l):
    l[j]=0
    j+=1
print(l)

l=[4,0,5,0,1,9,0,0]
for i in range(0,len(l)):
    for j in range(i,len(l)-1):
        if l[j]==0:
            p=j+1
            l[j]=l[p]
            l[p]=0
print(l)          