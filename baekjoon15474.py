"""
문구점에서 연필이 일정 개수 씩 세트로 판매되고있다. 
세트 X는 A 책에서 B 엔, 세트 Y는 C 책에서 D 엔이다.

JOI 군은 세트 X 또는 세트 Y 중 하나를 선택하고 선택한 
세트를 몇 가지 구입한다. 두 세트를 구입할 수 없다. 
N 개 이상의 연필을 얻기 위해 필요한 금액의 최소값을 구하라.
10개
"""
n,a,b,c,d=map(int,input().strip().split())
print(min(n//a*b if n%a==0 else (n//a+1)*b,n//c*d if n%c==0 else (n//c+1)*d))