def f(num):
    my_text=str(num)
    constructor_num=num
    for element in my_text:
        constructor_num+=int(element)
    return constructor_num
num_list=[i for i in range(1,10001)]
for i in range(1,10001):
    if f(i) in num_list:
        num_list.remove(f(i))
for element in num_list:
    print(element)
