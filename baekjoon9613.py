def gcd(a,b):
    a,b= b if a<b else a, a if a<b else b
    if b==0:return a
    return gcd(b,a%b)
t=int(input())
for _ in range(t):
    cmd=list(map(int,input().strip().split()))[1:]
    print(sum(gcd(cmd[i],cmd[j]) for i in range(len(cmd)) for j in range(i+1,len(cmd)) ))