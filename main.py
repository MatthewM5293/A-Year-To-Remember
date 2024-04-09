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
# UI stuff
form = tk.Tk()

question_text_variable = tk.StringVar(value='')
hint_text_variable = tk.StringVar(value='')
score_text_variable = tk.StringVar(value=f"Score: {points}")
question = ('', 0)
index = 0

lbl_hint_text = tk.Label(form, textvariable=hint_text_variable)
lbl_question_text = tk.Label(form, textvariable=question_text_variable, wraplength=400)
entry = tk.Entry(form)
lbl_score_text = tk.Label(form, textvariable=score_text_variable)
submit_button = tk.Button(form, text='Submit')


def increment_points(bonus):
    global points, score_text_variable
    points += bonus
    score_text_variable.set(f"Score: {points}")
    print(f"{points} points")


def check_answer(answer, guess):
    global hint_text_variable
    if check_range(answer, guess, 0):
        increment_points(10)
    elif check_range(answer, guess, 5):
        hint_text_variable.set(f"Close! You were within 5 years! The correct answer was {answer} you got +5 score")
        increment_points(5)
    elif check_range(answer, guess, 10):
        hint_text_variable.set(f'Close! You were within 10 years! The correct answer was {answer} you got +2 score')
        increment_points(3)
    elif check_range(answer, guess, 20):
        hint_text_variable.set(f'Close! You were within 20 years! The correct answer was {answer} you got +1 score')
        increment_points(1)
    else:
        hint_text_variable.set('incorrect')


def update_question_text():
    global question_text_variable, question
    question_text_variable.set(f'When was {question[0]}')


def check_guess(guess):
    global hint_text_variable, question
    try:
        if len(guess) != 4 or not guess.isdigit():
            hint_text_variable.set("Invalid year. Please enter a 4-digit number.")
            return False
        else:
            check_answer(question[1], int(guess))
            return True
    except:
        hint_text_variable.set("Try again.")


def check_range(answer, guess, tolerance):
    return abs(answer - guess) <= tolerance


def restart_quiz():
    global points, hint_text_variable, index
    hint_text_variable.set(f'final score: {points} out of {len(questions) * 10}')
    points = 0
    index = 0
    return update_ui()


def submit_answer():
    global index
    guess = entry.get()
    if check_guess(guess):
        entry.delete(0, 'end')
        index = index + 1
        update_question_text(update_question())
    update_ui()


def start_ui_quiz():
    global form, submit_button, questions
    random.shuffle(questions)
    question = update_question()
    form.title('A GUI to remember')
    form.geometry('400x150')
    update_question_text(question)

    submit_button = tk.Button(form, text="Submit Guess", command=submit_answer)

    update_ui()


def update_question():
    global questions, index, lbl_question_text, hint_text_variable
    if index > questions.__len__() - 1:
        restart_quiz()
        return questions[questions.__len__() - 1]
    else:
        return questions[index]


def update_ui():
    global entry, submit_button, lbl_hint_text, lbl_score_text, lbl_question_text, form
    lbl_score_text.pack()
    lbl_question_text.pack()
    entry.pack()
    submit_button.pack()
    lbl_hint_text.pack()

    form.mainloop()


if __name__ == "__main__":
    start_ui_quiz()
