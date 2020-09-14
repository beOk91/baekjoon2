n=int(input())
spot_sum=0
for i in range(1,n+1):
    for j in range(i,i*n+1):
        spot_sum+=j
print(spot_sum)