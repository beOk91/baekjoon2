arr=list(map(int,input().strip().split()))
n=int(input())
cnt=sum(1 for element in arr if element>n)
print("A+" if cnt<=4 else "A0" if cnt<=14 else "B+" if cnt<=29 else "B0" if cnt<=34 else "C+" if cnt<=44 else "C0" if cnt<=47 else "F" )