#Count Sort 
l=[2,5,3,4,2,7,5,8,5]
print('List before Sorting = ',l)
n=max(l)
a=[0]*n
for i in l:
    a[i-1]+=1
print('Count of each digit from 1 to ',n,' = ',a)
l=[]
for i in range(0,n):
    l+=[i+1]*a[i]
print('List after Sorting = ',l)