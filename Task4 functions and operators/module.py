from module import palindrome

def func1():
    print("No Argument No Return Statement Function")

func1()


def func2(num):
    print("With Argument No Return Statement Function")
    print("Argument: ", num)

func2(23)


def func3():
    return "No Argument With Return Statement Function"

var = func3()
print(var)


def func4(num):
    return "Argument With Return Statement Function", num

var2, var3 = func4(32)
print(var2, var3)


def func5(a=5, b=7):
    """ Function with Default Values """
    print("Result is: ",a+b)

func5()
func5(56, 14)


def func6(*num):
    sum = 0

    for n in num:
        sum = sum + n
    print("Sum: ", sum)

func6(10, 20)
func6(10, 20, 30)


def func7(**value):
    for i, j in value.items():
        print(f"{i} : {j}")

func7(Name = "Ashifa", Lastname = "Bhayala")


# Imported Function:
palindrome(12344321)
