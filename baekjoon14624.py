n=int(input())
if n%2==0:
    print("I LOVE CBNU")
else:
    print("*"*n)
    for i in range((n+1)//2):
        print(" "*((n+1)//2-i-1)+"*"+" "*(i*2-1)+("*" if i!=0 else ""))



"""
        for j in range((n+1)//2-i-1):
            print(" ",end="")
        print("*",end="")
        for j in range(i*2-1):
            print(" ",end="")
            if j==i*2-2:
                print("*",end="")
        print()
"""