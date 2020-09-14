import sys
while True:
    a=sys.stdin.readline().strip()
    if a=="0":
        break
    result=0
    for i in range(len(a)):
        b=1
        for j in range(1,i+2):
            b*=j
        result+=int(a[::-1][i])*b
    print(result)