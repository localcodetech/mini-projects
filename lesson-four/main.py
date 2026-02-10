
def main():
    output = operation_checker()
    print(output)



def number_input(prompt="enter number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            continue
        except TypeError:
            continue
    

def operation_checker():

    while True:
        message: str = input (F"\n{"="*5}Select OPERATION{"="*5}\n[1: ADDITION] \n[2: SUBSTRACTION] \n[3: MULTIPLICATION] \n[4: DIVISION] \nPress'n' or 'no' to quit \n\n").lower().strip()
        if message not in ["1","2", "3", "4", "n", "no"]:
            continue
        else:
            message
            # break
        match message:
            case "no" | "n":
                return "program exited"
            case _:
                num1 = number_input("enter first number: \n")
                num2 = number_input("enter second number: \n")
        match message:
            case "1":
                return addition(num1,num2)
            case "2":
                return subtraction(num1,num2)
            case "3":
                return multiplication(num1,num2)
            case "4":
                return division(num1,num2)
            case _:
                return "invalid choice"

def  addition(num1,num2):
    total = num1 + num2
    return F"ans: {int(total)}"

def subtraction(num1,num2):
    total = num1 + num2
    return F"ans: {int(total)}"

def multiplication(num1,num2):
    total = num1 * num2
    return F"ans: {int(total)}"

def division(num1,num2):
    if num2 != 0:
        total = num1 / num2
        return F"ans: {total}"
    else:
        return "cant divide a number 0"

if __name__ == "__main__":
    main()