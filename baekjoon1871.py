def conversion(n1):
    n1,result=n1[::-1],0
    for i in range(len(n1)):
        a=1
        for _ in range(i):
            a*=26
        result+=(ord(n1[i])-65)*a
    return result
n=int(input())
for _ in range(n):
    a,b=input().strip().split("-")
    print("nice" if abs(conversion(a)-int(b))<=100 else "not nice")