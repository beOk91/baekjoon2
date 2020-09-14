while True:
    cnt=int(input())
    if cnt==0:break
    page=[False]*(cnt+1)
    page_list=input().strip().split(",")
    for i in range(len(page_list)):
        page_list[i]=list(map(int,page_list[i].split("-")))
        if len(page_list[i])>=2 and page_list[i][0]<=page_list[i][1]:
            for j in range(page_list[i][0],page_list[i][1]+1 if page_list[i][1]<=cnt else cnt+1):
                page[j]=True
        elif len(page_list[i])>=2 and page_list[i][0]>page_list[i][1]:
            for j in range(page_list[i][1],page_list[i][0]+1 if page_list[i][0]<=cnt else cnt+1): 
                if page[j]:continue
                page[j]=False
        elif len(page_list[i])==1 and page_list[i][0]<=cnt:
            page[page_list[i][0]]=True
    print(sum(1 for i in range(cnt+1) if page[i]==True))