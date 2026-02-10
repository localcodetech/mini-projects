

def main():

    print (f"\n{"="*10}simple calculator{"="*10}\n")
    user_name = input ("what is your name: \n")
    print (F"\n{user_name.title()} you can do your calculation \n")

    output = user_input()
    print(output)

def user_input():
    operation_checker = input(" what operation do you wanna do?__ \n[1:addition]\n[2:substraction]\n[3:multiplication]\n[4:Division]\npress 'no' to quit \n").lower().strip()
    match operation_checker:
        case "no"|"n":
            return "ok... Good bye"
        case _:
            while True:
                try:
                    num1 = float( input (" enter first number:  "))
                    num2 = float(input("enter second number:  "))

                except ValueError:
                    print("invalid user input")
                    continue
                    
                match operation_checker:
                    case "1":
                        return addition(num1,num2)
                    case "2":
                        return substraction(num1,num2)
                    case "3":
                        return multiplication(num1,num2)
                    case "4":
                        return division(num1,num2)  
                    case _:
                        return "invalid user input"     

def addition(num1,num2):
    total = num1 + num2
    return int(total)

def substraction(num1,num2):
    total = num1 - num2
    return int(total)

def multiplication(num1,num2):
    total = int(num1 * num2)
    return total

def division(num1,num2):
    if num2 != 0:
        total = num1 /num2
        return total
    else:
        return "error can't divide my zero"

if __name__ == "__main__":
    main()
