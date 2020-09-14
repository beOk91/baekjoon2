n=int(input())
for _ in range(n):
    m=(bin(int(input()))[2:])[::-1]
    print(" ".join(str(i) for i in range(len(m)) if m[i]=="1"))