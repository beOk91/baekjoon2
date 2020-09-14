import sys
while True:
    a=int(sys.stdin.readline().strip())
    if a==0:break
    a_list=sys.stdin.readline().strip().split()
    print("Mary won {} times and John won {} times".format(a_list.count("0"),a_list.count("1")))