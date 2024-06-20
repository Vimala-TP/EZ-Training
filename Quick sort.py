#Quick Sort
def Partition(l,low,high):
    j=low-1
    pi=high
    for i in range(low,high):
        if l[i]<l[pi]:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[pi],l[j]=l[j],l[pi]
    return j
def Quick_sort(l,low,high):
    if low<high:
        pi=Partition(l,low,high)
        Quick_sort(l,low,pi-1)
        Quick_sort(l,pi+1,high)
if __name__=="__main__":
    print('Enter the list to sort')
    l=list(map(int,input().split()))  
    Quick_sort(l,0,len(l)-1)
    print('Sorted List =',l)