# 1.This Prints Hello World
print("Hello World")


# 2. Declaration and use of variable
a=12
b=12.5
name='ASHIFA'

print(a)
print('b is', b)
print('Name is' ,name)


# 3.Changing the value of variable
name='ASHIFA'
print('Name (Before Changing) is : ' ,name)

# Assigning new value to same variable
name='ASHIFA BHAYALA'
print('Name is : ' ,name)


# 4. Assigning multiple values to multiple variables
a, b, c = 12, 12.5, 'XYZ'
print(a)
print('value of b is : ', b)
print('Random user name is : ' , c)


# 5. Assigning same value to multiple variables
a = b = c = 12
print('Value of a is: ', a)
print('Value of b is :', b)
print('Value of c is : ', c)


# 6. Example of number datatype
a = 12
print(a, 'is of type', type(a))

b = 15.5
print(b, 'is of type', type(b))
print(b, 'is a complex number?', isinstance(15.5, int))

c = 1+2j
print(c, 'is a complex number?', isinstance(1+2j, complex))


# 7.Example of string datatype
name = 'ASHIFA'

# prints full name
print('Name is:', name)

# prints character starting from 2nd to 4th
print(name[1:4])

# prints whole string starting from 2nd character
print(name[1:])

# prints 1st character of string
print(name[0])

# prints string twice
print(name * 2)

# prints concatenated string
print('Hey '+ name)


# 8.Examples of List datatype
list1 = [10, 20, 30, 'xyz', 40, 50, 'ASHIFA', 60, 70]
print(list1)
print(list1[2])
print(list1[0:3])
print(list1[3: ])
print(list1[ :5])


# 9.Tuple datatype
tuple1 = (10, 20, 30, 'xyz', 40, 50, 'ABC', 60, 70)
print(tuple1)
print(tuple1[2])
print(tuple1[1:5])
print(tuple1[5: ])
print(tuple1[ :4])


# 10.Example for user input list
lst= []
n= int(input('Enter number of elements: '))

for i in range(0, n):
    ele = input('Enter value: ')
    lst.append(ele)

print(lst)
