n=int(input())
for _ in range(n):
    text=input()
    idx=0
    myScore=0
    for element in text:
        if element =="O":
            idx+=1
            myScore+=idx
        else:
            idx=0
    print(myScore)