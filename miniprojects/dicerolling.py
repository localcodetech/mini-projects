'''
Write a program that simulates rolling a pair of dice. Each time the program runs, it
should randomly generate two numbers between 1 and 6 (inclusive), representing
the result of each die. The program should then display the results and ask if the
user would like to roll again.
'''


import random as rd

def main():
    
    message = F"\n{"="*10}Dice Rolling Game {"="*10}\n"
    print(message)
    dice_counter = 0
    dice_rolling(dice_counter)
    
def user_input(prompt= "enter number: "):
    
    while True:
        try:
            dice_1 = int(input(prompt))
            dice_2 = int(input(prompt))
            return dice_1, dice_2
        except ValueError:
            print("numbers only")
            continue
        except TypeError: 
            print("numbers only")
            continue

def dice_rolling(dice_counter):
    while True:   
        checker = input("Roll the dice?.. [y/n]").lower().strip()
        match checker:
            case "n":
                print("exiting program")
                if dice_counter > 0:
                    print(f"you have played the program {dice_counter} times")
                    break
                else:
                    break
            case "y":
               dice_1, dice_2 = user_input()
               dice_roller_1 = rd.randint(dice_1, dice_2)
               dice_roller_2 = rd.randint(dice_1,dice_2)
               
               print (F"({dice_roller_1},{dice_roller_2})")
               dice_counter +=1

if __name__ == "__main__":
    main()



    ### functions are meant to perform single but in this instance i want do everything in one place