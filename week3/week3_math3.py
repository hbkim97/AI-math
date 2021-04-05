class Man:
    def __init__(self, name):
        self.name = name

    def tellYourName(self):
        print("my name is" + self.name)

class BusinessMan(Man):
    def __init__(self, name, company, position):
        self.company = company
        self.position = position
        self.name = name #1
        #Man.__init__(self.name) #2.1
        #super().__init__(self.name) #2.2

    def tellYourInfo(self):
        print('my company is '+ self.company)
        print('my position is ' + self.position)
        self.tellYourName()

man1 = Man('heeseok')
man1.tellYourName()

bman1 = BusinessMan('heeseok', 'hansung', 'student')
bman1.tellYourInfo()
