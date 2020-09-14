l=int(input())
b=int(input())
a=int(input())
c=int(input())
d=int(input())
b= b//c+1 if b%c!=0 else b//c
a= a//d+1 if a%d!=0 else a//d
print(l-max(b,a))