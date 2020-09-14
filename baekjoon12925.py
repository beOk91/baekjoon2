t=int(input())
for i in range(1,t+1):
    n=int(input())
    val=int((3+5**0.5)**n)%1000
    print("Case #%d: %03d" %(i,val))
    """
    val=str(int((3+5**0.5)**n)%1000)
    print("Case #{}: ".format(i)+(3-len(val))*"0"+val)
    """