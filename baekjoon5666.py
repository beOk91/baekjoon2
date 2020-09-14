try:
    while True:
        a,b=map(int,input().strip().split())
        print("%.2f" %(a/b))
except:
    exit()