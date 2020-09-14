import sys
a,b=sys.stdin.readline().strip().split()
#print(sum([(int(i)*int(j)) for j in b for i in a]))
print(sum(int(element) for element in a)*sum(int(element) for element in b))