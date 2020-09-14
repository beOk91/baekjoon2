n,a,b=map(int,input().strip().split())
s=list(input())
print("".join(s[0:a-1]+s[a-1:b][::-1]+s[b:]))