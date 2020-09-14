n=int(input())
for _ in range(n):
    text=input().strip()
    text=text.replace(" ","")
    cnt=0
    for element in text:
        if element in ["A","E","I","O","U","a","e","i","o","u"]:
            cnt+=1
    print(len(text)-cnt,cnt)