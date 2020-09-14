n=int(input())
for _ in range(n):
    text=input().strip()
    if text[0].isalpha():print("skipped")
    else:a,b=map(int,text.split("+"));print(a+b)