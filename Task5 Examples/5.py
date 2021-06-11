class Employee:
    name = "ASHIFA"
    desgination = "Developer"

    def display(self):
        print(f"Name: {self.name} \nDesignation: {self.desgination}")

class SubClass(Employee):
    salary = 10000

    def display(self):
        print(f"Name: {self.name} \nDesignation: {self.desgination} \nSalary: {self.salary}")

c1 = Employee()
print("The Following is from Employee(Parent):")
c1.display()

print("\n")
print("The Following is from SubClass(Child) inherited from Employee(Parent):")
c2 = SubClass()
c2.display()
