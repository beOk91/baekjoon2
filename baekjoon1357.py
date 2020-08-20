x,y=input().strip().split()
print(int(str(int(x[::-1])+int(y[::-1]))[::-1]))