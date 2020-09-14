n=int(input())
fox=0
for _ in range(n):
    finger=list(map(int,input().strip().split()))
    finger[0],finger[1]=finger[1] if finger[0]>finger[1] else finger[0], finger[0] if finger[0]>finger[1] else finger[1]
    if finger in [[1,3],[1,4],[3,4]]:
        fox+=1
    else:
        fox=-1
        break
print("Wa-pa-pa-pa-pa-pa-pow!" if fox==3 else "Woof-meow-tweet-squeek")