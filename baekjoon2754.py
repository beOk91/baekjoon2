score=input()
if score[0]=="A":
    print(4.3 if score[1]=="+" else 4.0 if score[1]=="0" else 3.7)
elif score[0]=="B":
    print(3.3 if score[1]=="+" else 3.0 if score[1]=="0" else 2.7)
elif score[0]=="C":
    print(2.3 if score[1]=="+" else 2.0 if score[1]=="0" else 1.7)
elif score[0]=="D":
    print(1.3 if score[1]=="+" else 1.0 if score[1]=="0" else 0.7)
elif score[0]=="F":
    print(0.0)
