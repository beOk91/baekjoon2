def solution(numbers, hand):
    answer = ''
    left_thumb=(3,0);right_thumb=(3,2)
    for element in numbers:
        if element in [1,4,7]:
            answer+="L";left_thumb=(0,0) if element==1 else (1,0) if element==4 else (2,0)
        elif element in [3,6,9]:
            answer+="R";right_thumb=(0,2) if element==3 else (1,2) if element==6 else (2,2)
        else:
            if element==2:
                if ((left_thumb[0]**2) + ((left_thumb[1]-1)**2))**0.5 < ((right_thumb[0]**2) + ((right_thumb[1]-1)**2 ))**0.5:
                   answer+="L";left_thumb=(0,1)
                elif ((left_thumb[0]**2) + ((left_thumb[1]-1)**2))**0.5 > ((right_thumb[0]**2) + ((right_thumb[1]-1)**2 ))**0.5:
                    answer+="R";right_thumb=(0,1)
                else: 
                    if hand=="right":answer+="R";right_thumb=(0,1)
                    else:answer+="L";left_thumb=(0,1)
            elif element==5:
                if (((left_thumb[0]-1)**2) + ((left_thumb[1]-1)**2))**0.5 < (((right_thumb[0]-1)**2) + ((right_thumb[1]-1)**2 ))**0.5:
                   answer+="L";left_thumb=(1,1)
                elif (((left_thumb[0]-1)**2) + ((left_thumb[1]-1)**2))**0.5 > (((right_thumb[0]-1)**2) + ((right_thumb[1]-1)**2 ))**0.5:
                    answer+="R";right_thumb=(1,1)
                else: 
                    if hand=="right":answer+="R";right_thumb=(1,1)
                    else:answer+="L";left_thumb=(1,1)
            elif element==8:
                if (((left_thumb[0]-2)**2) + ((left_thumb[1]-1)**2))**0.5 < (((right_thumb[0]-2)**2) + ((right_thumb[1]-1)**2 ))**0.5:
                   answer+="L";left_thumb=(2,1)
                elif (((left_thumb[0]-2)**2) + ((left_thumb[1]-1)**2))**0.5 > (((right_thumb[0]-2)**2) + ((right_thumb[1]-1)**2 ))**0.5:
                    answer+="R";right_thumb=(2,1)
                else: 
                    if hand=="right":answer+="R";right_thumb=(2,1)
                    else:answer+="L";left_thumb=(2,1)
            elif element==0:
                if (((left_thumb[0]-3)**2) + ((left_thumb[1]-1)**2))**0.5 < (((right_thumb[0]-3)**2) + ((right_thumb[1]-1)**2 ))**0.5:
                   answer+="L";left_thumb=(3,1)
                elif (((left_thumb[0]-3)**2) + ((left_thumb[1]-1)**2))**0.5 > (((right_thumb[0]-3)**2) + ((right_thumb[1]-1)**2 ))**0.5:
                    answer+="R";right_thumb=(3,1)
                else: 
                    if hand=="right":answer+="R";right_thumb=(3,1)
                    else:answer+="L";left_thumb=(3,1)
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"))

"""
            if hand=="right":
                if right_thumb[0]-1>=0 and arr[right_thumb[0]-1][right_thumb[1]]==element:
                    right_thumb=(right_thumb[0]-1,right_thumb[1])
                    answer+="R"
                elif right_thumb[0]+1<=3 and arr[right_thumb[0]+1][right_thumb[1]]==element:
                    right_thumb=(right_thumb[0]+1,right_thumb[1])
                    answer+="R"
                elif right_thumb[1]+1<3 and arr[right_thumb[0]][right_thumb[1]+1]==element:
                    right_thumb=(right_thumb[0],right_thumb[1]+1)
                    answer+="R"
                elif right_thumb[1]-1<3 and arr[right_thumb[0]][right_thumb[1]-1]==element:
                    right_thumb=(right_thumb[0],right_thumb[1]-1)
                    answer+="R"
                elif left_thumb[0]-1>=0 and arr[left_thumb[0]-1][left_thumb[1]]==element:
                    left_thumb=(left_thumb[0]-1,left_thumb[1])
                    answer+="L"
                elif left_thumb[0]+1<=3 and arr[left_thumb[0]+1][left_thumb[1]]==element:
                    left_thumb=(left_thumb[0]+1,left_thumb[1])
                    answer+="L"
                elif left_thumb[1]+1<3 and arr[left_thumb[0]][left_thumb[1]+1]==element:
                    left_thumb=(left_thumb[0],left_thumb[1]+1)
                    answer+="L"
                elif left_thumb[1]-1>=0 and arr[left_thumb[0]][left_thumb[1]-1]==element:
                    left_thumb=(left_thumb[0],left_thumb[1]-1)
                    answer+="L"
                    
            elif hand=="left":
                if left_thumb[0]-1>=0 and arr[left_thumb[0]-1][left_thumb[1]]==element:
                    left_thumb=(left_thumb[0]-1,left_thumb[1])
                    answer+="L"
                elif left_thumb[0]+1<=3 and arr[left_thumb[0]+1][left_thumb[1]]==element:
                    left_thumb=(left_thumb[0]+1,left_thumb[1])
                    answer+="L"
                elif left_thumb[1]+1<3 and arr[left_thumb[0]][left_thumb[1]+1]==element:
                    left_thumb=(left_thumb[0],left_thumb[1]+1)
                    answer+="L"
                elif left_thumb[1]-1>=0 and arr[left_thumb[0]][left_thumb[1]-1]==element:
                    left_thumb=(left_thumb[0],left_thumb[1]-1)
                    answer+="L"
                elif right_thumb[0]-1>=0 and arr[right_thumb[0]-1][right_thumb[1]]==element:
                    right_thumb=(right_thumb[0]-1,right_thumb[1])
                    answer+="R"
                elif right_thumb[0]+1<=3 and arr[right_thumb[0]+1][right_thumb[1]]==element:
                    right_thumb=(right_thumb[0]+1,right_thumb[1])
                    answer+="R"
                elif right_thumb[1]+1<3 and arr[right_thumb[0]][right_thumb[1]+1]==element:
                    right_thumb=(right_thumb[0],right_thumb[1]+1)
                    answer+="R"
                elif right_thumb[1]-1<3 and arr[right_thumb[0]][right_thumb[1]-1]==element:
                    right_thumb=(right_thumb[0],right_thumb[1]-1)
                    answer+="R"
"""