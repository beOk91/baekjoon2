import sys
def f(num):
    if num<=1:
        return str(num)
    return f(num//2)+str(num%2)
n=int(sys.stdin.readline().strip())
print(int(str(f(n))[::-1],2))