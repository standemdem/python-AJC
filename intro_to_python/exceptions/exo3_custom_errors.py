from custom_errors import CustomError, AnotherError

def divide(x, y):
    if y == 0:
        raise CustomError("you divided by 0")
    elif y == 1:
        raise AnotherError("you divided by 1")
    else:
        return x / y
    
try:
    x=int(input("Enter x :"))
    y = int(input("Enter y "))
except CustomError as e:
    e.printError()
except AnotherError:
    print(str(AnotherError))