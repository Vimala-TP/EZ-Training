#Single Inheritance
class c1:
    def st(self):
        print('Class c1')
class c2(c1):
    print('Class c2')
o=c2()
o.st()

#Multilevel Inheritance
class c1:
    def st(self):
        print('Class c1')
class c2(c1):
    print('Class c2')
class c3(c2):
    pass
o=c3()
o.st()

#Multiple Inheritance
class c1:
    def st(self):
        print('Class c1')
class c2():
    def st1(self):
        print('Class c2')
class c3(c1,c2):
    pass   
o=c3()
o.st()
o.st1()

#Hierarchical inheritance
class c1:
    def st(self):
        print('Class c1')
class c2(c1):
    print('Class c2')
class c3(c1):
    pass
o1=c2()
o1.st()
o2=c3()
o2.st()

