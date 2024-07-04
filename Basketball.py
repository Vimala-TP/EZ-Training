input1=int(input())                  #Number of Shots
input2=int(input())                  #Length of subarray
arr=list(map(int,input().split()))   #Subarray elements
mx=-1
for i in range(0,len(arr)-input2+1): 
    temp=arr[i:i+input2]
    k,s=1,0
    for j in temp: 
        s+=(j*k) 
        k+=1
    if s>mx:
        mx=s 
print(mx)








