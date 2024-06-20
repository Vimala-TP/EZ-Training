'''Create a Student class that holds the details of students like name,usn and the marks
in 5 subjects percentage and grade.
Create 5 student object and get the data for name usn and marks after that find the 
percentage and grade and store it to the class object'''
class Student:
    def __init__(self):
        self.name=input('Enter name =')
        self.usn=input('Enter usn =')
        self.m1=int(input('Enter s1 marks ='))
        self.m2=int(input('Enter s2 marks ='))
        self.m3=int(input('Enter s3 marks ='))
        self.m4=int(input('Enter s4 marks ='))
        self.m5=int(input('Enter s5 marks ='))
    def calculate(self):   
        p=((self.m1+self.m2+self.m3+self.m4+self.m5)/500)*100
        if p<=100 and p>80:
            grade='A'
        elif p<=80 and p>60:
            grade='B'
        elif p<=60 and p>30:
            grade='Pass'
        else:
            grade='Fail'
        print('Student name is ',self.name)
        print('Student usn is ',self.usn)
        print('Percentage of your marks is {}%'.format(p))
        print('Your grade is ',grade)
'''o1=Student()
o2=Student()
o3=Student()
o4=Student()
o5=Student()
o1.calculate()
o2.calculate()
o3.calculate()
o4.calculate()
o5.calculate()'''

n=int(input('Enter number of students ='))
print('Enter student details')
o=[]
for i in range(0,n):
    print('\nEnter student {} details'.format(i+1))
    o.append(i)
    o[i]=Student()
print('\n---Student Details---')
for i in range(0,n):
    print('\nStudent {} details'.format(i+1))
    o[i].calculate()    