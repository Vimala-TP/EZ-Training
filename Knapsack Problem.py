#Knapsack problem
p=[20,10,6,9,18,12,16,30,15]
w=[4,5,6,3,2,5,4,6,6]
d={}
for i in range(0,len(p)):
    c=p[i]/w[i]
    d[i+1]=c
print('Profit/Weight = ',d)
cap=30
pr=0
items=[]
while cap!=0:
    max=0
    for i in d:
        if max<d[i]:
            max=d[i]
            j=i
    cap-=w[j-1]
    pr+=p[j-1]
    d[j]=0
    items.append(j)
print('Items selected = ',items)
print('Maximum profit = ',pr)