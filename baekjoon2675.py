n=int(input())
for _ in range(n):
    text=input().strip().split()
    for element in text[1]:
        for _ in range(int(text[0])):
            print(element,end="")
    print()