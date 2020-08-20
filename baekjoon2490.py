for _ in range(3):
    arr=list(map(int,input().strip().split()))
    if sum(arr)==3:
        print("A")
    elif sum(arr)==2:
        print("B")
    elif sum(arr)==1:
        print("C")
    elif sum(arr)==0:
        print("D")
    else:
        print("E")