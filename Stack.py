class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.items)
print(s.pop())
print(s.items)