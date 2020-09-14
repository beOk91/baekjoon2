a,b=map(int,input().strip().split())
print(abs((4 if a%4==0 else a%4) -(4 if b%4==0 else b%4))+ abs((a//4 if a%4==0 else a//4+1)- (b//4 if b%4==0 else b//4+1)))