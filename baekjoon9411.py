n=int(input())
for _ in range(n):
    i,mySum=1,0.0
    while i!=0:
        i=float(input())
        mySum+=i
    print(int(mySum) if mySum%1==0 else mySum)