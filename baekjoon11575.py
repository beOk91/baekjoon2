import sys
t=int(sys.stdin.readline().strip())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().strip().split())
    text=sys.stdin.readline().strip()
    new_s=""
    for e in text:
        new_s+=chr((a*(ord(e)-65)+b)%26+65)
    print(new_s)