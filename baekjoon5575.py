for _ in range(3):
    h1,m1,s1,h2,m2,s2=map(int,input().strip().split())
    time=h2*3600-h1*3600+m2*60-m1*60+s2-s1
    print(time//3600,time%3600//60,time%3600%60)