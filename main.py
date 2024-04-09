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

form = tk.Tk()
points = 0
question = ('', 0)
index = 0

question_text_variable = tk.StringVar(value='')
hint_text_variable = tk.StringVar(value='')
score_text_variable = tk.StringVar(
    value=f"Score: {points}              Question: {index + 1} out of {questions.__len__()}")
lbl_hint_text = tk.Label(form, textvariable=hint_text_variable, wraplength=400)
lbl_question_text = tk.Label(form, textvariable=question_text_variable, wraplength=400)
entry = tk.Entry(form)
lbl_score_text = tk.Label(form, textvariable=score_text_variable)
submit_button = tk.Button(form, text='Submit')


def increment_points(bonus):
    global points, score_text_variable, index
    points += bonus
    score_text_variable.set(f"Score: {points}              Question: {index + 1} out of {questions.__len__()}")


def check_answer(answer, guess):
    global hint_text_variable
    if check_range(answer, guess, 0):
        increment_points(10)
        hint_text_variable.set("Correct! you got +10 score")
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
        increment_points(0)


def update_question_text():
    global question_text_variable, question
    question_text_variable.set(f'When was {question[0]}')


def check_guess(guess):
    global hint_text_variable, question, index
    try:
        if len(guess) != 4 or not guess.isdigit():
            hint_text_variable.set("Invalid year. Please enter a 4-digit number.")
            return False
        else:
            index += 1
            check_answer(question[1], int(guess))
            return True
    except ValueError:
        hint_text_variable.set("Try again.")


def check_range(answer, guess, tolerance):
    return abs(answer - guess) <= tolerance


def prompt_restart():
    global hint_text_variable, submit_button
    hint_text_variable.set(f'final score: {points} out of {len(questions) * 10}\nPress the button to restart the quiz')
    lbl_score_text.pack_forget()
    lbl_question_text.pack_forget()
    entry.pack_forget()
    submit_button.pack_forget()
    submit_button = tk.Button(form, text="Restart Quiz", command=restart_quiz)


def restart_quiz():
    global points, index, questions, submit_button, lbl_hint_text, hint_text_variable
    submit_button.pack_forget()
    lbl_hint_text.pack_forget()
    random.shuffle(questions)
    points = 0
    index = 0
    score_text_variable.set(f"Score: {points}              Question: {index + 1} out of {questions.__len__()}")

    submit_button = tk.Button(form, text="Submit", command=submit_answer)
    hint_text_variable.set('Quiz restarted, good luck!')
    update_ui()


def submit_answer():
    global index
    guess = entry.get()
    if check_guess(guess):
        entry.delete(0, 'end')
        update_question()
    if index != len(questions):
        update_ui()
    else:
        update_ui_restart()


def start_ui_quiz():
    global form, submit_button, questions, question
    random.shuffle(questions)
    update_question()
    form.title('A GUI to remember')
    form.geometry('400x150')
    update_question_text()

    submit_button = tk.Button(form, text="Submit Guess", command=submit_answer)

    update_ui()

    form.mainloop()


def update_question():
    global questions, index, lbl_question_text, hint_text_variable, question
    if index > questions.__len__() - 1:
        prompt_restart()
    else:
        question = questions[index]


def update_ui():
    global entry, submit_button, lbl_hint_text, lbl_score_text, lbl_question_text
    update_question_text()
    lbl_score_text.pack()
    lbl_question_text.pack()
    entry.pack()
    submit_button.pack()
    lbl_hint_text.pack()


def update_ui_restart():
    global lbl_hint_text, submit_button
    submit_button.pack()
    lbl_hint_text.pack()


if __name__ == "__main__":
    start_ui_quiz()
