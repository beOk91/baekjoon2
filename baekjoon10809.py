text=list(input())
for i in range(97,123):
    for j in range(len(text)):
        if text[j]==chr(i):
            print(j,end=" ")
            break
        elif j==(len(text)-1) and text[j]!=chr(i):
            print(-1,end=" ")