
def main():
    print(F"\n{"="*10} welcome to openlabs calculator {"="*10} \n")
    output = opeartion_checker()
    print(output)


def opeartion_checker():
    checker = input("\nwhat operation do you want to do? \n[1: addition] \n[2: substraction]\n[3: multiplication]\n[4: Division] \n press 'no' to exit" ) 

    match checker:
        case "no" | "n":
            return "quitting the Program"
        case _:
            try:
               num1 = float(input( " enter number: "))
               num2 = float(input( "enter second number: "))
            except ValueError as e:
                return F"error: {e}"

            match checker:
                case"1":
                    return addition(num1,num2)
                case"2":
                    return substraction(num1,num2)
                case "3":
                    return multiplication(num1,num2)
                case "4":
                    return division(num1,num2)
                case _:
                    return "invalid input.. pleaese try again"

def addition(num1,num2):
    total = num1 + num2
    return int(total)
    

def substraction(num1,num2):
    total = num1 - num2
    return int(total)
    

def multiplication(num1,num2):
    total = num1 * num2
    return int(total)


def division(num1,num2):
    if num2 != 0:
        total = num1 / num2
        return total
    else:
        return "error can't divide by zero"
    

if __name__ == "__main__":
    main()    