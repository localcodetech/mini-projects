import quiz



''' a simple script to run a cmd quiz'''


def main():
    output = python_quiz()
    print(output)




def python_quiz():
    
    for question in quiz.python_questions:

        while True:

         return F"\n{question[0]}\nA: {question[1][0]}\nB: {question[1][1]}\nC: {question[1][2]}\nD: {question[1][3]} \n"





def html_css():
    pass





if __name__ == "__main__":
    main()