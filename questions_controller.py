from main_window import *
from random import *
from main_window import *
from menu_window import *

class Question:
    def __init__(self, question, answer, wrong_ansswer1, wrong_ansswer2, wrong_ansswer3):

        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer1 = wrong_answer2
        self.wrong_answer1 = wrong_answer3

class Questioncontroler:
    def __init__(self):
        self.questions = []

        self.answer_buttons_widgets = [ans1_rbtn, ans2_rbtn, ans3_rbtn, ans4_rbtn,]
        self.question_widget = question_lbl
        self.result_widget = result_lbl

        self.answer_list = questions_list
        self.new_question_input_question = question_ledit
        self.new_question_input_answer = answer_ledit
        self.new_question_input_wrong1 = wrong1_ledit
        self.new_question_input_wrong2 = wrong2_ledit
        self.new_question_input_wrong3 = wrong3_ledit

    def shuffle_buttons(self):
        shuffle(self.answer_buttons_widgets)

    def choose_random_question(self):
        return choice(self.questions)
    
    def show_question(self)
        next_question = self.choose_random_question()

        self.shuffle_buttons()

        self.question_widget.setText(next_question.question)
        self.answer_buttons_widgets[0].setText(next_question.answer)
        self.answer_buttons_widgets[1].setText(next_question.wrong_answer1)
        self.answer_buttons_widgets[2].setText(next_question.wrong_answer2)
        self.answer_buttons_widgets[3].setText(next_question.wrong_answer3)

    def add_answer(self, question):
        self.questions.append(question)