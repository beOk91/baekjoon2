n=int(input())
for _ in range(n):
    name,score=input().strip().split()
    print(name,"A+" if int(score)>=97 else "A" if int(score)>=90 else "B+" if int(score)>=87 else "B" if int(score)>=80 else "C+" if int(score)>=77 else "C" if int(score)>=70 else "D+" if int(score)>=67 else "D" if int(score)>=60 else "F")