class cal3:
    principal = 0
    rate = 0
    time = 0
    si = 0
    def __init__(self,principal,rate,time):
        self.principal = principal
        self.rate = rate
        self.time = time
    def callinterest(self):
        self.si = (self.principal * self.rate * self.time)/100
    def display(self):
        self.callinterest()
        print(f"Simple Interest is: Rs.{self.si}")

principal = int(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time (In Years): "))

c = cal3(principal,rate,time)
c.display()
