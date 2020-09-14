import sys
"""
def conversion(n1,n2):
    if n1<n2:return str(n1)
    else:return conversion(n1//n2,n2)+str(n1%n2)
result=0
n=int(sys.stdin.readline().strip())
result=sum(i for i in range(1,2**n))
print(conversion(result,2))
"""
n=int(sys.stdin.readline().strip())
print("1"*n+"0"*(n-1))