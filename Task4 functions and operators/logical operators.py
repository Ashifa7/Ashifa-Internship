# Logical Operators:
num1 = 28
num2 = 32
num3 = 30
print("Logical Operators:")

# AND operator
if num1>num2 and num1>num3:
    print("num1 is the largest")
if num2>num1 and num2>num3:
    print("num2 is the largest")
if(num3>num1 and num3>num2):
    print("num3 is the largest")

# Or Operator    
ch=input("Enter Char:")
if(ch=='A'or ch=='a'or ch=='E'or ch=='e'or ch=='I'or ch=='i' or ch=='O'or ch=='o'or ch=='U'or ch=='u'):
    print(ch," is Vowel")
else:
    print(ch," is consonant")
