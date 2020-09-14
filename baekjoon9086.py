n=int(input())
for _ in range(n):
    text=input()
    print(text*2 if len(text)==1 else text[0]+text[len(text)-1])