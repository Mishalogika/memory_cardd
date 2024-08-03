from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

window_main = QWidget()
window_main_layout = QVBoxLayout()

# віджети вікна #

menu_pbtn = QPushButton("Налштуваня")
rest_pbtn =  QPushButton("Відпочинок")
give_answer_pbtn = QPushButton()

rest_sbox = QSpinBox()
rest_sbox.setValue(30)

ans1_rbtn = QRadioButton("answer 1")
ans2_rbtn = QRadioButton("answer 2")
ans3_rbtn = QRadioButton("answer 3")
ans4_rbtn = QRadioButton("answer 4")

question_lbl = QLabel("Question")
minutes_lbl = QLabel(" хвилин")
result_lbl = QLabel("Правильна відповідь")

answers_gbox = QGroupBox()
result_gbox = QGroupBox()

header_layout = QHBoxLayout()

answer_gbox_layout = QHBoxLayout()
results_gbox_layout = QHBoxLayout()

answer_buttons_row1_layout = QHBoxLayout()
answer_buttons_row2_layout = QHBoxLayout()


header_layout.addWidget(menu_pbtn)
header_layout.addWidget(rest_pbtn)
header_layout.addWidget(rest_sbox)
header_layout.addWidget(minutes_lbl)
window_main_layout.addLayout(header_layout)

window_main_layout.addWidget(question_lbl)

answer_buttons_row1_layout.addWidget(ans1_rbtn)
answer_buttons_row1_layout.addWidget(ans2_rbtn)

answer_buttons_row2_layout.addWidget(ans3_rbtn)
answer_buttons_row2_layout.addWidget(ans4_rbtn)

answer_gbox_layout.addLayout(answer_buttons_row1_layout)
answer_gbox_layout.addLayout(answer_buttons_row2_layout)

answers_gbox.setLayout(answer_gbox_layout)
window_main_layout.addWidget(answers_gbox)

results_gbox_layout.addWidget(result_lbl)
result_gbox.setLayout(results_gbox_layout)
window_main_layout.addWidget(result_gbox)

window_main_layout.addWidget(give_answer_pbtn)

window_main.setLayout(window_main_layout)

