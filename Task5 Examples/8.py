print("\n")

class Publisher:
    title = "Lord of the Rings"

    def display(self):
        print("Title: ", self.title)

class Book(Publisher):
    total_pages = 135

    def display(self):
        print("Title: ", self.title)
        print("Total Pages: ", self.total_pages)

class Tape(Publisher):
    time_play = "30min 45sec"

    def display(self):
        print("Title: ", self.title)
        print("Playing Time: ", self.time_play)
        
c1 = Publisher()
c2 = Book()
c3 = Tape()

print("The Following is from Publisher(Parent):")
c1.display()

print("\n")
print("The Following is from Book(Child) inherited from Publisher(Parent):")
c2.display()

print("\n")
print("The Following is from Tape(Child) inherited from Publisher(Parent):")
c3.display()

print("\n")
