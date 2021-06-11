print("\n")

class arith:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        result = self.num1 + self.num2
        return result

    def subtract(self):
        result = self.num1 - self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result

    def divide(self):
        result = self.num1 / self.num2
        return result

c = arith(24,12)

print("Addition is: ", c.add())
print("Substraction is: ", c.subtract())
print("Multiplication is: ", c.multiply())
print("Division is: ", c.divide())

print("\n")
