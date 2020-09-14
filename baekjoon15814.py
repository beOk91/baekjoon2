import sys
text=list(sys.stdin.readline().strip())
t=int(sys.stdin.readline().strip())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().strip().split())
    text[a],text[b]=text[b],text[a]
print("".join(str(e) for e in text))