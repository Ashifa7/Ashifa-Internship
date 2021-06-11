class cal6:

    def setdata(self, length):
        self.length = length

    def area(self):
        self.result = self.length * self.length

        return self.result

    def display(self):
        result = self.area()
        print(f"Area of Square is: {result}")

length = int(input("Enter Length: "))

c = cal6()
c.setdata(length=length)
c.display()
