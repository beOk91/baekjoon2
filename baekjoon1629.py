import sys
a,b,c=map(int,sys.stdin.readline().strip().split())
def f(a,b,c):
    if b==0:return 1
    if b%2==1:return a*f(a,b-1,c)%c
    else:
        a1=f(a,b/2,c)
        return (a1*a1)%c
print(f(a,b,c))