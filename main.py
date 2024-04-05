import random

Q1 = ('the start of the Revolutionary War', 1775)
Q2 = ('the United States Constitution signed', 1783)
Q3 = ('President Lincoln assassinated', 1865)
Q4 = ("Theodore Roosevelt's first day in office as President of the United States", 1901)
Q5 = ('the beginning of World War II', 1939)
Q6 = ('the Berlin Wall taken down', 1989)
Q7 = ('the first personal computer introduced', 1975)
Q8 = ('When was D-Day', 1944)
Q9 = ('the detonation of the First ' + '\x1B[4m' + 'Hydrogen' + '\x1B[0m' + ' Bomb', 1952)
Q10 = ('YouTube launched', 2005)

questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]


def printQuestion(questionText):
    print(f'When was {questionText}?')


def initQuiz():
    random.shuffle(questions)
    startQuiz(questions, 0, 0)


def startQuiz(questions, index, points):
    for question in questions:
        isValidAnswer = False
        while not isValidAnswer:
            print(f'\nScore: {points}     Question {index+1} of {len(questions)}')
            printQuestion(question[0])

            userInput = input()
            try:
                int_year = int(userInput.strip())

                if int_year > 2024:
                    print("That hasn't happened yet! Try again!")
                else:
                    points += switch(int_year, question[1])
                    isValidAnswer = True
            except:
                print("Invalid input! Must be a year!")
    if index < len(questions) - 1:
        ++index

    print(f'final score: {points} out of {len(questions) * 10}')
    print('Thank you for playing!\nWould you like to play again? Y/N')

    userTry = input()
    if userTry == 'Y' or userTry == 'Yes':
        restartQuiz()
    else:
        print('Bye bye')


def restartQuiz():
    initQuiz()


def switch(inputYear, correctYear):
    if inputYear == correctYear:
        print(f'Correct! The correct answer was {correctYear} you got +10 score')
        return 10
    elif correctYear - 5 <= inputYear <= correctYear + 5:
        print(f'Close! You were within 5 years! The correct answer was {correctYear} you got +5 score')
        return 5
    elif correctYear - 10 <= inputYear <= correctYear + 10:
        print(f'Close! You were within 10 years! The correct answer was {correctYear} you got +2 score')
        return 2
    elif correctYear - 20 <= inputYear <= correctYear + 20:
        print(f'Close! You were within 20 years! The correct answer was {correctYear} you got +1 score')
        return 1
    else:
        return 0


if __name__ == '__main__':
    initQuiz()
