while True:
    a=input()
    if a=="0":break
    while True:
        result=sum(int(i) for i in a)
        a=str(result)
        if int(a)<10:break
    print(result)