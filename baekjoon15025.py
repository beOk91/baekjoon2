a,b=map(int,input().strip().split())
print("Odd {}".format (max(a,b)*2) if a!=b else "Not a moose" if a==0 and b==0 else "Even {}".format(b*2))