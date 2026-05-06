num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
option = int(input("selet option \n For Addition Enter 1 \n For Substraction Enter 2 \n For Multiplication Enter 3 \n For Divison Enter 4 \n Enter option: "))

def add():
    print("num1 + num2 = ", num1 + num2)

def sub():
    print("num1 - num2 = ", num1 - num2)

def mul():
    print("num1 * num2 = ", num1 * num2)

def div():
    print("num1 / num2 = ", num1 / num2)

def calc(opt):
    if opt == 1:
        add()
    elif opt == 2:
        sub()
    elif opt == 3:
        mul()
    elif opt == 4:
        div()
    else:
        print("Invalid")

calc(option)