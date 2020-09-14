import re
pattern=re.compile("(\d+)+([+-])(\d+)([+-])(\d+)")
text=input().strip()
arr=(pattern.findall(text))[0]
val1=(int(arr[0])+int(arr[2]) if arr[1]=="+" else int(arr[0])-int(arr[2]))+int(arr[4]) if arr[3]=="+" else (int(arr[0])+int(arr[2]) if arr[1]=="+" else int(arr[0])-int(arr[2]))-int(arr[4])
val2=int(arr[0]) + (int(arr[2])+int(arr[4]) if arr[3]=="+" else int(arr[2])-int(arr[4])) if arr[1]=="+"  else int(arr[0])- (int(arr[2])+int(arr[4]) if arr[3]=="+" else int(arr[2])-int(arr[4]))
print(min(val1,val2))