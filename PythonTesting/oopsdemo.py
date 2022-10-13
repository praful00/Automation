

class pro:
    num=100 #class variable

    def getdata(self):
        print("executing method")


obj= pro()
obj.getdata()
print(obj.num)



#Constructer

class cls:
    num=100

    def getdata(self):
        print("execute")

obj1=cls()
obj1.getdata()
print(obj1.num)