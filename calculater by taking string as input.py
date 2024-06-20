n='44+2'
o=['+','-','*','/']
n1=''
n2=''
ind=0
for i in n:
    if i in o:
        op=i
        break
    else:
        n1+=i
    ind+=1
for i in range(ind+1,len(n)):
    n2+=n[i]
match op:
    case '+':print(float(n1)+float(n2))
    case '-':print(float(n1)-float(n2))
    case '*':print(float(n1)*float(n2))
    case '/':print(float(n1)/float(n2))