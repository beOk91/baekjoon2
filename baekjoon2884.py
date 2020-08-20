hour,minute=map(int,input().strip().split())
sum1=hour*60+minute-45
print((sum1//60+24)%24,sum1%60)