while True:
    b,n=map(int,input().strip().split())
    if b==0 and n==0:
        break
    print(int(b**(1/n)))
    """
1 **3 = 1
2 ** 3 = 8
"""