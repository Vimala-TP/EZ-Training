#Recursion
#finding the factorial
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#Finding nth fibonacci number 
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

#Finding power
def p(m,n):
    if n==0:
        return 1
    else:
        return m*p(m,n-1)
print(p(2,3))  

#Sum of digits of a given number
def sd(n):
    if n==0:
        return 0
    else:
        return n%10+sd(n//10)
print(sd(1234))   

#Sum of digits of a given number
def sd(n):
    if n==0:
        return 0
    else:
        return n%10+sd(n//10)
print(sd(1234))   