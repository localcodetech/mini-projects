
import quiz 

count = 1
for var in quiz.python_questions:
    print(
        F'''{count}:{var[0]} \n{"="*3}options{"="*3}\nA:{var[1][0]}\nB:{var[1][1]}\nC:{var[1][2]}\nD:{var[1][3]}
'''
    )
    count += 1

    selection = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3
    }

    while True:
        user_answer = input ("\nenter correct answer [a],[b],[c].[d] \n").lower().strip()
        if user_answer not in ["a","b","c","d"]:
            continue
        else:
            user_answer
            break

    
    if selection[user_answer] == var[2]:
        print("correct")
    else:
        print("wrong")

            




