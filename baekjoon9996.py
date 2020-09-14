n=int(input())
pattern=input().strip().split("*")
for _ in range(n):
    text=input().strip()
    print("DA" if text.index(pattern[0])<text.index(pattern[1]) else "NE")