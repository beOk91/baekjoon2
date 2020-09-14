h=input().strip()
n=input().strip()
print(sum(1 if n == str(h[i:i+len(n)]) else 0 for i in range(len(h)-len(n)+1)))