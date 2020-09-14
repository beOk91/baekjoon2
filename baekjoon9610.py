n=int(input())
m=[0]*5
for _ in range(n):
    a,b=map(int,input().strip().split())
    if a>0 and b>0:m[0]+=1
    elif a>0 and b<0:m[3]+=1
    elif a<0 and b>0:m[1]+=1
    elif a<0 and b<0:m[2]+=1
    else:m[4]+=1
print("Q1: {}".format(m[0])+"\n"+"Q2: {}".format(m[1])+"\n"+"Q3: {}".format(m[2])+"\n"+"Q4: {}".format(m[3])+"\n"+"AXIS: {}".format(m[4]))