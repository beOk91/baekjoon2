n=int(input())
for _ in range(n):
    num=int(input())
    sum1=0
    for i in range(1,num+1):
        if i%2!=0:
            sum1+=i
    print(sum1)