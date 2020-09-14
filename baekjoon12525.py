t=int(input())
for i in range(1,t+1):
    text=input().strip()
    print("Case #{}: ".format(i)+text+" is ruled by "+("nobody." if text[-1] in ["y","Y"] else "a queen." if text[-1] in ["a","e","i","o","u","A","E","I","O","U"] else "a king."))