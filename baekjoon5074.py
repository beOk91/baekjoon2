while True:
    start_time,end_time=input().strip().split()
    if start_time=="00:00" and end_time=="00:00":break
    start_time=list(map(int,start_time.split(":")))
    end_time=list(map(int,end_time.split(":")))
    total=start_time[0]*60+end_time[0]*60+start_time[1]+end_time[1]
    print("%02d:%02d" %(total%(60*24)//60,total%60)+(" +{} ".format(total//1440) if total>=1440 else ""))
    """
     if total//60<24 else total%(60*24)//60
    """