#Finding the index of first letter of the pattern in the given string
S=input('Enter the String =')
P=input('Enter the Pattern =')
li=[]
f=0
for i in range(0,len(S)-(len(P)-1)):
    a=''
    for j in range(0,len(P)):
        a+=S[i+j]
    if a==P:
        li.append(i)
        f+=1
if f==0:
    print('Pattern not found')
else:
    print('Pattern is at index =',li)