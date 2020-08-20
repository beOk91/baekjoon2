a=int(input())
b=int(input())
c=int(input())
abc=str(a*b*c)
arr=[0]*10
for element in abc:
    arr[int(element)]+=1
for element in arr:
    print(element)