n=int(input())
round1=list(map(int,input().strip().split()))
round2=list(map(int,input().strip().split()))
print(sum(i if i>0 else i*-1 for i in round1)-sum(i if i<0 else i*-1 for i in round2))