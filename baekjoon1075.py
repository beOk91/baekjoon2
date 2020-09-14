n=int(input())
f=int(input())
print("%02d" %min(int(str(n+f-n%f)[len(str(n))-2:]),int(str(n-(f-n%f))[len(str(n))-2:])))