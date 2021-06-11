class cal2:
    def setdata(self, radius):
        self.radius = radius
        print("Radius Set Succesfully! ")

    def area(self):
        radius = self.radius
        self.result = 3.14 * (radius**2)

    def display(self):
        self.area()
        print(f"Area of A Circle with {self.radius} is: {self.result}")

c = cal2()
radius = float(input("Enter Radius:"))
c.setdata(radius)
c.display()
