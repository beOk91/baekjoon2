a1,p1=map(int,input().strip().split())
r1,p2=map(int,input().strip().split())
print("Whole pizza" if r1*r1*3.14159265359/a1*p1>p2 else "Slice of pizza")