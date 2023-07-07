try :
    a = int(input("a= "))
    b = int(input("b= "))
    print(a / b)
except ZeroDivisionError:
    print("don't divide by zerro")
    print(ZeroDivisionError.__doc__)
except ValueError:
    print("Enter a valid value")
    print(ValueError.__doc__)
finally:
    print("Learn to use your brain my friend")    