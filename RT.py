#IMPORTS
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMessageBox, QRadioButton, QPushButton, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout
from random import randint
from PyQt5.QtGui import QFont

#WINDOW THINGS
app = QApplication([])
window = QWidget()

window.setWindowTitle("Ruffier Test")
window.resize(550,550)

#..... layout
main_layout = QVBoxLayout()

#Screen 1
screen1 = QVBoxLayout()

scr1_widgets = {
    "title" : QLabel("Rufiers Test"),
    "description" : QLabel("It's a cardiovascular endurance test. Click -Start- to begin."),
    "start_button" : QPushButton("Start")
}

for s1w in scr1_widgets.values():
    screen1.addWidget(s1w)

def start():
    scr2.show()
scr1_widgets["start_button"].clicked.connect(start)

#Screen 2
screen2 = QVBoxLayout()
scr2_widgets = {
    "name_label" : QLabel("Enter your full name:"),
    "name_input" : QLineEdit(),
    "age_label" : QLabel("Enter your age"),
    "age_input": QLineEdit(),
    "instructions1" : QLabel("Instructions"),
    "test_1" : QPushButton("Start the first test"),
    "p1_input" : QLineEdit(),
    "instructions2" : QLabel("Instructions #2"),
    "test_2": QPushButton("Start doing squats"),
    "instructions3" : QLabel("Instructions #3"),
    "test_3" : QPushButton("Start the final test"),
    "p2_input" : QLineEdit(),
    "p3_input" : QLineEdit(),
    "result_button" : QPushButton("Results")
}
for s2w in scr2_widgets.values():
    screen2.addWidget(s2w)

#Screen 3
screen3 = QVBoxLayout()

scr1 = QGroupBox()
scr2 = QGroupBox()
scr3 = QGroupBox()

scr1.setLayout(screen1)
scr2.setLayout(screen2)
scr3.setLayout(screen3)

main_layout.addWidget(scr1)
main_layout.addWidget(scr2)
main_layout.addWidget(scr3)

scr1.show()
scr2.hide()
scr3.hide()

#END
window.setLayout(main_layout)
window.show()
app.exec_()