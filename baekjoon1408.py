import sys
start_time=list(map(int,sys.stdin.readline().strip().split(":")))
end_time=list(map(int,sys.stdin.readline().strip().split(":")))
time=end_time[0]*60*60-start_time[0]*60*60+end_time[1]*60-start_time[1]*60+end_time[2]-start_time[2]
print("%02d:%02d:%02d" %(time//3600%24,time%3600//60,time%3600%60))