now1=list(map(int,input().strip().split(":")))
bomb=list(map(int,input().strip().split(":")))
difference=(((24+bomb[0])*60*60+bomb[1]*60+bomb[2])-(now1[0]*60*60+now1[1]*60+now1[2]))
if difference==24*60*60:
    print("24:00:00")
else:
    print("%.2d:%.2d:%.2d" %(difference//3600%24,difference%3600//60,difference%3600%60))
