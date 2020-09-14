def sosu(n):
    cnt=0
    for i in range(1,n+1):
        if cnt>2:
            return False
        if n%i==0:
            cnt+=1
    return True

while True:
    a=int(input())
    if a==0:
        break
    for i in range(3,a,2):
        if sosu(a-i):
            print("{} = {} + {}".format(a,i,a-i))
            break
        if i==a-1:
            print("Goldbach's conjecture is wrong.")