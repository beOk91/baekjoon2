n=int(input())
for _ in range(n):
    text=list(map(int,input().strip().split()))
    avr=(sum(text)-text[0])/text[0]
    cnt=0
    for element in text[1:]:
        if element>avr:
            cnt+=1
    print("%.3f%%" %(cnt/text[0]*100))