import sys
def f(num):
    if num==0 or num==1:
        return 1
    else:
        return num*f(num-1)
sys.setrecursionlimit(1000)
num=int(sys.stdin.readline().strip())
print(f(num))