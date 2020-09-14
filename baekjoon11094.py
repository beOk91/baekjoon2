n=int(input())
for _ in range(n):
    text=input()
    if "Simon says" in text:print(text[text.index("Simon says")+len("Simon says"):])