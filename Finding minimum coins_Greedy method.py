#Given coins as 1,5 and 7, the bill will be 18, Find the minimum coins to pay the bill
coins=[1,5,7]
coins.sort(reverse=True)
bill=18
l=[]
i=0
while bill!=0:
    if coins[i]<=bill:
        bill-=coins[i]
        l.append(coins[i])
    else:
        i+=1
print(l)