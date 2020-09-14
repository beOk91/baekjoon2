while True:
    name,age,weight=input().strip().split()
    if name=="#" and age=="0" and weight=="0":break
    print(name,"Junior" if int(age)<=17 and int(weight)<80 else "Senior")