t=int(input())
for _ in range(t):
    num=int(input())
    num2=str(int(str(num)[::-1])+num)
    print("YES" if num2[:len(num2)//2]==(num2[::-1])[:len(num2)//2] else "NO")
