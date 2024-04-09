import random
import tkinter as tk

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
# UI stuff
question_text = 'Test?'
hint_text = 'Close!'
score_text = 'Score: 0'


def increment_points(bonus):
    global points
    points += bonus


def check_answer(answer, guess):
    global hint_text
    if check_range(answer, guess, 0):
        hint_text = 'Correct! you got +10 score'
        increment_points(10)
    elif check_range(answer, guess, 5):
        hint_text = f'Close! You were within 5 years! The correct answer was {answer} you got +5 score'
        increment_points(5)
    elif check_range(answer, guess, 10):
        hint_text = f'Close! You were within 10 years! The correct answer was {answer} you got +2 score'
        increment_points(3)
    elif check_range(answer, guess, 20):
        hint_text = f'Close! You were within 20 years! The correct answer was {answer} you got +1 score'
        increment_points(1)
    else:
        hint_text = 'incorrect'


def ask_question(question, index):
    global question_text, score_text, hint_text
    score_text = f'Score: {points}     Question {index + 1} of {len(questions)}'
    isValid = False
    while not isValid:
        question_text = f'When was {question[0]}'
        try:
            answer = input()  # change to be UI input
            if len(answer) >= 4:
                hint_text = f"Invalid year, unless your from the future it's 2024 so try again"
            else:
                check_answer(question[1], int(answer))
                isValid = True
        except:
            print('invalid input, try again')


def check_range(answer, guess, tolerance):
    return abs(answer - guess) <= tolerance


def start_quiz():
    global game_over
    create_ui()
    while not game_over:
        random.shuffle(questions)
        for question in questions:
            ask_question(question, questions.index(question))
        game_over = ask_restart_quiz()


def ask_restart_quiz():
    global points, hint_text
    hint_text = f'final score: {points} out of {len(questions) * 10}'
    print('Thank you for playing!\nWould you like to play again? Y/N')

    restart_response = input()  # UI input
    restart_response.strip().lower()
    if restart_response == 'y' or restart_response == 'yes':
        points = 0
        return False
    else:
        hint_text = 'Bye bye'
        return True


# NumEntry custom widget
class NumberEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(validate="key", validatecommand=(self.register(self.validate), "%P"))

    def validate(self, new_text):
        if new_text == "":
            return True
        try:
            float(new_text)
            return True
        except ValueError:
            return False


def create_ui():
    global hint_text, question_text, score_text
    form = tk.Tk()
    form.title('A GUI to remember')
    form.geometry('400x600')

    lblHintText = tk.Label(form, text=score_text)
    lblHintText.pack()

    lblQuestionText = tk.Label(form, text=question_text)
    lblQuestionText.pack()

    guessEntry = tk.Entry(form, validate='key', width=4)
    guessEntry.pack()

    guessButton = tk.Button(form, text='Submit Guess')
    guessButton.pack()

    form.mainloop()


def update_ui():
    global points, hint_text, question_text, score_text
    score_text = points.__str__()
    # update labels with text and clear input field


if __name__ == "__main__":
    start_quiz()
