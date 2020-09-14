import decimal
n=int(input())
myscore=[0]*2
for _ in range(n):
    subject_info=input().strip().split()
    myscore[0]+=int(subject_info[1])
    myscore[1]+=int(subject_info[1])*(4.3 if subject_info[2]=="A+" else 4.0 if subject_info[2]=="A0" else 3.7 if subject_info[2]=="A-" 
                                else 3.3 if subject_info[2]=="B+" else 3.0 if subject_info[2]=="B0" else 2.7 if subject_info[2]=="B-" 
                                else 2.3 if subject_info[2]=="C+" else 2.0 if subject_info[2]=="C0" else 1.7 if subject_info[2]=="C-" 
                                else 1.3 if subject_info[2]=="D+" else 1.0 if subject_info[2]=="D0" else 0.7 if subject_info[2]=="D-" 
                                else 0.0)
print("%.2f" %(round(decimal.Decimal(myscore[1])/decimal.Decimal(myscore[0]),2)))