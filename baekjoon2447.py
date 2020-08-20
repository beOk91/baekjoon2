n=int(input())

arr=["***","* *","***"]
for k in range(n//3//3):
    for i in range(3):
        for j in range(3):
            if i%2!=0 and j==1:
                for l in range(n//3//3):
                    print(" ",end="")
            else:
                for l in range(n//3//3):
                    print("*",end="")
            print()

"""
for i in range(n//3//3):
    print(arr[i]*3)
for i in range(n//3//3):
    for j in range(n//3//3):
        if i%2!=0:
            print(arr[i],end="")
        else:
            print(" ",end="")
    print()
for i in range(n//3//3):
    print(arr[i]*3)


for element in arr:
    print(element)
"""