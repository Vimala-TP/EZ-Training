n=int(input())                     #Enter length of list
l=list(map(int,input().split()))   #Enter the list containing  1 and -1 
c=r=0
for i in range(0,n):
    c+=l[i]
    if c==0:
        r+=1
print(r)





















