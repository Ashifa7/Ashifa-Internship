#1) Average of 5 Numbers
sum = 0 
for i in range(5):
    n = int(input(f"Enter {i+1} Number: "))
    sum += n


average = sum/5
print("The Average is: ",average)

#2) check if number is even or odd
num = int(input("Enter The Number: "))

if num % 2 == 0:
    print(f"{num} is even! ")
else:
    print(f"{num} is odd! ")
 
#3) check if year is leap or not
print("\n")

year = int(input("Enter The Year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(f"{year} is a leap year")
       else:
           print(f"{year} is not a leap year")
   else:
       print(f"{year} is a leap year")
else:
   print(f"{year} is not a leap year")


print("\n")

#4) check if a number is zero, positive or negative
print("\n")

num = int(input("Enter The Number: "))
print("\n")
if num == 0:
    print("Number is Zero")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Positive")


print("\n")

#5) take two numbers and identify greatest
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 == num2:
    print("Both Number are Equal")
else:
    if num1<num2:
        print(f"{num2} is Greater! ")
    else:
        print(f"{num1} is Greater! ")

print("\n")

#6) find factorial
print("\n")

num = int(input("Enter Number: "))

def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)
        

print(f"Factorial of {num} is {fact(num)}")

print("\n")

#7) swap 2 numbers
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("\n")

print("Number before swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

# Using third Variable
temp = num1
num1 = num2
num2 = temp

print("Number after swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

#8) find smallest of 2 numbers
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 == num2:
    print("Both Number are Equal")
else:
    if num1<num2:
        print(f"{num1} is Smaller! ")
    else:
        print(f"{num2} is Smaller! ")

print("\n")

#9) check if number is <100, if yes check if its even or odd
print("\n")

num = int(input("Enter Number: "))

if num<100:
    if num % 2 !=0:
        print(f"Number ({num}) is Odd")
    else:
        print(f"Number ({num}) is not Odd")
else:
    print("Number Greater Than 100")


print("\n")

#10) print square of number if its <10
print("\n")

num = int(input("Enter Number: "))

if num<10:
    print(f"Square of {num} is {num**2}")
else:
    print("Number Greater Than 10")


print("\n")

#11) check number is 0, -, + using nested if-else
print("\n")

num = int(input("Enter The Number: "))

if num == 0:
    print("Number is Zero")

else:
    if num < 0:
        print("Number is Negative")
    else:
        print("Number is Positive")


print("\n")

#12) find greatest of 3 numbers using nested if-else
print("\n")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))


if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Largest")
    else:
        print(f"{num3} is Largest")
else:
    if num2 > num3:
        print(f"{num2} is Largest")
    else:
        print(f"{num3} is Largest")

print("\n")

#13) find smallest of 3 numbers using logical operators
print("\n")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if(num1 < num2 and num1<num3):
    print(f"{num1} is smallest")
elif(num2 < num1 and num2 < num3):
    print(f"{num2} is smallest")
else:
    print(f"{num3} is smallest")

print("\n")

#14) swap two numbers without third variable
print("\n")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))


print("Number before swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

num1, num2 = num2, num1

print("Number after swapping are: ")
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")

print("\n")

#15) print series
print("\n")

start = int(input("Enter 1st number: "))
end = int(input("Enter 2nd number: "))

for i in range(start, end-1, -3):
    print(i)


print("\n")
