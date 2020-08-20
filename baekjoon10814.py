class User:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

num=int(input())
arr=[]
for i in range(num):
    info1,info2=input().strip().split()
    arr.append(User(int(info1),info2))
arr.sort(key=lambda x:x.age)
for i in range(num):
    print(arr[i].age,arr[i].name)