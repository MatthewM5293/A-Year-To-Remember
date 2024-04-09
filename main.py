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
    ('the detonation of the First Hydrogen Bomb', 1952),
    ('YouTube launched', 2005)
]

points = 0
game_over = False
# UI stuff
question_text = 'Test?'
hint_text = ''
score_text = 'Score: 0'
question = ('', 0)
index = 0

form = tk.Tk()
lbl_hint_text = tk.Label(form)
lbl_question_text = tk.Label(form, text=question_text)
entry = tk.Entry(form)
lbl_score_text = tk.Label(form)
submit_button = tk.Button(form, text='')


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


def ask_question(question):
    global question_text
    question_text = f'When was {question[0]}'  # Update question text


def check_guess(question, guess):
    global hint_text
    try:
        if len(guess) != 4 or not guess.isdigit():
            hint_text = "Invalid year. Please enter a 4-digit number."
        else:
            check_answer(question[1], int(guess))
    except:
        hint_text = "Try again."


def check_range(answer, guess, tolerance):
    return abs(answer - guess) <= tolerance


# def start_quiz():
#     global game_over
#     while not game_over:
#         random.shuffle(questions)
#         for question in questions:
#             ask_question(question, questions.index(question))
#         game_over = ask_restart_quiz()


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


# def create_ui():
#     global hint_text, question_text, score_text
#     form = tk.Tk()
#     form.title('A GUI to remember')
#     form.geometry('400x600')
#
#     lbl_hint_text = tk.Label(form, text=score_text)
#     lbl_hint_text.pack()
#
#     lbl_question_text = tk.Label(form, text=question_text)
#     lbl_question_text.pack()
#
#     guess_entry = tk.Entry(form, validate='key', width=4)
#     guess_entry.pack()
#
#     guessButton = tk.Button(form, text='Submit Guess', command=lambda: ask_question())
#     guessButton.pack()
#
#     form.mainloop()


def start_ui_quiz():
    global game_over, question_text, score_text, hint_text, form, entry, submit_button, lbl_hint_text, \
        lbl_score_text, lbl_question_text, question, index
    question = update_question()
    random.shuffle(questions)
    # question = questions[index]
    form.title('A GUI to remember')
    form.geometry('400x600')
    ask_question(question)

    score_text = f'Score: {points}'

    lbl_score_text = tk.Label(form, text=score_text)
    lbl_score_text.pack()

    lbl_question_text = tk.Label(form, text=question_text)
    lbl_question_text.pack()

    entry = tk.Entry(form)
    entry.pack()

    def submit_answer():
        global question, index
        guess = entry.get()
        check_guess(question, guess)
        entry.delete(0, 'end')
        index = index + 1
        ask_question(update_question())

    submit_button = tk.Button(form, text="Submit Guess", command=submit_answer)
    submit_button.pack()

    lbl_hint_text = tk.Label(form, text=hint_text)
    lbl_hint_text.pack()

    form.mainloop()


def update_question():
    global questions, game_over, index, lbl_question_text
    if index > questions.__len__() - 1:
        game_over = True
    else:
        return questions[index]


if __name__ == "__main__":
    start_ui_quiz()
