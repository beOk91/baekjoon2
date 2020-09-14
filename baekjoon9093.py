t=int(input())
for _ in range(t):
    text=input().strip().split()
    print(" ".join(element[::-1] for element in text))