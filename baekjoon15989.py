import sys
def f(num,arr):
    if sum(arr)==num:
        result.add(" ".join(str(e) for e in sorted(arr)))
    if sum(arr)<num:
        for i in range(1,4):
            f(num,arr+[i])
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    result=set([])
    f(n,[])
    print(len(result))