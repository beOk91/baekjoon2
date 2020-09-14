n=int(input())
for _ in range(n):
    arr=list(map(int,input().strip().split()))
    print(sum(element if element%2==0 else 0 for element in arr),min([element for element in arr if element%2==0]))