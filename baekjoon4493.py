n=int(input())
for _ in range(n):
    arr=[0]*2
    cnt=int(input())
    for _ in range(cnt):
        p1,p2=input().strip().split()
        if p1=="R":
            if p2=="P":
                arr[1]+=1
            elif p2=="S":
                arr[0]+=1
        elif p1=="P":
            if p2=="S":
                arr[1]+=1
            elif p2=="R":
                arr[0]+=1
        else:
            if p2=="P":
                arr[0]+=1
            elif p2=="R":
                arr[1]+=1
    print("Player 1" if arr[0]>arr[1] else "Player 2" if arr[0]<arr[1] else "TIE")