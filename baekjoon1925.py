a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
c=list(map(int,input().strip().split()))
arr=[]
"""
a_b=int((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
b_c=int((b[0]-c[0])**2+(b[1]-c[1])**2)**0.5
c_a=int((c[0]-a[0])**2+(c[1]-a[1])**2)**0.5
"""
arr.append((a[0]-b[0])**2+(a[1]-b[1])**2)
arr.append((b[0]-c[0])**2+(b[1]-c[1])**2)
arr.append((c[0]-a[0])**2+(c[1]-a[1])**2)
arr.sort()
if (a[0]==b[0] and b[0]==c[0]) or (a[1]==b[1] and b[1]==c[1]) or (int((a[1]-b[1])/(a[0]-b[0]))==int((b[1]-c[1])/(b[0]-c[0]))):print("X")
elif arr[0]==arr[1] and arr[1]==arr[2]:print("JungTriangle")
elif arr[0]==arr[1] or arr[1]==arr[2] or arr[2]==arr[0]:
    print("Dunkak2Triangle" if arr[2]>arr[0]+arr[1] else "Jikkak2Triangle" if arr[2]==(arr[0]+arr[1]) else "Yeahkak2Triangle")
else:
    print("DunkakTriangle" if arr[2]>arr[0]+arr[1] else "JikkakTriangle" if arr[2]==(arr[0]+arr[1]) else "YeahkakTriangle")
