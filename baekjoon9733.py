arr=[]
try:
    while True:
        arr2=input().strip().split(" ")
        arr.extend(arr2)
except:
    exit()
# 휴식(Re), 순찰(Pt), 방청소(Cc), 꽃가루 먹기(Ea), 새끼 돌보기(Tb), 벌집 짓기와 관리(Cm), 외부 활동(Ex)
    total_name=["Re","Pt","Cc", "Ea","Tb","Cm","Ex"]
    total=[0]*7
    for element in arr:
        if element=="Re":
            total[0]+=1
        elif element=="Pt":
            total[1]+=1
        elif element=="Cc":
            total[2]+=1
        elif element=="Ea":
            total[3]+=1
        elif element=="Tb":
            total[4]+=1
        elif element=="Cm":
            total[5]+=1
        elif element=="Ex":
            total[6]+=1
    for i in range(7):
        print(str(total_name[i])+" {}".format(total[i])+" %.2f" %(total[i]/len(arr)))
    print("Total "+str(len(arr))+" 1.00")