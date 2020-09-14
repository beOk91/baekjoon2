n=int(input())
for _ in range(n):
    text=input()
    print("Do-it" if text[len(text)//2-1]==text[len(text)//2] else "Do-it-Not")