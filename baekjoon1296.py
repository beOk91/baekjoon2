ominsik=input()
l=ominsik.count("L");o=ominsik.count("O");v=ominsik.count("V");e=ominsik.count("E") 
n=int(input())
max_val,max_name,name=-1,"",[]
for _ in range(n):
    name.append(input().strip())
name.sort()
for element in name:
    arr=[0]*4
    arr[0]+=element.count("L");arr[1]+=element.count("O");arr[2]+=element.count("V");arr[3]+=element.count("E")
    arr[0]+=l;arr[1]+=o;arr[2]+=v;arr[3]+=e
    if max_val<((arr[0]+arr[1])*(arr[0]+arr[2])*(arr[0]+arr[3])*(arr[1]+arr[2])*(arr[1]+arr[3])*(arr[2]+arr[3]))%100:
        max_val=((arr[0]+arr[1])*(arr[0]+arr[2])*(arr[0]+arr[3])*(arr[1]+arr[2])*(arr[1]+arr[3])*(arr[2]+arr[3]))%100
        max_name=element
print(max_name)