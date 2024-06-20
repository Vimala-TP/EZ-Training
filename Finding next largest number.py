#Without stack
l1=[3,5,2,14,5,3,7,9,4,6,4,2,5,3]
l2=[]
for i in range(0,len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]<l1[j]:
            l2.append(l1[j])
            break
        if len(l1)-1==j:
            l2.append(-1)
l2.append(-1)
print(l2)

#With stack
def find_next_largest_right(arr):
    n = len(arr)
    result = [-1] * n      
    stack = []    
    for i in range(n - 1, -1, -1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()        
        if stack:
            result[i] = stack[-1]        
        stack.append(arr[i])    
    return result
arr = [3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
output = find_next_largest_right(arr)
print(output)