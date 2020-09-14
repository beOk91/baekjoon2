import sys
num=int(sys.stdin.readline().strip())
for _ in range(num):
    text=sys.stdin.readline().strip()
    print(text+(" is GOOD" if text.lower().count("g")>text.lower().count("b") else " is A BADDY" if  text.lower().count("g")<text.lower().count("b") else " is NEUTRAL"))