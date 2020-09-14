# 2월, 28일로 이루어진(윤년에는 29일)
#  4월, 6월 , 9월, 11월-> 30일
# 을 제외한 모든 달은 31일
dayofyear=[31,28,31,30,31,30,31,31,30,31,30,31]
while True:
    d,m,y=map(int,input().strip().split())
    if d==0 and m==0 and y==0:break
    print(sum(dayofyear[0:m-1])+d+(1 if ((y%4==0 and y%100!=0) or y%400==0) and m>=3 else 0))