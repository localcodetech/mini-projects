class Calculator:
    def __init__(self):
        self.memory = 0

    
    # create method for the body 

    def addition(self, num1, num2=None):
        if num2 is None:
            self.memory += num1
            return self.memory
        else:
            self.memory = num1 + num2
            return self.memory
    

    def substraction(self, num1, num2):
        if num2 is None:
            self.memory -= num1
            return self.memory
        else:
            self.memory = num1 - num2
            return self.memory
        

    def multiplication(self, num1, num2):
        if num2 is None:
            self.memory *= num1
            return self.memory
        else:
            self.memory = num1 - num2

    def division(self, num1, num2):
        if num2 is None:
            self.memory /= num1
            return self.memory
        elif num2 == 0:
            return "error cant divide by zero"
        elif num1  == 0:
            return "division error"
        else:
            self.memory = num1 / num2
            return self.memory
            

    def user_input(self,prompt="Enter number: "):
        
        num1 = float (input(prompt))
        num2 = input(prompt)
        num2 = float(num2) if num2 else None
        return num1,num2
        
    


        
    def operations(self):
        
        while True:
            message = input (F"\n{"="*5}SELECT OPERATION{"="*5}\n[1: ADDITION]\n[2: SUBSTRACTION]\n[3: MULTIPLICATION]\n[4: DIVISION]\n(press 'n' or 'q' to exit the app)\n\n").lower().strip()
            if message not in ["1","2","3","4","n","q"]:
                continue
            else:

                match message:
                    case "n" | "q":
                        return "program exited ....."
                    case _:
                        num1,num2 = self.user_input()
                        match message:
                            case "1":
                                return self.addition(num1,num2)
                            case "2":
                                return self.substraction(num1,num2)
                            case "3":
                                return self.multiplication(num1,num2)
                            case "4":
                                return self.division(num1,num2)
                            
            
        
        
        


out = Calculator()
result = out.operations()
print(result)





        
        
        