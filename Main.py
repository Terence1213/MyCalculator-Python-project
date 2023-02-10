add = lambda num1, num2: num1 + num2

mult = lambda num1, num2: num1 * num2

div = lambda num1, num2: num1 / num2

sub = lambda num1, num2: num1 - num2

def calculate(num1):
    result = 0
    num2 = float(input("Please enter the next number: "))
    inputValid = True
    while inputValid:
        inputValid = True
        operation = int(input("\nEnter the mathematical operation of your choice:"
                              "\n1. = Addition"
                              "\n2. = Subtraction"
                              "\n3. = Multiplication"
                              "\n4. = Division"
                              "\nEnter your choice (1 - 4): "))
        try:
            match operation:
                case 1:
                    result += add(num1, num2)
                case 2:
                    result += sub(num1, num2)
                case 3:
                    result += mult(num1, num2)
                case 4:
                    result += div(num1, num2)
                case _:
                    inputValid = False
        except:
            print("\nCannot divide by 0!")

        print("--------------------------------------")
        print("The answer is: " + str(result))
        print("--------------------------------------")

        return result

def startCalculation():

    result = 0
    num1 = float(input("\n-------------------------------------\nPlease enter the first number: "))
    result = calculate(num1)

    while True:
        menuChoice = int(input("\nEnter 1. = calculate another number (continued on the obtained result)"
                               "\nEnter 2. = Go back to main menu"
                               "\nEnter your choice (1 - 2): "))

        if menuChoice == 1:
            result = calculate(result)
        elif menuChoice == 2:
            break

def menu():
    while True:
        print("\n--------------------------------------------------------------------------")
        choice = int(input("1. = Start calculation\n2. = Quit\nPlease enter your choice (1 - 2): "))

        match choice:
            case 1:
                startCalculation()
            case 2:
                break
            case _:
                pass
menu()

