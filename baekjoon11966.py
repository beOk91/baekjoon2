n=int(input())
while n%2==0:
    if n%2!=0 or n==2:
        break
    else:
        n/=2
print(1 if n==2 or n==1 else 0)