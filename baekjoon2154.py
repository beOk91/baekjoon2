n=int(input().strip())
a="".join(str(i) for i in range(1,n+1))
print(a.index(str(n))+1)