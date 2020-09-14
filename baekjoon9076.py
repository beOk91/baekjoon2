t=int(input())
for _ in range(t):
    s=list(map(int,input().strip().split()))
    s.remove(max(s));s.remove(min(s))
    print("KIN" if max(s)-min(s)>=4 else str(sum(s)))