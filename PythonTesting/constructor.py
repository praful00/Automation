#self keyword is mandatory to call the variable names into method
#instance and class variable have whole diffrent purpose
#constructor name should be _init_
#new keyword not required when you create object


class calculator:

    num=100      #class variable


    def __init__(self,a,b):                  #constructer
        self.firstnum = a                    #instance variable
        self.secondnum = b
        print("enter data into constructor")

    def getdata(self):
        print("enter data")

    def summation(self):
        return self.firstnum + self.secondnum + calculator.num

obj = calculator(5,5)
obj.getdata()
print(obj.num)
print(obj.summation())
