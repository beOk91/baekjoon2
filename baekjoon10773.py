import sys
class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]

stack=[]
num=int(sys.stdin.readline().strip())
for i in range(num):
    cmd=int(sys.stdin.readline().strip())
    stack.pop() if cmd==0 else stack.append(cmd)
sum=0
for element in stack:
    sum+=element
print(sum)