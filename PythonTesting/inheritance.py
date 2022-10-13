from constructor import calculator

class child(calculator):

    num2=200

    def __init__(self):
        calculator.__init__(self,10,10)

    def getalldata(self):

        return self.num+self.num2+self.summation()

object= child()
print(object.getalldata())