m,n=map(int,input().strip().split())
def conversion(m,n):
    c="0123456789ABCDEF"
    if m<n:
        return str(c[m])
    else:
        return conversion(m//n,n)+str(c[m%n])
print(conversion(m,n))