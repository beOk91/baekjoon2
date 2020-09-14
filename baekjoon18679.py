n=int(input())
arr={}
for _ in range(n):
    cmd=input().strip().split("=")
    arr[cmd[0].strip()]=cmd[1].strip()
n2=int(input())
for _ in range(n2):
    n3=int(input())
    cmd=input().strip().split()
    print(" ".join([str(arr[element]) for element in cmd]))