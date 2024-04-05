import random

questions = [
    ('the start of the Revolutionary War', 1775),
    ('the United States Constitution signed', 1783),
    ('President Lincoln assassinated', 1865),
    ("Theodore Roosevelt's first day in office as President of the United States", 1901),
    ('the beginning of World War II', 1939),
    ('the Berlin Wall taken down', 1989),
    ('the first personal computer introduced', 1975),
    ('When was D-Day', 1944),
    ('the detonation of the First ' + '\x1B[4m' + 'Hydrogen' + '\x1B[0m' + ' Bomb', 1952),
    ('YouTube launched', 2005)
]

points = 0
game_over = False


def increment_points(bonus):
    global points
    points += bonus


def check_answer(answer, guess):
    if check_range(answer, guess, 0):
        print('Correct! you got +10 score')
        increment_points(10)
    elif check_range(answer, guess, 5):
        print(f'Close! You were within 5 years! The correct answer was {answer} you got +5 score')
        increment_points(5)
    elif check_range(answer, guess, 10):
        print(f'Close! You were within 10 years! The correct answer was {answer} you got +2 score')
        increment_points(3)
    elif check_range(answer, guess, 20):
        print(f'Close! You were within 20 years! The correct answer was {answer} you got +1 score')
        increment_points(1)
    else:
        print('incorrect')


def ask_question(question, index):
    print(f'\nScore: {points}     Question {index + 1} of {len(questions)}')
    isValid = False
    while not isValid:
        print(f'When was {question[0]}')
        try:
            answer = input()
            if len(answer) >= 4:
                print(f"Invalid year, unless your from the future it's 2024 so try again")
            else:
                check_answer(question[1], int(answer))
                isValid = True
        except:
            print('invalid input, try again')


def check_range(answer, guess, tolerance):
    return abs(answer - guess) <= tolerance


def start_quiz():
    global game_over
    while not game_over:
        random.shuffle(questions)
        for question in questions:
            ask_question(question, questions.index(question))
        game_over = ask_restart_quiz()


def ask_restart_quiz():
    global points
    print(f'final score: {points} out of {len(questions) * 10}')
    print('Thank you for playing!\nWould you like to play again? Y/N')

    restart_option = input()
    restart_option.strip().lower()
    if restart_option == 'y' or restart_option == 'yes':
        points = 0
        return False
    else:
        print('Bye bye')
        return True


if __name__ == "__main__":
    start_quiz()
