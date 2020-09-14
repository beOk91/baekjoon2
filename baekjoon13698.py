import sys
yabai=[1,0,0,2]
text=list(sys.stdin.readline().strip())
for e in text:
    if e=="A":
        yabai[0],yabai[1]=yabai[1],yabai[0]
    elif e=="B":
        yabai[0],yabai[2]=yabai[2],yabai[0]
    elif e=="C":
        yabai[0],yabai[3]=yabai[3],yabai[0]
    elif e=="D":
        yabai[1],yabai[2]=yabai[2],yabai[1]
    elif e=="E":
        yabai[1],yabai[3]=yabai[3],yabai[1]
    elif e=="F":
        yabai[2],yabai[3]=yabai[3],yabai[2]
print(yabai.index(1)+1)
print(yabai.index(2)+1)