#Printing n 
def fib(n1,n2,n):
    if n==1:
        print(n1,end=' ')
    else:
        print(n1,end=' ')
        fib(n2,n1+n2,n-1)
    return
if __name__=="__main__":
    n=int(input('Enter number of series ='))
    fib(0,1,n)