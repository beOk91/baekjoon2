n,b=input().strip().split()
def conversion(n,b):
    a="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=0
    for i in range(len(n)):
        val=1
        for j in range(len(n)-1-i):
            val*=int(b)
        result+=a.index(n[i])*val
    return result
print(conversion(n,b))