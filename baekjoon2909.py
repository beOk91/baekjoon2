c,k=input().strip().split()
if len(c)<int(k):
    print(0)
elif len(c)==int(k):
    print(str(10)+"0"*(int(k)-1) if int(c[0])>=5 else "0")
elif int(c[len(c)-int(k)])>=5:
    print(str(int(c[:len(c)-int(k)])+1)+"0"*int(k))
else:
    print(str(int(c[:len(c)-int(k)]))+"0"*int(k))