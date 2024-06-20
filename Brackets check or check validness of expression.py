#Checking whether the given expression is valid or not(brackets check)
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
exp=input('Enter the expression =')
s=Stack()
f=0
dic={')':'(',
     ']':'[',
     '}':'{'}
for i in exp:
    if i=='(' or i=='[' or i=='{':
        s.push(i)
    elif i==')' or i==']' or i=='}':
        a=s.pop()
        if dic[i]==a:
            pass
        else:
            f+=1
            break
if f==0 and s.items==[]:
    print('Valid expression')
else:
    print('Invalid expression')