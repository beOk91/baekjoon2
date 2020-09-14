while True:
    try:
        n,k=map(int,input().strip().split())
        cnt,stamp=n,n
        while stamp>=k:
            cnt+=stamp//k
            stamp=stamp-stamp//k*k+stamp//k
        print(cnt)
            
    except:
        break