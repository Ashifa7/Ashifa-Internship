class cal1:
    def setdata(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        print("Data Set Successfully! ")
    def display(self):
        sum = self.num1 + self.num2 + self.num3
        print(f'{self.num1} + {self.num2} + {self.num3} = {sum}')

c = cal1()
c.setdata(34,12,14)
c.display()
