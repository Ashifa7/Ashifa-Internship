class cal5:
    length = 0
    breadth = 0

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calArea(self):
        self.result = self.length * self.breadth
    
    def display(self):
        self.calArea()
        result = self.result
        print(f"The Area of Rectangle is: {result}")

c = cal5(20,45)
c.display()
