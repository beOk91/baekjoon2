song=["sukhwan","baby", "sukhwan", "tururu", "turu","very", "cute", "tururu", "turu","in", "bed", "tururu", "turu","baby"]
n=int(input())
voca=song[n%14]+"ru"*(n//14) if n%14 in [3,4,7,8,11,12] else song[n%14]
if len(voca)>=12:
    print(voca[:2]+"+ru*"+str((len(voca)-2)//2))
else:
    print(voca)