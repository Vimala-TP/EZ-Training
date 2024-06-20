"""
Context:
A financial services company, FutureInvest, uses advanced mathematical models to forecast market trends and make
 investment decisions. One of the models they use is based on the Fibonacci sequence due to its relevance in
 technical analysis, particularly in identifying retracement levels and predicting future price movements.
Scenario:
FutureInvest analysts need a reliable tool that can generate the Fibonacci sequence up to a specified number of
 terms. This tool will help them in creating Fibonacci retracement levels, which are critical for predicting
 potential reversal points in the financial markets. The accuracy and efficiency of generating these sequences
 are crucial for timely and effective decision-making•
"""
n=int(input('Enter number of fibonacci series ='))
n1=0
n2=1
n3=0
if n==1:
    print(n1)
elif n==2:
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    for i in range (2,n):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3