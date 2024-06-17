l=[2,1,0,1,1,2,0,0]
c0=0
c1=0
c2=0
for i in range(0,len(l)):
    if l[i]==0:
        c0+=1
    if l[i]==1:
        c1+=1
    if l[i]==2:
        c2+=1
j=0
print(c0,c1,c2)
while c0>0:
    l[j]=0
    j+=1
    c0-=1
while c1>0:
    l[j]=1 
    j+=1 
    c1-=1 
while c2>2:
    l[j]=2 
    j=j+1
    c2-=1 
print(l)