'''In the enchanted land of Numeria, Alice is on a quest to find the legendary 
Prime Key to unlock the ancient Vault of Secrets. The vault's guardian, an 
ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the 
Prime Key.
The puzzle consists of multiple levels, each requiring Alice to solve a different 
challenge involving prime numbers. To progress through each level, Alice must 
perform the following tasks:
Level 1: Find the smallest prime number larger than a given integer N.
Level 2: Calculate the sum of all prime numbers between N and the smallest 
prime number larger than N.
Level 3: Determine if the product of the smallest prime number larger than N
and the next immediate prime number is also a prime.
To complete the puzzle and retrieve the Prime Key, Alice must solve these 
challenges in sequence for a given integer N.
Your task is to write a function that takes an integer N and returns a tuple 
containing the following:
- The smallest prime number larger than N (Level 1 result).
- The sum of all prime numbers between N and the smallest prime number 
larger than N (Level 2 result).
- A boolean indicating whether the product of the smallest prime number 
larger than N and the next immediate prime number is prime (Level 3 result).
Help Alice navigate through the levels, solve the puzzle, and obtain the Prime 
Key to unlock the Vault of Secrets'''
def check_prime(n):
    f=0
    if n<1:
        f=1
    elif n==1:
        f=0
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                f+=1
                break
    if f==0:
        return True
    else:
        return False 
l=[]
n=int(input('Enter the number ='))
f=0
k=n+1
while f<1:
    f=check_prime(k)
    if f==1:
        l.append(k)
    else:
        k+=1
sum=0
for i in range(n,k+1):
    sum+=i
l.append(sum)
p1=k
f=0
k=p1+1
while f<1:
    f=check_prime(k)
    if f==1:
        p2=k
    else:
        k+=1
p=p1*p2
f=check_prime(k)
l.append(f)
print(tuple(l))