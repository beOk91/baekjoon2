import math
print("n","e")
print("- -----------")
for i in range(10):
    result=0
    for j in range(i+1):
        result+=1/math.factorial(j)
    print(str(i),str(int(result)) if i in [0,1] else "%.1f" %result if i==2 else "%.9f" %result)