a,b,c=map(int,input().strip().split())
result=0
day=0
while result<c:
    result+=a
    day+=1
    if day%7==0:
        result+=b
print(day)